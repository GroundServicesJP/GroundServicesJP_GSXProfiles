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
# Mototok Behavior Handler (Weight, Airline, Aircraft Type Checks + Mototok Model Selection for ANA at RJFS and ANA/JAL at RJOO)
# version =  1.0

# Maximum towing weight for the Spacer 8600 (largest Mototok)
MOTOTOK8600_MAX_WEIGHT_LBS = 210000
# Define the data request once at the top level for reuse
ddef_weight = SimDataDefinition()("TOTAL WEIGHT", "pounds")

def checkIfAircraftOfSpecificAirline(self, airline_icao_id_list, candidate_airline_icao):
  # Check GSX Selected ICAO Airline
  aircraft_icao_airline = candidate_airline_icao
  if aircraft_icao_airline:
    print("[GSJP Mototok] ICAO Airline is", aircraft_icao_airline)
    for airline_icao_id in airline_icao_id_list:
      if aircraft_icao_airline.casefold() == airline_icao_id.casefold():
        return True
      
  return False

def checkIfAircraftIsMototokSupportedType(self, icao_type_support, candidate_icao_type):
  # Check if the aircraft ICAO type is in the list of Mototok supported types for RJOO
  aircraft_icao_type = candidate_icao_type
  if aircraft_icao_type:
    print("[GSJP Mototok] ICAO Type is", aircraft_icao_type)
    for supported_type in icao_type_support:
      if aircraft_icao_type.casefold() == supported_type.casefold():
        return True
      
  return False

def checkIfAircraftIsANA(self, candidate_airline_icao, candidate_icao_type):
  # Check GSX Selected ICAO Airline
  airline_icao_id_list = ['ANA', 'AKX']
  aircraft_of_is_of_ANA = checkIfAircraftOfSpecificAirline(self, airline_icao_id_list, candidate_airline_icao)
  aircraft_is_mototok_supported_type = checkIfAircraftIsMototokSupportedType(self, ['B738', 'B38M', 'A320', 'A321', 'A20N', 'A21N'], candidate_icao_type)
  print(f"[GSJP Mototok] Is Aircraft of ANA? {aircraft_of_is_of_ANA}")
  print(f"[GSJP Mototok] Is Aircraft Type supported for Mototok for this airline? {aircraft_is_mototok_supported_type}")
  return aircraft_of_is_of_ANA and aircraft_is_mototok_supported_type

def checkIfAircraftIsJAL(self, candidate_airline_icao, candidate_icao_type):
  # Check GSX Selected ICAO Airline
  airline_icao_id_list = ['JAL', 'JLJ']
  aircraft_of_is_of_JAL = checkIfAircraftOfSpecificAirline(self, airline_icao_id_list, candidate_airline_icao)
  aircraft_is_mototok_supported_type = checkIfAircraftIsMototokSupportedType(self, ['B738', 'B38M', 'A320', 'A321', 'A20N', 'A21N', 'E170', 'E190'], candidate_icao_type)
  print(f"[GSJP Mototok] Is Aircraft of JAL? {aircraft_of_is_of_JAL}")
  print(f"[GSJP Mototok] Is Aircraft Type supported for Mototok for this airline? {aircraft_is_mototok_supported_type}")
  return aircraft_of_is_of_JAL and aircraft_is_mototok_supported_type

def checkIfAircraftIsCKTS(self):
  # Check if CKTS is the selected ground operator for the gate
  gate = getGate()
  if not gate:
    return False
  ground_handler = gate.handlingTexture
  print(f"[GSJP Mototok] Ground Handling Texture is {ground_handler}")
  return (ground_handler and ground_handler.casefold() == "ckts")

