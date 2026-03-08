# -- coding: utf-8 --

# Copyright (C) 2026 GroundServicesJP
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

########################################################################

# Airport handler script for RJTT (profile: rjtt-karuchie)
# Applies to all aircraft at RJTT
# Version 0.9 Beta

# Top Level Defines
PROFILE_STEM = "rjtt-karuchie"
BRANCH_STEM = "handler_test"
AIR_OPR_CORRELATION_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/airline_operator_corr_dicts/{PROFILE_STEM}_corr_dict.json"
INI_PROFILE_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/{PROFILE_STEM}.ini"
PY_PROFILE_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/{PROFILE_STEM}.py"

# Debug Flags
DISABLE_AUTO_OPR_SELECTION = False # Set to True to disable automatic operator selection based on airline ICAO code, and always use profile defaults
DISABLE_AUTO_PROFILE_UPDATES = True # Set to True to disable automatic fetching of profile updates from GitHub, and always use local files

# Shared library checks
def try_require(req_name):
  try:
    return require(req_name)
  except Exception as e:
    print(f"[GSJP] Failed to load library: {req_name}, Error: {e}")
    return None

def checkRequirements():
  global mototok_handler, operator_correlator, auto_profile_fetcher, model_disabler
  operator_correlator = try_require("gsjp_operator_correlation_v1")
  auto_profile_fetcher = try_require("gsjp_auto_profile_fetch_v1")
  model_disabler = try_require("gsjp_model_disabler_v1")
  all_libs_available = (operator_correlator is not None
                        and auto_profile_fetcher is not None
                        and model_disabler is not None)

  if not all_libs_available:
    message_1 = "必要なGSXライブラリがインストールされていません。\n" \
                "Failed to load one or more required GSX Handler libraries."
    message_2 = "以下のページをご覧ください。\nSee the following page on how to install:"
    message_3 = "https://gsjp.info/gsx-handlers"

    messageBox(f"{message_1}\n{message_2}\n{message_3}",
               caption="ERROR", style=MB_OK | MB_ICONERROR)
    
# Operator-Airline Correlation Matrix
# Fallback hardcoded dict in case the remote fetch fails
FALLBACK_AIRLINE_OPERATOR_CORRELATION = {
  "ANA": ("ANA", "ANA"),
  "AKX": ("ANA", "ANA"),
  "AJX": ("ANA", "ANA"),
  "APJ": ("ANA", "ANA"),
  "ADO": ("ANA", "ANA"),
  "SNJ": ("6J", "ANA"),
  "SFJ": ("ANA", "ANA"),
  "JAL": ("JL", (("JAL", "JAL Royal Catering [INTL]"), ("TFK", "TFK [Domestic]"))),
  "JTA": ("JL", "TFK"),
  "JLJ": ("JL", "TFK"),
  "JAC": ("JL", "TFK"),
  "NTH": ("JL", "TFK"),
  "JJP": ("JL", "TFK"),
  "SJO": ("JL", "TFK"),
  "SKY": ("BC", "TFK"),
  "UAE": ("SWISSPORT", "GGOURMET"),
  "THA": ((("CKTS", "CKTS [Ground Handling and Pushback]"), ("HTS", "Haneda Turtle Service [Towing Only]")), "GGOURMET"), 
  "AFR": ("SWISSPORT", "TFK"),
  "AAR": ("ANA", "ANA"),
  "HKE": ("SWISSPORT", "TFK"),
  "PAL": ("ANA", "COSMO"),
  "KAL": ("KAAS", "TFK"),
  "DKH": ("SWISSPORT", "ANA"),
  "GCR": ("CKTS", ""),
  "VJC": ("SWISSPORT", "TFK"),
  "TTW": ("HTS", ""),
  "CAL": ("JAL", "COSMO"),
  "CCA": ("JAL", "TFK"),
  "CES": ("JAL", "TFK"),
  "QFA": ("JAL", "GGOURMET"),
  "SIA": ("ANA", "ANA"),
  "BAW": ("JAL", "COSMO"),
  "CPA": ("CKTS", "COSMO"),
  "EVA": ("ANA", "ANA"),
  "CSN": ("JAL", "TFK"),
  "DLH": ("ANA", "GGOURMET"),
  "GIA": ("ANA", "ANA"),
  "AAL": ("JAL", "COSMO"),
  "ITY": ("JAL", "TFK"),
  "CSH": ("CKTS", "TFK"),
  "DAL": ("HTS", "TFK"),
  "UAL": ("JAL", "GGOURMET"),
  "HVN": ("ANA", "ANA"),
  "ACA": ("HTS", "TFK"),
  "HAL": ("JAL", "COSMO"),
  "VOZ": ("SWISSPORT", "TFK"),
  "FIN": ("CKTS", "ANA"),
  "THY": ("JAL", "TFK"),
  "XAX": ("CKTS", "TFK"),
  "CQH": ("JAL", "TFK"),
  "SAS": ("SWISSPORT", "TFK"),
  "AIC": ("SWISSPORT", "TFK")
}

