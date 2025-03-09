# -- coding: utf-8 --

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

msfs_mode = 1

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot21(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0.,
        320: -11.75, 
        321: -11.75,
        737: -11.75,  
        # ERJ
        195: -11.75, 
        190: -11.75,   
        175: -11.75,
        170: -11.75,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot23(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -3.63,
        320: -11.4,
        321: -11.4,
        737: -11.4,
        # ERJ
        195: -11.4, 
        190: -11.4,
        175: -11.4, 
        170: -11.4, 
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -3.63,
        9: 0.,
        10: 0.,
    }

    table350 = {
        900: -3.63,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot24(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0.,
        320: -10.33, 
        321: -10.33, 
        737: -10.33, 
        # ERJ
        195: -10.33, 
        190: -10.33, 
        175: -10.33,  
        170: -10.33, 
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot25(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -2.88,
        320: -12.29,
        321: -12.29,
        737: -12.29,
        # ERJ
        195: -12.29,
        190: -12.29,
        175: -12.29,
        170: -12.29,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -2.88,
        9: 0.,
        10: 0.,
    }

    table350 = {
        900: -2.88,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot26(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -2.83,
        320: -12.24,
        321: -12.24,
        737: -12.24,
        # ERJ
        195: -12.24,
        190: -12.24,
        175: -12.24,
        170: -12.24,
    }

    table777 = {
        200: 0.,
        300: 0.+5.,
    }

    table787 = {
        8: -2.83,
        9: 0.,
        10: 0.,
    }

    table350 = {
        900: -2.83,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot27(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0.,
        320: -12.25, 
        321: -12.25, 
        737: -12.25, 
        # ERJ
        195: -12.25, 
        190: -12.25,    
        175: -12.25,  
        170: -12.25,  
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot32(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -2.88,
        320: -21.78,
        321: -21.78,
        737: -21.78,
        # ERJ
        195: -21.78,
        190: -21.78,
        175: -21.78,
        170: -21.78,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -2.88,
        9: 0.,
        10: 0.,
    }
    
    table350 = {
        900: -2.88,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot33(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -2.88,
        320: -22.52,
        321: -22.52,
        737: -22.52,
        # ERJ
        195: -22.52,
        190: -22.52,
        175: -22.52,
        170: -22.52,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -2.88,
        9: 0.,
        10: 0.,
    }

    table350 = {
        900: -2.88,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot35(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -2.88,
        320: -18.,
        321: -18.,
        737: -18.,
        # ERJ
        195: -18.,
        190: -18.,
        175: -18.,
        170: -18.,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -2.88,
        9: 0.,
        10: 0.,
    }

    table350 = {
        900: -2.88,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot36(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -2.88,
        320: -12.25,
        321: -12.25,
        737: -12.25,
        # ERJ
        195: -12.25,
        190: -12.25,
        175: -12.25,
        170: -12.25,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -2.88,
        9: 0.,
        10: 0.,
    }

    table350 = {
        900: -2.88,
        1000: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot42(aircraftData):
    second_loc = -6.8

    # Product of GSJP
    mainTable = {
        0: 0.,
        767: second_loc,
        319: second_loc, # 33.84m
        320: second_loc, # 37.57m
        321: second_loc, # 44.51m
        737: second_loc, # 31–43.8m
        190: second_loc, # 36.25m
        170: second_loc, # 29.90m
        175: second_loc, # 31.67m
        1008: second_loc, # 32.8m
        221: second_loc, # 35m
        223: second_loc, # 38.71m
    }

    table330 = {
        200: second_loc, # 58.82m
        300: 0., # 63.66m
        800: 0., # 58.82m
        900: 0., # 63.66m
    }

    table340 = {
        200: second_loc, # 59.4m
        300: 0., # 63.69m
        500: 0, # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0, # 73.79m
    }

    table777 = {
        200: 0., # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: second_loc, # 56.72m
        9: 0., # 62.81m
        10: 0., # 68.28m
    }

    table350 = {
        900: second_loc,
        1000: 0.,
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

# Product of GSJP
parkings = {
    GATE : {
        None : (),
        # JAL Gates
        21 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_Spot21),
        22 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_noOffset),
        23 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_Spot23),
        24 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_Spot24),
        25 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_Spot25),
        26 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_Spot26),
        27 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [JAL/JTA/JJP/SKY]"), customOffset_Spot27),

        # ANA Gates
        31 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot27),
        32 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot32),
        33 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot33),
        34 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot24),
        35 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot35),
        36 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot36),
        37 : (CustomizedName("Domestic Gate (21-27, 31-37)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_Spot36),
        
        # Mixed Gate
        41 : (CustomizedName("Domestic/Intl Gate (41)|SPOT #§ [ANA/APJ/SNA/SKY/INTL]"), customOffset_noOffset),

        # Intl Gates
        42 : (CustomizedName("International Gate (42-44)|SPOT #§ [INTL]"), customOffset_Spot42),
        43 : (CustomizedName("International Gate (42-44)|SPOT #§ [INTL]"), customOffset_noOffset),
        44 : (CustomizedName("International Gate (42-44)|SPOT #§ [INTL]"), customOffset_noOffset),

        # Apron NR4
        45: (CustomizedName("NR4 Apron (45-46)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_noOffset),
        46: (CustomizedName("NR4 Apron (45-46)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_noOffset),
    },

    0 : {
        None : (CustomizedName("{MIL} JASDF Naha|#§"), ), # Using this to catch all JASDF
        41 : (CustomizedName("{MIL} JASDF Naha|#§"), ),
    },

    PARKING : {
        # West Apron Helipads
        1 : (CustomizedName("West Apron Helipads|#§ [ANH/EAS/Okinawa Police]"), ),
        2 : (CustomizedName("West Apron Helipads|#§ [ANH/EAS/Okinawa Police]"), ),
        3 : (CustomizedName("West Apron Helipads|#§ [ANH/EAS/Okinawa Police]"), ),
        4 : (CustomizedName("West Apron Helipads|#§ [ANH/EAS/Okinawa Police]"), ),
        5 : (CustomizedName("West Apron Helipads|#§ [ANH/EAS/Okinawa Police]"), ),
        6 : (CustomizedName("West Apron Helipads|#§ [ANH/EAS/Okinawa Police]"), ),

        11 : (CustomizedName("NR1 Apron (11-16)|SPOT #§ [JAL/JTA/RAC/JAC/JJP/SKY]"), customOffset_noOffset),
        12 : (CustomizedName("NR1 Apron (11-16)|SPOT #§M [JAL/JTA/RAC/JAC/JJP/SKY]"), customOffset_noOffset),
        13 : (CustomizedName("NR1 Apron (11-16)|SPOT #§M [JAL/JTA/RAC/JAC/JJP/SKY]"), customOffset_noOffset),
        14 : (CustomizedName("NR1 Apron (11-16)|SPOT #§ [JAL/JTA/RAC/JAC/JJP/SKY]"), customOffset_noOffset),
        15 : (CustomizedName("NR1 Apron (11-16)|SPOT #§ [RAC/JAC]"), customOffset_noOffset),
        16 : (CustomizedName("NR1 Apron (11-16)|SPOT #§"), customOffset_noOffset),

        # Apron NR5
        51 : (CustomizedName("NR5 Apron (51-52, 57D)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_noOffset),
        52 : (CustomizedName("NR5 Apron (51-52, 57D)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_noOffset),
        57 : (CustomizedName("NR5 Apron (51-52, 57D)|SPOT #§ [ANA/APJ/SNA/SKY]"), customOffset_noOffset),

        # Apron NR6
        61 : (CustomizedName("NR6 Apron (61-66)|SPOT #§"), customOffset_noOffset),
        62 : (CustomizedName("NR6 Apron (61-66)|SPOT #§ [SJO (Yamato Transport)]"), customOffset_noOffset),
        63 : (CustomizedName("NR6 Apron (61-66)|SPOT #§"), customOffset_noOffset),
        64 : (CustomizedName("NR6 Apron (61-66)|SPOT #§"), customOffset_noOffset),
        65 : (CustomizedName("NR6 Apron (61-66)|SPOT #§"), customOffset_noOffset),
        66 : (CustomizedName("NR6 Apron (61-66)|SPOT #§"), customOffset_noOffset),

        # Apron NR7
        71 : (CustomizedName("NR7 Apron (71-74)|SPOT #§"), customOffset_noOffset),
        72 : (CustomizedName("NR7 Apron (71-74)|SPOT #§"), customOffset_noOffset),
        73 : (CustomizedName("NR7 Apron (71-74)|SPOT #§"), customOffset_noOffset),
        74 : (CustomizedName("NR7 Apron (71-74)|SPOT #§"), customOffset_noOffset),

        # Hangar
        #98 : (CustomizedName("West Apron (98-107)|SPOT #§ [MROJapan]"), customOffset_noOffset),
        #99 : (CustomizedName("West Apron (98-107)|SPOT #§ [MROJapan]"), customOffset_noOffset),
        100 : (CustomizedName("West Apron (98-107)|SPOT 100 [MROJapan]"), customOffset_noOffset),
        101 : (CustomizedName("West Apron (98-107)|SPOT 101 [JTA Maintenance]"), customOffset_noOffset),
        102 : (CustomizedName("West Apron (98-107)|SPOT 102 [JTA Maintenance]"), customOffset_noOffset),
        103 : (CustomizedName("West Apron (98-107)|SPOT 103 [JTA Maintenance]"), customOffset_noOffset),

        # JCG
        104 : (CustomizedName("West Apron (98-107)|SPOT 104 [JCG]"), ),
        105 : (CustomizedName("West Apron (98-107)|SPOT 105A [JCG]"), ),
        1005 : (CustomizedName("West Apron (98-107)|SPOT 105B [JCG]"), ),
        1813 : (CustomizedName("West Apron (98-107)|SPOT 105C [JCG]"), ),
        106 : (CustomizedName("West Apron (98-107)|SPOT #§ [JCG]"), ),

        #201 : (CustomizedName("Run Up Area|#§"), customOffset_noOffset),
        #202 : (CustomizedName("Run Up Area|#§"), customOffset_noOffset),

        # JASDF
        8 : (CustomizedName("{MIL} JASDF Naha|#§"), ),
        97 : (CustomizedName("{MIL} JASDF Naha|#§"), ),
        98 : (CustomizedName("{MIL} JASDF Naha|#§"), ),
    }, 

    GATE_L : {
        None : (CustomizedName("Light Aircraft Apron|SPOT L#§"), customOffset_noOffset),
    },

    GATE_T : {
        None : (CustomizedName("Typhoon Evacuation Apron|SPOT T#§"), customOffset_noOffset),
    },
}