### !!!!
# The function exposed to onVehicleCandidateSelected() to check if the selected Mototok can be used, and if not, change to a regular tug (pushback type 1)
def modifyIfMototokCantBeUsedAtRJFS(self, candidate_airline_icao, candidate_icao_type):
  gate = getGate()
  if not gate or gate.pushbackType != 3:
    return # Not a Mototok gate, nothing to do
  
  # Read current aircraft weight and check
  ddef_weight_data = USER.requestData(ddef_weight)
  if not ddef_weight_data:
    # Fallback if I did not fetch current aircraft weight
    gate.pushbackType = 1
    return
  weight = ddef_weight_data[0]
  is_within_weight_limit = (weight <= MOTOTOK8600_MAX_WEIGHT_LBS)

  # Read current aircraft ICAO airline
  is_ANA = checkIfAircraftIsANA(self, candidate_airline_icao, candidate_icao_type)
  if (is_within_weight_limit) and is_ANA:
    print("[GSJP Mototok] Aircraft meets Mototok weight limit and is ANA's supported aircraft. Mototok can be used.")
    return # Within Mototok limit and is of ANA, all good

  # Give user last chance to pick Mototok if weight limit is OK
  if (is_within_weight_limit):
    operator_choice = showChoiceMenu(
      "Mototokの使用条件を満たしていないようです。Mototokを使用しますか? You do not meet the requirements to use the Mototok. Would you still like to request a Mototok?",
      ["Yes","No (Default)"],
      timeout=10
    )
    if operator_choice < 0: 
      # Default is no choice
      operator_choice = 1
    
    if operator_choice == 0:
      # If Choice is Zero (Yes), still spawn a Mototok
      print("[GSJP Mototok] Although the operator is not ANA, the user chose to use a Mototok since the aircraft weight is within the allowable limit.")
      return
  
  # Final fallback, change to pushback type 1
  print("[GSJP Mototok] Mototok not permitted. Aircraft exceeds Mototok 8600 weight limit or operator is not ANA.")
  print("[GSJP Mototok] Using a regular towbar tug instead.")
  gate.pushbackType = 1

def modifyIfMototokCantBeUsedAtRJOO(self, candidate_airline_icao, candidate_icao_type):
  gate = getGate()
  if not gate or gate.pushbackType != 3:
    return # Not a Mototok gate, nothing to do
  
  # Read current aircraft weight and check
  ddef_weight_data = USER.requestData(ddef_weight)
  if not ddef_weight_data:
    # Fallback if I did not fetch current aircraft weight
    gate.pushbackType = 1
    return
  weight = ddef_weight_data[0]
  is_within_weight_limit = (weight <= MOTOTOK8600_MAX_WEIGHT_LBS)

  # Read current aircraft ICAO airline
  is_ANA = checkIfAircraftIsANA(self, candidate_airline_icao, candidate_icao_type)
  is_JAL = checkIfAircraftIsJAL(self, candidate_airline_icao, candidate_icao_type)
  is_ANA_or_JAL = (is_ANA or is_JAL)
  if (is_within_weight_limit) and (is_ANA_or_JAL):
    print("[GSJP Mototok] Aircraft meets Mototok weight limit and is ANA or JAL's supported aircraft. Mototok can be used.")
    return # Within Mototok limit and is of ANA or JAL, all good

  # Give user last chance to pick Mototok if weight limit is OK
  if (is_within_weight_limit):
    operator_choice = showChoiceMenu(
      "Mototokの使用条件を満たしていないようです。Mototokを使用しますか? You do not meet the requirements to use the Mototok. Would you still like to request a Mototok?",
      ["Yes","No (Default)"],
      timeout=10
    )
    if operator_choice < 0: 
      # Default is no choice
      operator_choice = 1
    
    if operator_choice == 0:
      # If Choice is Zero (Yes), still spawn a Mototok
      print("[GSJP Mototok] Although the operator is not ANA or JAL, the user chose to use a Mototok since the aircraft weight is within the allowable limit.")
      return
  
  # Final fallback, change to pushback type 1
  print("[GSJP Mototok] Mototok not permitted. Aircraft exceeds Mototok 8600 weight limit or operator is not ANA/JAL.")
  print("[GSJP Mototok] Using a regular towbar tug instead.")
  gate.pushbackType = 1

