# -- coding: utf-8 --

# Copyright (C) 2025 GroundServicesJP
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

msfs_mode = 1
version = 1.0

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot8085(aircraftData):
    return Distance.fromMeters(-9.)

@AlternativeStopPositions
def customOffset_Spot9091(aircraftData):
    return Distance.fromMeters(-9.)

@AlternativeStopPositions
def customOffset_Spot0(aircraftData):
    # Product of GSJP
    if aircraftData.idMajor in {767, 737}:
        return Distance.fromMeters(8.21) # Adjusted
    elif aircraftData.idMajor in {318, 319, 320, 321}:
        return Distance.fromMeters(4.) # Adjusted for PBB
    else: 
        # 1008
        return Distance.fromMeters(4.) # Adjusted for PBB
    
@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    # Product of GSJP
    if aircraftData.idMajor in {767, 200, 700, 900, 1000}:
        return Distance.fromMeters(-1.9)
    elif aircraftData.idMajor in {318, 319, 320, 321}:
        return Distance.fromMeters(-4.2)
    else: 
        # D84 (PBB) B3
        return Distance.fromMeters(0.)
    
@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    # Product of GSJP
    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(1.5)
    elif aircraftData.idMajor in {737}:
        return Distance.fromMeters(-2.3)
    elif aircraftData.idMajor in {318, 319, 320, 321, 1008, 200, 700, 900, 1000}:
        return Distance.fromMeters(-2.3)
        # return Distance.fromMeters(-3.3)
    else: 
        # B6 B72
        return Distance.fromMeters(0.)
    
@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    stop_1 = -1.96 # -3.7
    stop_2 = -4.7-5. # PBB Adjustment
    stop_3 = -5.7-5. # PBB Adjustment

    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor in {737, 767}:
        return Distance.fromMeters(stop_2)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        # A2
        return Distance.fromMeters(stop_3)
    else: 
        return Distance.fromMeters(stop_1)
    
@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    stop_1 = -2.57
    stop_2 = -3.57
    stop_3 = -4.57

    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor in {737, 767}:
        return Distance.fromMeters(stop_2)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        # A2
        return Distance.fromMeters(stop_3)
    else: 
        return Distance.fromMeters(stop_1)
    
@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    # Product of GSJP
    stop_1 = -3.68

    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor in {737, 767}:
        return Distance.fromMeters(stop_1)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        # A2
        return Distance.fromMeters(stop_1)
    else: 
        return Distance.fromMeters(0.)
    
@AlternativeStopPositions
def customOffset_Spot7(aircraftData):
    # Product of GSJP
    stop_1 = -2.39

    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(0.)
    elif (aircraftData.idMajor in {737, 767, 787}) or (aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}):
        return Distance.fromMeters(stop_1)
    else: 
        return Distance.fromMeters(0.)
    
@AlternativeStopPositions
def customOffset_Spot8(aircraftData):
    # Product of GSJP
    stop_1 = -1.52
    stop_2 = -3.04

    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(0.)
    elif (aircraftData.idMajor in {767, 777}) or (aircraftData.icaoTypeDesignator in {"B789"}):
        # B6 B72 B89
        return Distance.fromMeters(stop_1)
    elif (aircraftData.idMajor in {787}) or (aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}):
        # B3 B88 A2
        return Distance.fromMeters(stop_2)
    else: 
        return Distance.fromMeters(0.)
    
@AlternativeStopPositions
def customOffset_Spot9(aircraftData):
    # Product of GSJP
    stop_1 = -2.9

    # if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
    #     return Distance.fromMeters(0.)
    # else: 
    #     return Distance.fromMeters(stop_1)
    
    if aircraftData.aircraftGroup in {"ARC-D", "ARC-E", "ARC-F"}: 
        return Distance.fromMeters(0.)
    else: 
        return Distance.fromMeters(stop_1)
    
@AlternativeStopPositions
def customOffset_Spot10(aircraftData):
    # Product of GSJP
    stop_1 = -1.79
    stop_2 = -11. # guess

    if aircraftData.idMajor in {350, 747, 380}:
        return Distance.fromMeters(0.)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}: 
        return Distance.fromMeters(stop_2)
    else: 
        return Distance.fromMeters(stop_1)
    
@AlternativeStopPositions
def customOffset_Spot11(aircraftData):
    # Product of GSJP
    stop_1 = -2.
    stop_2 = -9.3

    if aircraftData.idMajor in {350, 747, 380}:
        return Distance.fromMeters(0.)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}: 
        return Distance.fromMeters(stop_2)
    else: 
        return Distance.fromMeters(stop_1)
    