############################### VDGS TSAT Display Logic ###############################
# Persistent TSAT data storage
# ``current_tsat_data`` holds a (hour, minute) tuple when available.
# ``None`` indicates no TSAT has been seen yet.
current_tsat_data = None  # type: tuple[int, int] | None
# Track the source of current TSAT data ('VATSIM' or 'Simbrief')
# This determines which UTC time to use for countdown calculations
current_tsat_source = None  # type: str | None
# Track previous source locally to detect changes
prev_source = None  # type: str | None

def create_tsat_data(*args):
  """
  Create TSAT data as (hour, minute) tuple.

  Usage:
  - create_tsat_data("1325")          # HHMM string
  - create_tsat_data(13, 25)          # hour, minute
  """
  if len(args) == 1 and isinstance(args[0], str):
    # From HHMM string
    tsat_str = args[0]
    hour = int(tsat_str[:2])
    minute = int(tsat_str[2:])
  elif len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
    # From hour and minute
    hour, minute = args
  else:
    return None
  
  return (hour, minute)

def format_tsat_data(tsat_data):
  """Return formatted HH:MM string from (hour, minute) tuple"""
  if tsat_data is None:
    return "None"
  return f"{tsat_data[0]:02d}:{tsat_data[1]:02d}"

def in_tsat_operation_time(tsat_data):
  """
  Check if this time is inside TSAT operation interval:
  2120 UTC to 1359 UTC (wraps past midnight)
  """
  if tsat_data is None:
    return False
  
  utc_hour, utc_minute = tsat_data
  utc_seconds_total = utc_hour * 60 + utc_minute

  start = 21 * 60 + 20 # begin time 2120 UTC for RJTT
  end   = 13 * 60 + 59 # end time 1359 UTC for RJTT

  if start <= end:
    return start <= utc_seconds_total <= end
  else:
    # Interval wraps past midnight
    return utc_seconds_total >= start or utc_seconds_total <= end

def calculate_countdown_tsat(tsat_data, simvar_utc_seconds):
  """
  Calculate countdown in minutes relative to TSAT data.
  Negative -> minutes before departure
  Positive -> minutes after departure
  Wraps correctly around midnight.
  """
  if tsat_data is None:
    return None
  
  current_minutes = int(simvar_utc_seconds) // 60
  tsat_minutes = tsat_data[0] * 60 + tsat_data[1]

  # Difference modulo 24h
  diff = (current_minutes - tsat_minutes) % 1440
  if diff > 720:  # more than 12h ahead -> treat as negative
    diff -= 1440
  return diff

def poll_tsat_data_from_simbrief_data(simbrief_data):
  if simbrief_data:
    tsat_data = create_tsat_data(simbrief_data.sched_out.tm_hour, simbrief_data.sched_out.tm_min)
    return tsat_data
  else:
    return None
  
