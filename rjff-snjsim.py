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
def customOffset_Spot1(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -1.5,
        767: -7,
        320: -9., #nisemono
        321: -9., #nisemono
        737: -9., #nisemono
        # ERJ
        195: -9., #nisemono
        190: -9., #nisemono
        175: -9., #nisemono
        170: -9., #nisemono
    }

    table737 = {
        700: -9., #nisemono
        800: -9., #nisemono
    }

    table777 = {
        200: -7.,
        300: 0.,
    }

    table787 = {
        8: -7.,
        9: -7.,
        10: -4.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -3.5,
        320: -3.5,
        321: -3.5, #Real:0
        737: -3.5, #Real:0
        # ERJ
        195: -3.5,
        190: -3.5,
        175: -3.5,
        170: -3.5,
    }

    table737 = {
        700: -3.5, 
        800: -3.5, #Real:0
    }

    if aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -3.5,
        320: -3.5, #Real:-1.5
        321: -3.5, #Real:-1.5
        737: -3.5, #Real:-1.5
        # ERJ
        195: -3.5,
        190: -3.5,
        175: -3.5,
        170: -3.5,
    }

    table737 = {
        700: -3.5,
        800: -3.5, #Real:-1.5
    }

    if aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -4.5,
        350: -4.5, # Real:-1.5
        767: -7,
        320: -10.45,
        321: -10.45,
        737: -10.45,
        # ERJ
        195: -10.45,
        190: -10.45,
        175: -10.45,
        170: -10.45,
    }

    table737 = {
        700: -10.45, 
        800: -10.45,
    }

    table777 = {
        200: -7.,
        300: -4.5, # Real:0
    }

    table787 = {
        8: -7.,
        9: -7.,
        10: -4.5, # Real:-2.3
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot7(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -1.5,
        767: -8.47,
        320: -11.75,
        321: -11.75,
        737: -8.47,
        # ERJ
        195: -8.47,
        190: -8.47,
        175: -11.75,
        170: -11.75,
    }

    table737 = {
        700: -11.75, 
        800: -8.47,
    }

    table777 = {
        200: -7.,
        300: 0.,
    }

    table787 = {
        8: -7.,
        9: -7.,
        10: -4,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot9(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -3.,
        767: -9.45,
        320: -13.14,
        321: -13.14,
        737: -11.75,
        # ERJ
        195: -11.75,
        190: -11.75,
        175: -11.75,
        170: -11.75,
    }

    table737 = {
        700: -13.14, 
        800: -11.75,
    }

    table777 = {
        200: -4.44,
        300: 0.,
    }

    table787 = {
        8: -9.45,
        9: -7.,
        10: -5.71,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot10(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -1.5,
        767: -7.,
        320: -13.14,
        321: -13.14,
        737: -13.14,
        # ERJ
        195: -13.14,
        190: -13.14,
        175: -13.14,
        170: -13.14,
    }

    table737 = {
        700: -13.14, 
        800: -13.14,
    }

    table777 = {
        200: -5.5,
        300: 0.,
    }

    table787 = {
        8: -9.45,
        9: -9.45,
        10: -3.5,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot47(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -2.1,
        767: -7.1,
        320: -15.1, 
        321: -15.1, 
        737: -15.1, 
        # ERJ
        195: -15.1, 
        190: -15.1, 
        175: -15.1, 
        170: -15.1, 
        # A220
        221: -15.1, 
        223: -15.1, 
    }

    table330 = {
        200: -7.1,
        300: -5.1,
        800: -7.1,
        900: -5.1,
    }

    table350 = {
        900: -2.1,
        1000: 0., 
    }

    table737 = {
        700: -15.1, 
        800: -15.1, 
        900: -15.1, 
    }

    table777 = {
        200: -2.1,
        300: 0., 
    }

    table787 = {
        8: -7.1,
        9: -2.1,
        10: 0., 
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot53(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -2.1,
        767: -7.1,
        320: -15.1, 
        321: -15.1, 
        737: -15.1, 
        # ERJ
        195: -15.1, 
        190: -15.1, 
        175: -15.1, 
        170: -15.1, 
        # A220
        221: -15.1, 
        223: -15.1, 
    }

    table330 = {
        200: -7.1,
        300: -5.1,
        800: -7.1,
        900: -5.1,
    }

    table350 = {
        900: -2.1,
        1000: -2.1, #Real:0
    }

    table737 = {
        700: -15.1, 
        800: -15.1, 
        900: -15.1, 
    }

    table777 = {
        200: -2.1,
        300: -2.1, #Real:0
    }

    table787 = {
        8: -7.1,
        9: -2.1,
        10: -2.1, #Real:0
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737 and aircraftData.idMinor in table737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot59(aircraftData):
    myTable = {
        0: 0,
        320: -14.71,
        321: -14.71,
        737: -14.71,
        195: -14.71,
        190: -14.71,
        175: -14.71,
        170: -14.71,
        42: -14.71,
        72: -14.71,
        1008: -14.71,
        200: -14.71,
        700: -14.71,
        900: -14.71,
        1000: -14.71,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

parkings = {
    GATE : {
        None : (),
        1 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot1),
        2 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot2),
        3 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot3),
        4 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot3),
        5 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot3),
        6 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot6),
        7 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot7),
        8 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot7),
        9 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot9),
        10 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot10),
        11 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot6),
        12 : (CustomizedName("Domestic Terminal|SPOT #§"), customOffset_Spot6),

        13 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        14 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        15 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        16 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        17 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        18 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        19 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        20 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        21 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        22 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        23 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        24 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        25 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        26 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        27 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        28 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        29 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        30 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        31 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),
        32 : (CustomizedName("East Apron (13-32)|SPOT #§"), customOffset_noOffset),

        47 : (CustomizedName("West Apron (47-49)|SPOT #§"), customOffset_Spot47),
        48 : (CustomizedName("West Apron (47-49)|SPOT #§"), customOffset_Spot47),
        49 : (CustomizedName("West Apron (47-49)|SPOT #§"), customOffset_Spot47),
        50 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        51 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        52 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
    },
    0 : {
        None : (),
        53 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        54 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        55 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        56 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        57 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),
        58 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot53),

        59 : (CustomizedName("International Terminal|SPOT #§"), customOffset_Spot59),
    },
    GATE_L : {
        None : (),
        1 : (CustomizedName("West Apron (L Spots)|SPOT L#§"), customOffset_noOffset),
        2 : (CustomizedName("West Apron (L Spots)|SPOT L#§"), customOffset_noOffset),
        3 : (CustomizedName("West Apron (L Spots)|SPOT L#§"), customOffset_noOffset),
    },
    GATE_U : {
        None : (),
        1 : (CustomizedName("{MIL} USAF|#§"), ),
    },
    GATE_J : {
        None : (),
        1 : (CustomizedName("{MIL} JASDF|#§"), ),
        2 : (CustomizedName("{MIL} JASDF|#§"), ),
        3 : (CustomizedName("{MIL} JASDF|#§"), ),
        4 : (CustomizedName("{MIL} JASDF|#§"), ),
        5 : (CustomizedName("{MIL} JASDF|#§"), ),
        6 : (CustomizedName("{MIL} JASDF|#§"), ),
    }
}