### !!!!
# The function exposed to onVehicleCandidateSelected() to check if the selected Mototok can be used, and if not, change to a regular tug (pushback type 1)
def modifyIfMototokCantBeUsedAtRJFS(self, candidate_airline_icao, candidate_icao_type):
  gate = getGate()
  if not gate or gate.pushbackType != 3:
    return # Not a Mototok gate, nothing to do
  
  # Read current aircraft weight and check
  ddef_weight_data = USER.requestData(ddef_weight)
  if not ddef_weight_data:
    # Fallback if I did not fetch current aircraft weight
    gate.pushbackType = 1
    return
  weight = ddef_weight_data[0]
  is_within_weight_limit = (weight <= MOTOTOK8600_MAX_WEIGHT_LBS)

  # Read current aircraft ICAO airline
  is_ANA = checkIfAircraftIsANA(self, candidate_airline_icao, candidate_icao_type)
  if (is_within_weight_limit) and is_ANA:
    print("[GSJP Mototok] Aircraft meets Mototok weight limit and is ANA's supported aircraft. Mototok can be used.")
    return # Within Mototok limit and is of ANA, all good

  # Give user last chance to pick Mototok if weight limit is OK
  if (is_within_weight_limit):
    operator_choice = showChoiceMenu(
      "Mototokの使用条件を満たしていないようです。Mototokを使用しますか? You do not meet the requirements to use the Mototok. Would you still like to request a Mototok?",
      ["Yes","No (Default)"],
      timeout=10
    )
    if operator_choice < 0: 
      # Default is no choice
      operator_choice = 1
    
    if operator_choice == 0:
      # If Choice is Zero (Yes), still spawn a Mototok
      print("[GSJP Mototok] Although the operator is not ANA, the user chose to use a Mototok since the aircraft weight is within the allowable limit.")
      return
  
  # Final fallback, change to pushback type 1
  print("[GSJP Mototok] Mototok not permitted. Aircraft exceeds Mototok 8600 weight limit or operator is not ANA.")
  print("[GSJP Mototok] Using a regular towbar tug instead.")
  gate.pushbackType = 1

def selectRJBBGHOperator(self):
  handling_names_codess = [
    ("ANA KIX AP (Default)", "ANA"),
    ("JAL Ground Service", "JL"),
    ("Kansai Airports Aviation Services (CKTS)", "CKTS"),
    ("Korean Air Airport Service (KAAS)", "KAAS"),
    ("Contrail.aero", "CONTRAIL"),
    ("Flight Management Group (FMG)", "FMG"), 
    ("Swissport", "SWISSPORT"),
  ]
  gate = getGate()
  operator_options = [display_name for display_name, code in handling_names_codess]
  operator_choice = showChoiceMenu("グラハンを選択してください。Select a Ground Handling Operator.", operator_options, timeout=120)
  if operator_choice < 0:
    operator_choice = 0 # Default to first option if no choice made
  selected_operator_code = handling_names_codess[operator_choice][1]
  gate.handlingTexture = selected_operator_code
  print(f"[GSJP Mototok] Set Ground Handling Operator to {selected_operator_code} based on user selection.")

def modifyIfMototokCantBeUsedAtRJBB(self):
  gate = getGate()
  if not gate or gate.pushbackType != 3:
    return # Not a Mototok gate, nothing to do
  
  # Make sure select a handling operator first (if not CKTS, rule out)
  if gate.handlingTexture.casefold() != "ckts":
    selectRJBBGHOperator(self)
  
  # Read current aircraft weight and check
  ddef_weight_data = USER.requestData(ddef_weight)
  if not ddef_weight_data:
    # Fallback if I did not fetch current aircraft weight
    gate.pushbackType = 1
    return
  weight = ddef_weight_data[0]
  is_within_weight_limit = (weight <= MOTOTOK8600_MAX_WEIGHT_LBS)

  # Read current aircraft ICAO airline
  is_CKTS = checkIfAircraftIsCKTS(self)
  if (is_within_weight_limit) and is_CKTS:
    print("[GSJP Mototok] Aircraft meets Mototok weight limit and CKTS is the selected ground operator. Mototok can be used.")
    return # Within Mototok limit and is of CKTS, all good

  # Give user last chance to pick Mototok if weight limit is OK
  if (is_within_weight_limit):
    operator_choice = showChoiceMenu(
      "Mototokの使用条件を満たしていないようです。Mototok (CKTS)を使用しますか? You do not meet the requirements to use the Mototok. Would you still like to request a Mototok?",
      ["Yes","No (Default)"],
      timeout=10
    )
    if operator_choice < 0: 
      # Default is no choice
      operator_choice = 1
    
    if operator_choice == 0:
      # If Choice is Zero (Yes), still spawn a Mototok
      print("[GSJP Mototok] Although the operator is not CKTS, the user chose to use a Mototok since the aircraft weight is within the allowable limit.")
      return
  
  # Final fallback, change to pushback type 1
  print("[GSJP Mototok] Mototok not permitted. Aircraft exceeds Mototok 8600 weight limit or operator is not CKTS.")
  print("[GSJP Mototok] Using a regular towbar tug instead.")
  gate.pushbackType = 1

