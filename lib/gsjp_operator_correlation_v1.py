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

# Shared Library for GroundServicesJP Handlers
# Operator/Aircraft Correlation (Airline and Aircraft Type Checks for Vehicle Selection)
# version =  1.0

def fetchOperatorCorrelation(url):
  """Load airline_operator_correlation from a remote JSON URL using fetchJson().

  Converts the JSON structure back to the dict format:
  - Key: ICAO airline code (str)
  - Value: tuple of fields (Ground Handler, Catering Provider, ...)
    - A plain string stays a string.
    - A list of {code, display_name} objects becomes a tuple of
      (code, display_name) tuples representing a choice.

  Returns the parsed dict, or None if the fetch failed.
  """
  raw = fetchJson(url, timeout=10, etag=True)
  if not raw:
    return None
  
  def convert_field(field):
    if isinstance(field, str):
      return field
    # list of {code, display_name} dicts -> tuple of (code, display_name)
    return tuple((item['code'], item['display_name']) for item in field)

  result = {}
  for airline, fields in raw.items():
    result[airline] = tuple(convert_field(f) for f in fields)
  return result

def getOperatorInfoFromCorrelation(icao_airline, correlation_matrix, correlation_url):
  # Try to fetch correlation matrix from remote URL, fallback to hardcoded dict if fetch fails
  correlation = fetchOperatorCorrelation(correlation_url)
  if correlation is None:
    print("[GSJP Auto-OPR] Failed to fetch remote correlation matrix, using fallback.")
    correlation = correlation_matrix
  else:
    print("[GSJP Auto-OPR] Successfully fetched remote correlation matrix.")

  operator_info = correlation.get(icao_airline)
  return operator_info

def showOperatorSelectionMenu(self, display_names, title):
  # Show a menu to let user select from multiple operators for the same airline
  choice = showChoiceMenu(title, display_names, timeout=30)
  return choice

def setOperatorFromOperatorInfo(self, operator_info):
  # If operator_info is a tuple of strings, set directly. If it's a tuple with choices, show menu.
  loc_to_menu_title = {
    0: "グラハンを選択してください。Select a Ground Handling Operator.",
    1: "ケータリングを選択してください。Select a Catering Operator.",
  }
  loc = 0
  for field in operator_info:
    if isinstance(field, str):
      # Direct mapping
      setOperatorVariable(loc, field)
    else:
      # Multiple choices available, show menu
      display_names = [f"{display_name}" for code, display_name in field]
      choice_codes = [f"{code}" for code, display_name in field]
      title = loc_to_menu_title.get(loc, "オペレーターを選択してください。Select an Operator.")
      selection_choice = showOperatorSelectionMenu(self, display_names, title)
      chosen_operator_code = choice_codes[selection_choice]
      # if choice is -1, this will be filtered in set function - fallback to profile default
      setOperatorVariable(loc, chosen_operator_code)
    loc += 1

def setOperatorVariable(loc, code_str):
  # Set the operator variable based on type (Ground Handler, Catering, etc.)
  # If code_str is None, do not set (use default profile setting)
  gate = getGate()
  if loc == 0 and code_str != None:
    gate.handlingTexture = code_str
    print(f"[GSJP Auto-OPR] Set Ground Handling Operator to {code_str}.")
  elif loc == 1 and code_str != None:
    gate.cateringTexture = code_str
    print(f"[GSJP Auto-OPR] Set Catering Operator to {code_str}.")
  # Add more operator types as needed

def checkIfNeedAirlineOperatorCorrelation(self, aircraft_icao_airline, correlation_matrix, correlation_url):
  # Setup a menu to check if user wants to fetch correlation using menu
  auto_opr_select_choice = showChoiceMenu("オペレーターを自動選択しますか? Would you like automatic operator selection? ", 
                          ["Yes (Default)", "No"], 
                          timeout=30)
  if auto_opr_select_choice == 1:
    print("[GSJP Auto-OPR] User opted out of automatic operator selection. Airline-operator correlation will not be applied.")
  else:
    print(f"[GSJP Auto-OPR] User opted in for automatic operator selection. Attempting to fetch correlation matrix for {aircraft_icao_airline}.")
    operator_info = getOperatorInfoFromCorrelation(aircraft_icao_airline, correlation_matrix, correlation_url)
    if operator_info:
      setOperatorFromOperatorInfo(self, operator_info)
    else:
      print(f"[GSJP Auto-OPR] No operator info found for {aircraft_icao_airline}. Airline-operator correlation will not be applied.")