def poll_tsat_data_from_vatsim_data(vatsim_data):
  if vatsim_data: 
    vatsim_cid = getGlobalPersistentVariable("gsjp_vatsim_cid", default=None)
    pilots = vatsim_data.get('pilots', [])
    for pilot in pilots:
      if str(pilot.get('cid')) == str(vatsim_cid) and pilot.get('flight_plan', {}).get('departure') == 'RJTT':
        print("[GSJP VDGS Display - Data Acquisition] Found matching VATSIM pilot with CID and departure RJTT.")
        vatsim_fp = pilot.get('flight_plan')
        if vatsim_fp:
          tsat_data = create_tsat_data(vatsim_fp.get('deptime', ''))
          callsign_result = pilot.get('callsign', None)
          return tsat_data, callsign_result
    return None, None # In case I cannot find data in list of all pilots
  else: 
    return None, None

def check_and_notify_data_source_change(callsign, is_fallback=False):
  """Show message box if data source changed or is first TSAT."""
  global prev_source
  
  # Show message box on first TSAT or when source changes
  if prev_source != current_tsat_source:
    print(f"[GSJP VDGS Display - Data Acquisition] TSAT data source changed from {prev_source} to {current_tsat_source}.")
    message = ""
    if current_tsat_source == 'VATSIM':
      print(f"[GSJP VDGS Display - Data Acquisition] Updated TSAT Data from VATSIM: {format_tsat_data(current_tsat_data)}. Callsign: {callsign}.")
      if is_fallback:
        message += "ご希望のデータソースから取得できません。代替ソースのTSATを使用します。\n"
        message += "Primary data source is not available. \nUsing TSAT from fallback source.\n"
      message += f"Source: {current_tsat_source}, Callsign: {callsign}\n"
      message += "\n"
      message += "TSATはVATSIM FPLのEOBTから算出されています。\n"
      message += "Using VATSIM FPL EOBT as TSAT.\n"
      message += "管制官から、EOBTとは異なるTSATが提供される場合があります。\n"
      message += "ATC may issue a TSAT different from your EOBT.\n"
      message += "カウントダウン計算にはリアルなUTCを使用します。\n"
      message += "Using real-world UTC for countdown calculation."

    elif current_tsat_source == 'Simbrief':
      print(f"[GSJP VDGS Display - Data Acquisition] Updated TSAT Data from Simbrief: {format_tsat_data(current_tsat_data)}. Callsign: {callsign}.")
      if is_fallback:
        message += "ご希望のデータソースから取得できません。代替ソースのTSATを使用します。\n"
        message += "Primary data source is not available. Using TSAT from fallback source.\n"
      message += f"Source: {current_tsat_source}, Callsign: {callsign}\n"
      message += "\n"
      message += "TSATはSimbriefの出発時刻から算出されています。\n"
      message += "Using Simbrief Off-block time as TSAT.\n"
      message += "カウントダウン計算にはゲーム内UTCを使用します。\n"
      message += "Using in-game UTC for countdown calculation."

    messageBox(message, caption="GroundServicesJP TSAT Display", style=MB_OK | MB_ICONINFO)
    prev_source = current_tsat_source

def poll_tsat_data_from_simbrief():
  """ Statically fetch TSAT data from Simbrief and update global `current_tsat_data`.
    This is a simpler alternative to the VATSIM polling function, which is used when user selects Simbrief-only mode.
    Simbrief data is fetched once and used as the TSAT source.
  """
  global current_tsat_data, current_tsat_source
  
  simbrief_data = getSimbrief()
  if simbrief_data and simbrief_data.flight_number and simbrief_data.icao_airline:
    simbrief_callsign = f"{simbrief_data.icao_airline}{simbrief_data.flight_number}"
    tsat_data = poll_tsat_data_from_simbrief_data(simbrief_data)
    if (tsat_data != None) and (in_tsat_operation_time(tsat_data)):
      current_tsat_data = tsat_data
      current_tsat_source = 'Simbrief'
      check_and_notify_data_source_change(simbrief_callsign)
    else:
      # TSAT fetching attempts failed, but keep existing TSAT if available
      print("[GSJP VDGS Display - Data Acquisition] Could not fetch valid TSAT data. Using existing TSAT:", format_tsat_data(current_tsat_data))
  else: 
    # No simbrief data, but keep existing TSAT if available
    print("[GSJP VDGS Display - Data Acquisition] No valid simbrief data. Using existing TSAT:", format_tsat_data(current_tsat_data))

