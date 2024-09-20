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
def customOffset_Spot4(aircraftData):
    # Product of GSJP
    first = 0.
    second = -2.85
    third = -6.9
    fourth = -9.2

    mainTable = {
        0: 0.,
        767: third,
        350: first,
        320: third,
        321: third,
        737: third,
        # ERJ
        195: third, 
        190: third,
        175: third, 
        170: third, 
        #CRJ900
        900: fourth,
        #Q400
        1008: fourth,
        #ATR
        42: fourth,
        72: fourth,
        #A220
        221: fourth,
        223: fourth,
    }

    table777 = {
        200: second,
        300: first,
    }

    table787 = {
        8: second,
        9: second,
        10: first,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    # Product of GSJP
    first = 0.
    second = -8.62

    mainTable = {
        0: 0.,
        767: second,
        350: first,
        320: second,
        321: second,
        737: second,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        #CRJ900
        900: second,
        #Q400
        1008: second,
        #ATR
        42: second,
        72: second,
    }

    table777 = {
        200: first,
        300: first,
    }

    table787 = {
        8: first,
        9: first,
        10: first,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot8(aircraftData):
    # Product of GSJP
    first = -2.14
    second = -5.26

    mainTable = {
        0: 0.,
        320: first,
        321: first,
        737: first,
        # ERJ
        195: first, 
        190: first,
        175: first, 
        170: first, 
        #CRJ900
        900: second,
        #Q400
        1008: second,
        #ATR
        42: second,
        72: second,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("Apron Gates (2-7)|SPOT #§ [INTL]"), customOffset_noOffset),
        3 : (CustomizedName("Apron Gates (2-7)|SPOT #§ [INTL]"), customOffset_Spot4),
        4 : (CustomizedName("Apron Gates (2-7)|SPOT #§ [INTL/DOM]"), customOffset_Spot4),
        5 : (CustomizedName("Apron Gates (2-7)|SPOT #§ [Domestic]"), customOffset_Spot4),
        6 : (CustomizedName("Apron Gates (2-7)|SPOT #§ [Domestic]"), customOffset_Spot6),
        7 : (CustomizedName("Apron Gates (2-7)|SPOT #§ [Domestic]"), customOffset_noOffset),
    }, 

    PARKING : {
        None : (CustomizedName("{MIL} JSDF-G Apron|#§"),),
        1 : (CustomizedName("Apron Stands (1, 11-14)|SPOT #§"), customOffset_noOffset),
        8 : (CustomizedName("Apron Pier Bldg (8-10)|SPOT #§ [Domestic]"), customOffset_Spot8),
        9 : (CustomizedName("Apron Pier Bldg (8-10)|SPOT #§ [Domestic]"), customOffset_Spot8),
        10 : (CustomizedName("Apron Pier Bldg (8-10)|SPOT #§ [Domestic]"), customOffset_Spot8),
        11 : (CustomizedName("Apron Stands (1, 11-14)|SPOT #§ [TOK/IBEX]"), customOffset_noOffset),
        12 : (CustomizedName("Apron Stands (1, 11-14)|SPOT #§ [TOK/IBEX]"), customOffset_noOffset),
        13 : (CustomizedName("Apron Stands (1, 11-14)|SPOT #§ [TOK/IBEX]"), customOffset_noOffset),
        14 : (CustomizedName("Apron Stands (1, 11-14)|SPOT #§ [TOK/IBEX]"), customOffset_noOffset),

        42 : (CustomizedName("JCG Apron|C"), ),
        43 : (CustomizedName("JCG Apron|D"), ),
        88 : (CustomizedName("JCG Apron|#§"), ),
        89 : (CustomizedName("JCG Apron|B"), ),
        90 : (CustomizedName("JCG Apron|A"), ),
        99 : (CustomizedName("JCG Apron|#§"), ),
        100 : (CustomizedName("JCG Apron|#§"), ),
        101 : (CustomizedName("JCG Apron|#§"), ),
        102 : (CustomizedName("JCG Apron|#§"), ),
    }, 

    S_PARKING : {
        None : (), 
        1 : (CustomizedName("Run Up Area|#§"), ),
        2 : (CustomizedName("Run Up Area|#§"), ),
        3 : (CustomizedName("Run Up Area|#§"), ),
        4 : (CustomizedName("Run Up Area|#§"), ),

        20 : (CustomizedName("South 1 Apron|#§"), ),
        21 : (CustomizedName("South 1 Apron|#§"), ),
        22 : (CustomizedName("South 1 Apron|#§"), ),
        23 : (CustomizedName("South 1 Apron|#§"), ),
        24 : (CustomizedName("South 1 Apron|#§"), ),
        25 : (CustomizedName("South 1 Apron|#§"), ),
        26 : (CustomizedName("South 1 Apron|#§"), ),
        27 : (CustomizedName("South 1 Apron|#§"), ),
        28 : (CustomizedName("South 1 Apron|#§"), ),
        29 : (CustomizedName("South 1 Apron|#§"), ),

        30 : (CustomizedName("South 2 Apron|#§"), ),
        31 : (CustomizedName("South 2 Apron|#§"), ),
        32 : (CustomizedName("South 2 Apron|#§"), ),
        33 : (CustomizedName("South 2 Apron|#§"), ),
        34 : (CustomizedName("South 2 Apron|#§"), ),
        35 : (CustomizedName("South 2 Apron|#§"), ),
        36 : (CustomizedName("South 2 Apron|#§"), ),
        37 : (CustomizedName("South 2 Apron|#§"), ),
        38 : (CustomizedName("South 2 Apron|#§"), ),
        39 : (CustomizedName("South 2 Apron|#§"), ),
        40 : (CustomizedName("South 2 Apron|#§"), ),

        41 : (CustomizedName("South 3 Apron|#§"), ),
        42 : (CustomizedName("South 3 Apron|#§"), ),
        43 : (CustomizedName("South 3 Apron|#§"), ),
        44 : (CustomizedName("South 3 Apron|#§"), ),
        45 : (CustomizedName("South 3 Apron|#§"), ),
        46 : (CustomizedName("South 3 Apron|#§"), ),
        47 : (CustomizedName("South 3 Apron|#§"), ),
        48 : (CustomizedName("South 3 Apron|#§"), ),
        49 : (CustomizedName("South 3 Apron|#§"), ),
        50 : (CustomizedName("South 3 Apron|#§"), ),
        51 : (CustomizedName("South 3 Apron|#§"), ),
    }, 

    GATE_A : {
        None : (), 
        0 : (CustomizedName("CAC Apron|A"), ),
    }, 

    GATE_B : {
        None : (), 
        0 : (CustomizedName("CAC Apron|B"), ),
    }, 

    GATE_C : {
        None : (), 
        0 : (CustomizedName("CAC Apron|C"), ),
    }, 

    GATE_D : {
        None : (), 
        0 : (CustomizedName("CAC Apron|D"), ),
    }, 

    GATE_E : {
        None : (), 
        0 : (CustomizedName("CAC Apron|E"), ),
    }, 

    GATE_F : {
        None : (), 
        0 : (CustomizedName("CAC Apron|F"), ),
    }, 

}