@AlternativeStopPositions
def customOffset_Spot12(aircraftData):
    # Product of GSJP
    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}): 
        return Distance.fromMeters(2.28)
    elif aircraftData.aircraftGroup in {"ARC-D", "ARC-E", "ARC-F"}: 
        return Distance.fromMeters(1.65)
    else:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot14(aircraftData):
    # Product of GSJP
    if aircraftData.idMajor in {170, 175, 190, 195}: 
        return Distance.fromMeters(-2.08)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}: 
        return Distance.fromMeters(-1.15)
    elif aircraftData.aircraftGroup in {"ARC-D", "ARC-E", "ARC-F"}: 
        return Distance.fromMeters(-1.7), Distance.fromMeters(-6.73)
    else:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot15(aircraftData):
    # Product of GSJP
    if aircraftData.idMajor in {767}:
        return Distance.fromMeters(-1.8)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}: 
        return Distance.fromMeters(-4.58), Distance.fromMeters(-4.13)
    else:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot16(aircraftData):
    # Product of GSJP
    if (aircraftData.idMajor in {350, 747, 380}) or (aircraftData.icaoTypeDesignator in {"B77W", "B773", "B78X", "A346"}):
        return Distance.fromMeters(0.)
    else: 
        return Distance.fromMeters(-2.29)
    
@AlternativeStopPositions
def customOffset_Spot17(aircraftData):
    # Product of GSJP
    # Pseudo based on reality
    special_ac_set = {195, 190, 175, 170, 737}
    if (aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}) and (aircraftData.idMajor not in special_ac_set):
        return Distance.fromMeters(-1.74)
    else: 
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot20(aircraftData):
    # Product of GSJP
    if aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        return Distance.fromMeters(-16.)
    else:
        return Distance.fromMeters(0.)
    
@AlternativeStopPositions
def customOffset_Spot21(aircraftData):
    # Product of GSJP
    common_regional = {42, 72, 1008, 200, 700, 900, 1000, 195, 190, 175, 170, 221, 223}
    if (aircraftData.idMajor in common_regional) or (aircraftData.aircraftGroup in {"ARC-A", "ARC-B"}):
        return Distance.fromMeters(-16.)
    else:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot62(aircraftData):
    # Product of GSJP
    stop_t = 0.
    stop_1 = -1.23
    stop_2 = -16.28
    stop_3 = -20.54

    if aircraftData.idMajor in {737, 321, 320, 319, 318, 190, 195, 221, 223}:
        return Distance.fromMeters(stop_t)
    elif aircraftData.idMajor == 1008:
        return Distance.fromMeters(stop_2)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        return Distance.fromMeters(stop_3)
    else:
        return Distance.fromMeters(stop_t)
    
@AlternativeStopPositions
def customOffset_Spot61(aircraftData):
    # Product of GSJP
    stop_t = 0.
    stop_p1 = 2.28
    stop_p2 = 6.68
    top_1 = -1.23
    stop_2 = -16.28
    stop_3 = -20.54

    if aircraftData.icaoTypeDesignator in {"A332", "A338", "A342", "B788"} or aircraftData.idMajor in {767}:
        return Distance.fromMeters(stop_p1)
    elif aircraftData.aircraftGroup in {"ARC-D", "ARC-E", "ARC-F"}:
        return Distance.fromMeters(stop_p2)
    elif aircraftData.idMajor in {737, 321, 320, 319, 318, 190, 195, 221, 223}:
        return Distance.fromMeters(stop_t)
    elif aircraftData.idMajor == 1008:
        return Distance.fromMeters(stop_2)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        return Distance.fromMeters(stop_3)
    else:
        return Distance.fromMeters(stop_t)

@AlternativeStopPositions
def customOffset_Spot63(aircraftData):
    # Product of GSJP
    stop_t = 0.
    stop_1 = -8.
    stop_2 = -15.58
    stop_prop = (-18.86, -3.58)

    if aircraftData.idMajor in {737, 320, 319, 318, 170, 175, 190, 195, 221, 223}:
        return Distance.fromMeters(stop_2)
    elif aircraftData.idMajor == 321 or aircraftData.icaoTypeDesignator in {"B39M", "B3XM", "B739"}:
        return Distance.fromMeters(stop_1)
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        return Distance.fromMeters(stop_prop[0]), Distance.fromMeters(stop_prop[1])
    else:
        return Distance.fromMeters(stop_t)