def _poll_tsat_data_from_vatsim():
  """Asynchronously fetch TSAT data from available sources and update
  the global `current_tsat_data` variable.

  This function does **not** modify VDGS state.  All display logic is
  performed by the separate update loop (`_update_vdgs_from_tsat`),
  which monitors `current_tsat_data` for changes and handles the CHG/DLA
  countdown behaviour.
  """
  global current_tsat_data, current_tsat_source
  
  while True:
    # First check VATSIM for a TSAT value
    vatsim_data = fetchJson("https://data.vatsim.net/v3/vatsim-data.json", timeout=15)
    tsat_data, vatsim_callsign = poll_tsat_data_from_vatsim_data(vatsim_data)
    if (tsat_data != None) and (in_tsat_operation_time(tsat_data)):
      current_tsat_data = tsat_data
      current_tsat_source = 'VATSIM'
      check_and_notify_data_source_change(vatsim_callsign)
      truewait(30000) # Wait 30 sec before next poll
      continue
    # fallback to Simbrief if VATSIM had no valid TSAT
    simbrief_data = getSimbrief()
    if simbrief_data and simbrief_data.flight_number and simbrief_data.icao_airline:
      simbrief_callsign = f"{simbrief_data.icao_airline}{simbrief_data.flight_number}"
      tsat_data = poll_tsat_data_from_simbrief_data(simbrief_data)
      if (tsat_data != None) and (in_tsat_operation_time(tsat_data)):
        current_tsat_data = tsat_data
        current_tsat_source = 'Simbrief'
        check_and_notify_data_source_change(simbrief_callsign, is_fallback=True)
        truewait(30000) # Wait 30 sec before next poll
        continue
      # TSAT fetching attempts failed, but keep existing TSAT if available
      print("[GSJP VDGS Display - Data Acquisition] Could not fetch valid TSAT data. Using existing TSAT:", format_tsat_data(current_tsat_data))
    else: 
      # No simbrief data, but keep existing TSAT if available
      print("[GSJP VDGS Display - Data Acquisition] Could not fetch valid TSAT data. Using existing TSAT:", format_tsat_data(current_tsat_data))
    truewait(30000) # Wait 30 sec before next poll

def poll_msfs_utc_time():
  msfs_utc_seconds = executeCalculatorCode("(E:ZULU TIME, seconds)")
  return msfs_utc_seconds

def poll_real_world_utc_time():
  real_world_utc_seconds = fetchJson("https://timeapi.io/api/Time/current/zone?timeZone=UTC", timeout=2)
  if real_world_utc_seconds and 'hour' in real_world_utc_seconds and 'minute' in real_world_utc_seconds:
    hour = int(real_world_utc_seconds['hour'])
    minute = int(real_world_utc_seconds['minute'])
    return hour * 3600 + minute * 60
  else: # Try second source
    real_world_utc_seconds = fetchJson("https://time.now/developer/api/ip", timeout=2)
    if real_world_utc_seconds and 'utc_datetime' in real_world_utc_seconds:
      time_str = real_world_utc_seconds['utc_datetime']
      hour = int(time_str[11:13])
      minute = int(time_str[14:16])
      return hour * 3600 + minute * 60
  
  return None

def resetVDGSVariables():
  print("[GSJP VDGS Display - Data Display] TSAT not available or not displayable at the moment. Clearing VDGS variables.")
  removeVdgsVariable('vdgs_tsat')
  removeVdgsVariable('countdown_screen')

def setTSATVDGSVariables(tsat_data, display_str):
  """Update VDGS variables for TSAT display.

  display_str values:
  * 'CHG' - change indicator
  * 'DLA' - departure delayed/after time
  * any other string - numeric countdown (negative minutes before)

  Note: Caller is responsible for ensuring the TSAT template is set.
  """
  if display_str == 'CHG':
    print("[GSJP VDGS Display - Data Display] Setting CHG in VDGS.")
  elif display_str == 'DLA':
    print("[GSJP VDGS Display - Data Display] Setting DLA in VDGS.")
  else:
    # numeric countdown is expected
    minutes = int(display_str)
    print(f"[GSJP VDGS Display - Data Display] Setting countdown of {-minutes} minutes in VDGS.")

  setVdgsVariable('tsat_data', format_tsat_data(tsat_data))
  setVdgsVariable('countdown_screen', display_str)

