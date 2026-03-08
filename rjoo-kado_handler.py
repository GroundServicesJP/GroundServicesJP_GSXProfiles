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

# Airport handler script for RJOO (profile: rjoo-kado)
# Applies to all aircraft at RJOO
# Version 0.9 Beta

# Top Level Defines
PROFILE_STEM = "rjoo-kado"
BRANCH_STEM = "handler_test"
AIR_OPR_CORRELATION_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/airline_operator_corr_dicts/{PROFILE_STEM}_corr_dict.json"
INI_PROFILE_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/{PROFILE_STEM}.ini"
PY_PROFILE_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/{PROFILE_STEM}.py"

# Debug Flags
DISABLE_AUTO_PROFILE_UPDATES = False # Set to True to disable automatic fetching of profile updates from GitHub, and always use local files
DISABLE_AUTO_OPR_SELECTION = False # Set to True to disable automatic operator selection based on airline ICAO code, and always use profile defaults
DISABLE_AUTO_MOTOTOK_RESTRICTION = False # Set to True to disable automatic restriction of Mototok usage based on aircraft weight and airline, and always allow Mototok at Mototok gates

# Shared library checks
def try_require(req_name):
  try:
    return require(req_name)
  except Exception as e:
    print(f"[GSJP] Failed to load library: {req_name}, Error: {e}")
    return None

def checkRequirements():
  global mototok_handler, operator_correlator, auto_profile_fetcher, model_disabler
  mototok_handler = try_require("gsjp_mototok_handler_v1")
  operator_correlator = try_require("gsjp_operator_correlation_v1")
  auto_profile_fetcher = try_require("gsjp_auto_profile_fetch_v1")
  model_disabler = try_require("gsjp_model_disabler_v1")
  all_libs_available = (mototok_handler is not None
                        and operator_correlator is not None
                        and auto_profile_fetcher is not None
                        and model_disabler is not None)

  if not all_libs_available:
    message_1 = "必要なGSXライブラリがインストールされていません。\n" \
                "One or more required GSX Handler libraries are missing."
    message_2 = "以下のページをご覧ください。\nSee the following page on how to install:"
    message_3 = "https://gsjp.info/gsx-handlers"

    messageBox(f"{message_1}\n{message_2}\n{message_3}",
               caption="ERROR", style=MB_OK | MB_ICONERROR)

######################## GSJP VDGS ########################
def setJapaneseGenericVDGSMessage(self):
  # Replace the stock flight info page with Japanese style content
  addVdgsMessage({
    "id": "chock_and_gate_display",
    "display": {
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

  print("[GSJP VDGS Display] Set Japanese style generic VDGS message.")

######################## END GSJP VDGS ########################

# Operator-Airline Correlation Matrix
# Fallback hardcoded dict in case the remote fetch fails
FALLBACK_AIRLINE_OPERATOR_CORRELATION = {
  "ANA": ("ANA", "AAS"),
  "AKX": ("ANA", "AAS"),
  "AJX": ("ANA", "AAS"),
  "APJ": ("ANA", "AAS"),
  "ADO": ("ANA", "AAS"),
  "SNJ": ("ANA", "AAS"),
  "SFJ": ("ANA", "AAS"),
  "IBX": ("ANA", "AAS"),
  "JAL": ("JL", "AAS"),
  "JTA": ("JL", "AAS"),
  "JLJ": ("JL", "AAS"),
  "JAC": ("JL", "AAS"),
  "NTH": ("JL", "AAS"),
  "AHX": ("JL", "AAS"),
  "JJP": ("JL", "AAS"),
  "SJO": ("JL", "AAS")
}

################################ Inject in GSX Hooks ###############################
def onEnterAirport(self):
  checkRequirements()
  if not DISABLE_AUTO_PROFILE_UPDATES:
    auto_profile_fetcher.checkIfNeedAutoFetchProfile(self, INI_PROFILE_URL, PY_PROFILE_URL)

def onAirportAircraftEngaged(self):
  gate = getGate()
  if gate and "SafeDock" in gate.parkingSystem:
    setJapaneseGenericVDGSMessage(self)

def onAirportBeforeVehicleSelect(self):
  gate = getGate()
  if gate:
    if not DISABLE_AUTO_OPR_SELECTION:
      operator_correlator.checkIfNeedAirlineOperatorCorrelation(self, aircraft.icaoAirline, FALLBACK_AIRLINE_OPERATOR_CORRELATION, AIR_OPR_CORRELATION_URL)
    if not DISABLE_AUTO_MOTOTOK_RESTRICTION:
      mototok_handler.modifyIfMototokCantBeUsedAtRJOO(self, aircraft.icaoAirline, aircraft.icaoType)
      mototok_handler.stopMototokEarlyConnect(self)

def onVehicleCandidatesScored(self, vehicleType, candidates):
  gate = getGate()
  if vehicleType == "Pushback" and gate and gate.pushbackType == 3:
    mototok_handler.selectMototokForANAJALRJOO(self, candidates, aircraft.icaoAirline, aircraft.icaoType)
  if "BaggageLoader" in vehicleType:
    model_disabler.disableCCL35S(self, candidates)
  if "PassengerBus" in vehicleType:
    model_disabler.disableNeoplan(self, candidates)