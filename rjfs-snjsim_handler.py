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

# Airport handler script for RJFS (profile: rjfs-snjsim)
# Applies to all aircraft at RJFS
# Version 0.91 Beta

# Top Level Defines
PROFILE_STEM = "rjfs-snjsim"
BRANCH_STEM = "main"
AIR_OPR_CORRELATION_URL = f"https://raw.githubusercontent.com/GroundServicesJP/GroundServicesJP_GSXProfiles/{BRANCH_STEM}/airline_operator_corr_dicts/{PROFILE_STEM}_corr_dict.json"

# Debug Flags
DISABLE_AUTO_FETCH_PROFILE = False # Set to True to disable automatic fetching of profile updates from GitHub, and always use local files
DISABLE_AUTO_OPR_SELECTION = False # Set to True to disable automatic operator selection based on airline ICAO code, and always use profile defaults
DISABLE_AUTO_MOTOTOK_RESTRICTION = False # Set to True to disable automatic restriction of Mototok usage based on aircraft weight and airline, and always allow Mototok at Mototok gates

# Shared library checks
def try_require(req_name):
  try:
    return require(req_name)
  except Exception as e:
    print(f"[GSJP] Failed to load library: {req_name}, Error: {e}")
    return None
mototok_handler = try_require("gsjp_mototok_handler_v1")
operator_correlator = try_require("gsjp_operator_correlation_v1")
model_disabler = try_require("gsjp_model_disabler_v1")

def checkRequirements():
  global mototok_handler, operator_correlator, auto_profile_fetcher, model_disabler
  
  all_libs_available = (mototok_handler is not None
                        and operator_correlator is not None
                        and model_disabler is not None)

  if not all_libs_available:
    message_1 = "必要なGSXライブラリがインストールされていません。\n" \
                "One or more required GSX Handler libraries are missing."
    message_2 = "以下のページをご覧ください。\nSee the following page on how to install:"
    message_3 = "https://gsjp.info/gsx-handlers"

    messageBox(f"{message_1}\n{message_2}\n{message_3}",
               caption="ERROR", style=MB_OK | MB_ICONERROR)

# Operator-Airline Correlation Matrix
# Fallback hardcoded dict in case the remote fetch fails
FALLBACK_AIRLINE_OPERATOR_CORRELATION = {
  "ANA": ("ANA", ""),
  "AKX": ("ANA", ""),
  "AJX": ("ANA", ""),
  "APJ": ("ANA", ""),
  "TTW": ("JL", ""),
  "TWB": ("ANA", ""),
  "CQH": ("JL", ""),
  "SJO": ("JL", "")
}

# Initialization tasks to need to be done on the first hook that gate data is available
def run_initialization_tasks(self):
  # Requires gate context
  gate = getGate()
  if gate is not None:
    if not DISABLE_AUTO_OPR_SELECTION and operator_correlator is not None:
      operator_correlator.checkIfNeedAirlineOperatorCorrelation(self, aircraft.icaoAirline, FALLBACK_AIRLINE_OPERATOR_CORRELATION, AIR_OPR_CORRELATION_URL)
    if not DISABLE_AUTO_MOTOTOK_RESTRICTION and mototok_handler is not None:
      mototok_handler.modifyIfMototokCantBeUsedAtRJFS(self, aircraft.icaoAirline, aircraft.icaoType)
      mototok_handler.stopMototokEarlyConnect(self)
    if not gate.hasJetway: 
      # Disable Rear Exit for non-jetway SPOT
      print("[GSJP] Disabling rear exit for SPOT without PBB.")
      disableExit(EXIT_PASSENGERS, 3)

################################ Inject in GSX Hooks ###############################
def onEnterAirport(self):
  checkRequirements()

def onAirportBeforeVehicleSelect(self):
  gate = getGate()
  if gate:
    run_initialization_tasks(self)

def onVehicleCandidatesScored(self, vehicleType, candidates):
  gate = getGate()
  if vehicleType == "Pushback" and gate and gate.pushbackType == 3:
    mototok_handler.selectMototokForANARJFS(self, candidates, aircraft.icaoAirline, aircraft.icaoType)
  if "BaggageLoader" in vehicleType:
    model_disabler.disableCCL35S(self, candidates)