def setJapaneseGenericVDGSMessage():
	# Replace the stock flight info page with Japanese style content
	addVdgsMessage({
		"id": "chock_and_gate_display",
		"display": {
			"narrow": {
        "pages": [
          {
            "lines": [
              "",
              "",
              "",
              "",
              "",
              ""
            ],
            "duration": 6000
          }
        ]
      },
			"wide": {
				"pages": [
					{
						"lines": [
							"",
							"",
							"",
							"",
							"",
							"",
							""
						],
						"duration": 6000
					}
				]
			}
		}
	})

	addVdgsMessage({
		"id": "flight_information",
		"display": {
			"narrow": {
        "pages": [
          {
            "lines": [
              "",
              "",
              "",
              "",
              "",
              ""
            ],
            "duration": 6000
          }
        ]
      },
			"wide": {
				"pages": [
					{
						"lines": [
							"",
							"",
							"",
							"",
							"",
							"",
							""
						],
						"duration": 6000
					}
				]
			}
		}
	})

	addVdgsMessage({
		"id": "passenger_cargo_info",
		"display": {
			"narrow": {
        "pages": [
          {
            "lines": [
              "",
              "",
              "",
              "",
              "",
              ""
            ],
            "duration": 6000
          }
        ]
      },
			"wide": {
				"pages": [
					{
						"lines": [
							"",
							"",
							"",
							"",
							"",
							"",
							""
						],
						"duration": 6000
					}
				]
			}
		}
	})

	print("[GSJP VDGS Display - Data Display] Set Japanese style generic VDGS template.")

def setJapaneseTSATVDGSMessage():
	# Replace the stock flight info page with Japanese style content
	addVdgsMessage({
		"id": "chock_and_gate_display",
		"display": {
			"narrow": {
        "pages": [
          {
            "lines": [
              "TSAT",
              "${tsat_data}",
              "${countdown_screen}",
              "",
              "",
              ""
            ],
            "duration": 10000
          }
        ]
      },
			"wide": {
				"pages": [
					{
						"lines": [
							"TSAT",
              "${tsat_data}",
              "${countdown_screen}",
							"",
							"",
							"",
							""
						],
						"duration": 10000
					}
				]
			}
		}
	})

	addVdgsMessage({
		"id": "flight_information",
		"display": {
			"narrow": {
        "pages": [
          {
            "lines": [
              "TSAT",
              "${tsat_data}",
              "${countdown_screen}",
              "",
              "",
              ""
            ],
            "duration": 10000
          }
        ]
      },
			"wide": {
				"pages": [
					{
						"lines": [
							"TSAT",
              "${tsat_data}",
              "${countdown_screen}",
							"",
							"",
							"",
							""
						],
						"duration": 10000
					}
				]
			}
		}
	})

	addVdgsMessage({
		"id": "passenger_cargo_info",
		"display": {
			"narrow": {
        "pages": [
          {
            "lines": [
              "TSAT",
              "${tsat_data}",
              "${countdown_screen}",
              "",
              "",
              ""
            ],
            "duration": 10000
          }
        ]
      },
			"wide": {
				"pages": [
					{
						"lines": [
							"TSAT",
              "${tsat_data}",
              "${countdown_screen}",
							"",
							"",
							"",
							""
						],
						"duration": 10000
					}
				]
			}
		}
	})

	print("[GSJP VDGS Display - Data Display] Set Japanese style TSAT VDGS template.")

