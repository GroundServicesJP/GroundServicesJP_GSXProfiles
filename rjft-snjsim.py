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
version = 1.1

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    #T_loc = 0.
    T_loc = 0.-11.
    # first = -2.87
    first = -2.87-11.
    second = -18.56

    mainTable = {
        0: first,
        767: first,
        320: second,
        321: second,
        737: second,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        # Q400
        1008: second,
    }

    table777 = {
        200: first,
        300: T_loc,
    }

    table787 = {
        8: first,
        9: first,
        10: T_loc,
    }

    table350 = {
        900: first, 
        1000: T_loc,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    #T_loc = 0.
    T_loc = 0.-13.
    # first = -2.87
    first = -2.87-13.
    second = -18.56

    mainTable = {
        0: first,
        767: first,
        320: second,
        321: second,
        737: second,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        # Q400
        1008: second,
    }

    table777 = {
        200: first,
        300: T_loc,
    }

    table787 = {
        8: first,
        9: first,
        10: T_loc,
    }

    table350 = {
        900: first, 
        1000: T_loc,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

parkings = {
    GATE : {
        None : (),
        1 : (CustomizedName("Apron|SPOT #§ [Domestic]"), customOffset_noOffset),
        2 : (CustomizedName("Apron|SPOT #§ [Domestic]"), customOffset_Spot3),
        3 : (CustomizedName("Apron|SPOT #§ [Domestic]"), customOffset_Spot3),
        4 : (CustomizedName("Apron|SPOT #§ [Domestic]"), customOffset_Spot3),
        5 : (CustomizedName("Apron|SPOT #§ [DOM/INTL]"), customOffset_Spot5),
        6 : (CustomizedName("Apron|SPOT #§ [INTL]"), customOffset_noOffset),
        7 : (CustomizedName("Apron|SPOT #§ [INTL]"), customOffset_noOffset),
    }, 

    GATE_A : {
        None : (CustomizedName("Apron (General Aviation)|SPOT A"), ),
    },

    GATE_B : {
        None : (CustomizedName("Apron (General Aviation)|SPOT B"), ),
    },

    GATE_C : {
        None : (CustomizedName("{MIL} JSDF-G Apron|#§"), ),
        0 : (CustomizedName("Apron (General Aviation)|SPOT C"), ),
    },

    GATE_D : {
        None : (CustomizedName("Apron (General Aviation)|SPOT D"), ),
    },
    

    N_PARKING : {
        None : (CustomizedName("GA Apron (Papa Apron)|#§"), ),
    }, 
    
    GATE_H : {
        None : (CustomizedName("Kumamoto Pref. Apron|#§"), ),
    },

    PARKING : {
        None : (CustomizedName("Sojo Univ. Apron|#§"), ),
    }, 

    S_PARKING : {
        None : (CustomizedName("{MIL} JSDF-G Apron|#§"), ),
    },

    GATE_M : {
        None : (CustomizedName("{MIL} JSDF-G Apron|#§"), ),
    },
}