# !!!!
# The function exposed to onVehicleCandidateSelected() to disable the early tug (pushback on boarding) for Mototok gates since it can cause GPU overlap issues with the aircraft if the Mototok spawns too early while the aircraft is still loading in
# To be used after determining if Mototok is required. 
def stopMototokEarlyConnect(self):
  gate = getGate()
  if not gate or gate.pushbackType != 3:
    return # Not a Mototok gate, nothing to do
  settings = getSettings()
  if settings and settings.pushback_on_boarding == '1':
    settings.pushback_on_boarding = '0'
    print("[GSJP Mototok] Mototok gate detected — disabled early tug to avoid GPU overlap.")

######################## Random Mototok Selection Logic for ANA at RJFS ########################
def provideARandomMototok(mototok_candidates):
  return random.choice(mototok_candidates)

def provideARandomANAMototokRJFS():
  mototok_candidates = [
    "FSDT_PB_Mototok_8600_ANA_TL1001"
  ]

  return provideARandomMototok(mototok_candidates)

def provideARandomANAMototokRJOO():
  mototok_candidates = [
    "FSDT_PB_Mototok_8600_ANA_Monjyuro",
    "FSDT_PB_Mototok_8600_ANA_Moppi", 
    "FSDT_PB_Mototok_8600_ANA_Monika",
    "FSDT_PB_Mototok_8600_ANA_Mokomichi"
  ]

  return provideARandomMototok(mototok_candidates)

def provideARandomJALMototokRJOO():
  mototok_candidates = [
    "FSDT_PB_Mototok_8600NG_JAL_RJOO_1"
  ]

  return provideARandomMototok(mototok_candidates)

def provideARandomCKTSMototokRJBB():
  mototok_candidates = [
    "FSDT_PB_Mototok_8600NG_CKTS_RJBB_1"
  ]

  return provideARandomMototok(mototok_candidates)

### !!!!
# The function exposed to onVehicleCandidatesScored() to give a score boost to a random ANA Mototok at RJFS to match airline
def selectMototokForANARJFS(self, candidates, candidate_airline_icao, candidate_icao_type):
  # To be used in onVehicleCandidatesScored() only
  is_ANA = checkIfAircraftIsANA(self, candidate_airline_icao, candidate_icao_type)
  if is_ANA:
    # Get random ANA Mototok and give it a big score boost so it will be selected over the default Mototok
    random_ana_mototok = provideARandomANAMototokRJFS()
    for candidate in candidates:
      if candidate.title and candidate.title == random_ana_mototok:
        candidate.boostScore(100) # Give a big boost to the randomly selected ANA Mototok
        print(f"[GSJP Mototok] Boosting score for {candidate.title} since airline is ANA.")

### !!!!
# The function exposed to onVehicleCandidatesScored() to give a score boost to a random Mototok at RJOO to match airline
def selectMototokForANAJALRJOO(self, candidates, candidate_airline_icao, candidate_icao_type):
  # To be used in onVehicleCandidatesScored() only
  is_ANA = checkIfAircraftIsANA(self, candidate_airline_icao, candidate_icao_type)
  if is_ANA:
    # Get random ANA Mototok and give it a big score boost so it will be selected over the default Mototok
    random_ana_mototok = provideARandomANAMototokRJOO()
    for candidate in candidates:
      if candidate.title and candidate.title == random_ana_mototok:
        candidate.boostScore(100) # Give a big boost to the randomly selected ANA Mototok
        print(f"[GSJP Mototok] Boosting score for {candidate.title} since airline is ANA.")

  is_JAL = checkIfAircraftIsJAL(self, candidate_airline_icao, candidate_icao_type)
  if is_JAL:
    # Get random JAL Mototok and give it a big score boost so it will be selected over the default Mototok
    random_jal_mototok = provideARandomJALMototokRJOO()
    for candidate in candidates:
      if candidate.title and candidate.title == random_jal_mototok:
        candidate.boostScore(10) # Give a big boost to the randomly selected JAL Mototok
        print(f"[GSJP Mototok] Boosting score for {candidate.title} since airline is JAL.")

### !!!!
# The function exposed to onVehicleCandidatesScored() to give a score boost to a CKTS Mototok at RJBB to match ground handler
def selectMototokForCKTSRJBB(self, candidates):
  # Get random CKTS Mototok and give it a big score boost so it will be selected over the default Mototok
  random_ckts_mototok = provideARandomCKTSMototokRJBB()
  for candidate in candidates:
    if candidate.title and candidate.title == random_ckts_mototok:
      candidate.boostScore(100) # Give a big boost to the randomly selected CKTS Mototok
      print(f"[GSJP Mototok] Boosting score for {candidate.title}.")