def _update_vdgs_from_tsat():
  """Periodically compute and update VDGS messages from current TSAT, but only act on change

  Special handling:
  * when TSAT time is modified we show a 'CHG' message for 3 minutes
  * if the new TSAT already yields a non-negative countdown the CHG step is skipped
  """
  prev_tsat_data = None  # type: tuple[int, int] | None
  # local counter for CHG display (ticks of 5 sec, same as async period)
  chg_counter = 0  # type: int
  # track which template is currently active: 'GENERIC' or 'TSAT'
  active_template = None  # type: str | None
  # track previous countdown/display value for template refresh detection
  prev_countdown_display = None  # type: str | None

  def tsat_is_available():
    """Check if TSAT data is currently available."""
    return current_tsat_data is not None

  def clear_tsat_display():
    """Clear TSAT display state and revert to generic VDGS message."""
    nonlocal prev_tsat_data, active_template, prev_countdown_display
    resetVDGSVariables()
    setJapaneseGenericVDGSMessage()
    active_template = 'GENERIC'
    prev_countdown_display = None
    prev_tsat_data = None

  def is_first_time_tsat_data():
    """Check if this is the first time we see a TSAT value."""
    return prev_tsat_data is None

  def saved_tsat_data_has_changed():
    """Check if TSAT value has changed from the previously tracked value."""
    return current_tsat_data != prev_tsat_data
  
  def record_prev_tsat_data():
    """Save the current TSAT value for later comparison."""
    nonlocal prev_tsat_data
    prev_tsat_data = current_tsat_data

  def is_DLA(count_down):
    """Check if the countdown indicates a departure delay (non-negative)."""
    return count_down is not None and count_down > 0

  def update_display(count_down, chg_active=False):
    """Perform the usual countdown/DLA/timeout logic.

    Sets VDGS variables. Template is set separately when needed.
    """
    nonlocal prev_tsat_data, active_template, prev_countdown_display

    if count_down is None:
      # No valid countdown can be calculated
      if active_template == 'TSAT':
        clear_tsat_display()
      return

    # out-of-range takes precedence; clear/skip display if out of range
    if (count_down < -20) or (count_down > 30):
      if active_template == 'TSAT':
        clear_tsat_display()
      return

    # Determine what display string to use
    if chg_active:
      display_str = 'CHG'
    elif is_DLA(count_down):
      display_str = 'DLA'
    else:
      display_str = str(count_down)

    if display_str != prev_countdown_display or prev_tsat_data != current_tsat_data:
      # Only update VDGS variables if the display content has changed to avoid unnecessary refreshes
      # TSAT is valid; ensure template is active
      if active_template != 'TSAT':
        print("[GSJP VDGS Display - Data Display] TSAT available but template was not active - re-activating TSAT template")
        setJapaneseTSATVDGSMessage()
        active_template = 'TSAT'
      setTSATVDGSVariables(current_tsat_data, display_str)
      prev_countdown_display = display_str

    prev_tsat_data = current_tsat_data

  while True:
    if not tsat_is_available():
      if active_template != 'GENERIC':
        print("[GSJP VDGS Display - Data Display] Switching to GENERIC template (no TSAT)")
        setJapaneseGenericVDGSMessage()
        active_template = 'GENERIC'
    else:
      # Use appropriate UTC time based on TSAT source
      if current_tsat_source == 'VATSIM':
        utc_seconds = poll_real_world_utc_time()
      else: # Use MSFS UTC time for Simbrief or if source is None
        utc_seconds = poll_msfs_utc_time()
      if utc_seconds is not None:
        count_down = calculate_countdown_tsat(current_tsat_data, utc_seconds)
      else:
        count_down = None # Unable to calculate countdown without valid UTC time

      if is_first_time_tsat_data():
        # initial TSAT seen – activate template first, then set variables
        if active_template != 'TSAT':
          print("[GSJP VDGS Display - Data Display] First TSAT arrival - activating TSAT template")
          setJapaneseTSATVDGSMessage()
          active_template = 'TSAT'
        update_display(count_down, chg_active=False)
        record_prev_tsat_data()
      else: # Not first time seeing TSAT, we need consider if CHG is required to be posted. 
        if saved_tsat_data_has_changed():
          # TSAT changed from previous value
          if active_template != 'TSAT':
            setJapaneseTSATVDGSMessage()
            active_template = 'TSAT'
          # Always show CHG when TSAT changes, regardless of countdown value
          chg_counter = 36 # 3 minutes of CHG at 5 sec per tick -> 36 ticks
          update_display(count_down, chg_active=True)
          record_prev_tsat_data()
        else: # is same TSAT as before, CHG counter still on going
          if chg_counter > 0:
            # still in change-display window; just show CHG each tick
            update_display(count_down, chg_active=True)
            chg_counter -= 1
          else:
            update_display(count_down, chg_active=False)

    truewait(5000) # Check to see if VDGS messages update needed every 5 sec (but may do nothing)