@AlternativeStopPositions
def customOffset_SpotINTL(aircraftData):
    # Product of GSJP
    stop_t = 0.
    stop_1 = -2.81
    stop_2 = -4.21
    stop_3 = -7.01
    stop_4 = -8.91
    stop_5 = -10.98
    stop_6 = -18.08

    mainTable = {
        0: 0.,
        767: stop_4, # 48.51m-54.94m-61.37m, inf
    }

    table330 = {
        200: stop_4, # 58.82m, inf
        300: stop_4, # 63.66m
        800: stop_4, # 58.82m, inf
        900: stop_4, # 63.66m
    }

    table340 = {
        200: stop_4, # 59.4m, inf
        300: stop_4, # 63.69m, inf
        500: stop_2, # 67.93m, inf
        600: 0., # 75.36m
    }

    table350 = {
        900: stop_t, # 66.8m
        1000: stop_t, # 73.79m
    }

    table777 = {
        200: stop_3, # 63.73m
        300: stop_t, # 73.86m
    }

    table787 = {
        8: stop_4, # 56.72m
        9: stop_4, # 62.81m
        10: stop_2, # 68.28m
    }

    table747 = {
        100: stop_1, 
        200: stop_1, 
        300: stop_1,
        400: stop_1, 
        8: stop_t,
        800: stop_t,
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 747:
        return Distance.fromMeters(table747.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}:
        return Distance.fromMeters(stop_6)
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

parkings = {
    GATE :{
        None : (),
        0 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/AKX/APJ]"), customOffset_Spot0),
        1 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/AKX/APJ/IBEX]"), customOffset_Spot1),
        2 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/AKX/APJ/IBEX]"), customOffset_Spot2),
        3 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/AKX/APJ]"), customOffset_Spot3),
        5 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/APJ]"), customOffset_Spot5),
        6 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO]"), customOffset_Spot6),
        7 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO]"), customOffset_Spot7),
        8 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO]"), customOffset_Spot8),
        9 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO]"), customOffset_Spot9),
        10 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/JAL]"), customOffset_Spot10),
        11 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [ANA/ADO/JAL]"), customOffset_Spot11),
        12 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL]"), customOffset_Spot12),
        14 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL]"), customOffset_Spot14),
        15 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL/JJP/SJO]"), customOffset_Spot15),
        16 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL]"), customOffset_Spot16),
        17 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL/JJP/SJO/SKY/FDA]"), customOffset_Spot17),
        18 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL/JJP/SJO/SKY/FDA]"), customOffset_noOffset),
        19 : (CustomizedName("Domestic Terminal (0-19)|SPOT #§ [JAL/JJP/SJO/SKY/FDA]"), customOffset_noOffset),

        20 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot20),
        21 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot21),
        22 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot21),
        23 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot21),
        24 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot21),
        25 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot21),
        26 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_Spot21),
        27 : (CustomizedName("SPOTs 20-27 [JAL/JJP/SJO/SKY/FDA]|SPOT #§"), customOffset_noOffset),

        63 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_Spot63),
        64 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        65 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        66 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        67 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        68 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        69 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        70 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),
        71 : (CustomizedName("Intl Terminal (63-71)|SPOT #§"), customOffset_SpotINTL),

        80 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_Spot8085),
        81 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_Spot8085),
        82 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_Spot8085),
        83 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_Spot8085),
        84 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_Spot8085),
        85 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_Spot8085),
        86 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_noOffset),
        87 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§"), customOffset_noOffset),
        90 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§ [Yamato (SJO)]"), customOffset_Spot9091),
        91 : (CustomizedName("SPOTs 80s-90s [Cargo/Parking]|SPOT #§ [Yamato (SJO)]"), customOffset_Spot9091),
    },

    PARKING : {
        44 : (CustomizedName("SPOTs 44-49 (No GSX)|SPOT #§"), customOffset_noOffset),
        45 : (CustomizedName("SPOTs 44-49 (No GSX)|SPOT #§"), customOffset_noOffset),
        46 : (CustomizedName("SPOTs 44-49 (No GSX)|SPOT #§"), customOffset_noOffset),
        47 : (CustomizedName("SPOTs 44-49 (No GSX)|SPOT #§"), customOffset_noOffset),
        48 : (CustomizedName("SPOTs 44-49 (No GSX)|SPOT #§"), customOffset_noOffset),
        49 : (CustomizedName("SPOTs 44-49 (No GSX)|SPOT #§"), customOffset_noOffset),

        50 : (CustomizedName("SPOTs 50-54 [ASC JASDF] (No GSX)|SPOT #§"), customOffset_noOffset),
        51 : (CustomizedName("SPOTs 50-54 [ASC JASDF] (No GSX)|SPOT #§"), customOffset_noOffset),
        52 : (CustomizedName("SPOTs 50-54 [ASC JASDF] (No GSX)|SPOT #§"), customOffset_noOffset),
        53 : (CustomizedName("SPOTs 50-54 [ASC JASDF] (No GSX)|SPOT #§"), customOffset_noOffset),
        54 : (CustomizedName("SPOTs 50-54 [ASC JASDF] (No GSX)|SPOT #§"), customOffset_noOffset),
        55 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        56 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        57 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        58 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        59 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        60 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        61 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot61),
        62 : (CustomizedName("SPOTs 55-62 [ANA Series/INTL] (No GSX)|SPOT #§"), customOffset_Spot62),
    }, 

    N_PARKING : {
        42 : (CustomizedName("{JCG} M-SPOT|West"), ),
        43 : (CustomizedName("{JCG} M-SPOT|East"), ),
    }
}