def setVATSIMCID():
  vatsim_cid_candidate = getGlobalPersistentVariable("gsjp_vatsim_cid", default=None)
  message = "VATSIM CIDを入力してください。\nPlease enter your VATSIM CID. \n"
  message += "もしCIDを変更したいのであれば、GSXを再起動してください。\n"
  message += "If you would like to change your CID, please restart GSX."
  vatsim_cid_input = inputBox(message, 
                              caption="GroundServicesJP TSAT Display", 
                              defaultValue=vatsim_cid_candidate)
  if vatsim_cid_input is not None and vatsim_cid_input.isdigit():
    setGlobalPersistentVariable("gsjp_vatsim_cid", vatsim_cid_input.strip())
    print("[GSJP VDGS Display - Data Acquisition] Set VATSIM CID.")
  else: 
    messageBox("CID番号は無効です。Invalid CID.", caption="GroundServicesJP TSAT Display", style=MB_OK | MB_ICONWARNING)

def checkTSATSourceSelection(self):
  print("[GSJP VDGS Display - Data Acquisition] Pulling up Data Source Choice Menu.")
  tsat_data_source_options = ["VATSIM", 'Simbrief (Default)']
  tsat_data_source_choice = choiceBox("TSATデータソースを選択してください。\nPlease select TSAT Data Source.",
                                      caption="GroundServicesJP TSAT Display",
                                      choices=tsat_data_source_options,
                                      default=1)
  if tsat_data_source_choice == 0:
    # Current source is VATSIM
    setVATSIMCID()
    runAsync(_poll_tsat_data_from_vatsim)
  else:
    # Current source is Simbrief (selected index 1, or None on cancel)
    truewait(100) # Small delay to ensure Simbrief is ready
    poll_tsat_data_from_simbrief()

############################### END VDGS TSAT Display Logic ###############################

################################ Inject in GSX Hooks ###############################
def onEnterAirport(self):
  checkRequirements()
  if not DISABLE_AUTO_PROFILE_UPDATES:
    auto_profile_fetcher.checkIfNeedAutoFetchProfile(self, INI_PROFILE_URL, PY_PROFILE_URL)

def onAirportAircraftEngaged(self):
  # Check if gate needs VDGS Display
  gate = getGate()
  if gate and "SafeDock" in gate.parkingSystem:
    print("[GSJP VDGS Display - Data Display] Gate has SafeDock system. Start VDGS display.")
    runAsync(_update_vdgs_from_tsat)
    

def onAirportBeforeVehicleSelect(self):
  # Check if gate needs VDGS Display
  gate = getGate()
  if gate:
    if "SafeDock" in gate.parkingSystem:
      print("[GSJP VDGS Display - Data Acquisition] Gate has SafeDock system. Prompting for TSAT data source selection.")
      checkTSATSourceSelection(self)
    if not DISABLE_AUTO_OPR_SELECTION:
      operator_correlator.checkIfNeedAirlineOperatorCorrelation(self, aircraft.icaoAirline, FALLBACK_AIRLINE_OPERATOR_CORRELATION, AIR_OPR_CORRELATION_URL)

def onVehicleCandidatesScored(self, vehicleType, candidates):
  if "BaggageLoader" in vehicleType:
    model_disabler.disableCCL35S(self, candidates)
  if "PassengerBus" in vehicleType:
    model_disabler.disableNeoplan(self, candidates)