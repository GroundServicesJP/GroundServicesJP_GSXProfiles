# -- coding: utf-8 --

# Copyright (C) 2025 GroundServicesJP (FUK_Driver, ANA7875)
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

# @AlternativeStopPositions
# def customOffset_Spot2(aircraftData):
#     # Product of GSJP
#     mainTable = {
#         0: 0.,
#         767: -1.75,
#         320: -1.75,
#         321: -1.75,
#         737: -1.75,
#         # ERJ
#         195: -1.75, 
#         190: -1.75,
#         175: -1.75, 
#         170: -1.75, 
#     }

#     table777 = {
#         200: -1.75,
#         300: 0.,
#     }

#     table787 = {
#         8: -1.75,
#         9: -1.75,
#         10: 0.,
#     }

#     table350 = {
#         900: -1.75, 
#         1000: 0.
#     }

#     if aircraftData.idMajor == 777:
#         return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
#     elif aircraftData.idMajor == 787:
#         return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
#     elif aircraftData.idMajor == 350:
#         return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
#     return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    first = -2.87
    # second = -18.49
    second = -2.87

    mainTable = {
        0: 0.,
        767: first,
        320: second,
        321: second,
        737: second,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        1008: second,
    }

    table777 = {
        200: first,
        300: 0.,
    }

    table787 = {
        8: first,
        9: first,
        10: 0.,
    }

    table350 = {
        900: first, 
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
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    T_loc = -4.33
    # first = T_loc-1.75
    first = T_loc
    # second = first-2.
    second = first

    mainTable = {
        0: -2.87,
        767: -2.87,
        320: -2.87,
        321: -2.87,
        737: -2.87,
        # ERJ
        195: -2.87, 
        190: -2.87,
        175: -2.87, 
        170: -2.87, 
        # Q400
        1008: -2.87,
    }

    table777 = {
        200: -2.87,
        300: -2.87,
    }

    table787 = {
        8: -2.87,
        9: -2.87,
        10: -2.87,
    }

    table350 = {
        900: -2.87, 
        1000: -2.87,
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
        1 : (CustomizedName("Apron (Terminal)|SPOT #§ [Domestic]"), customOffset_noOffset),
        2 : (CustomizedName("Apron (Terminal)|SPOT #§ [Domestic]"), customOffset_noOffset),
        3 : (CustomizedName("Apron (Terminal)|SPOT #§ [Domestic]"), customOffset_Spot3),
        4 : (CustomizedName("Apron (Terminal)|SPOT #§ [Domestic]"), customOffset_noOffset),
        5 : (CustomizedName("Apron (Terminal)|SPOT #§ [DOM/INTL]"), customOffset_Spot5),
        6 : (CustomizedName("Apron (Terminal)|SPOT #§ [INTL]"), customOffset_Spot3),
    }, 

    PARKING : {
        7 : (CustomizedName("Apron (Terminal)|SPOT #§ [INTL]"), customOffset_Spot3),
    }, 

    0 : {
        None : (CustomizedName("{MIL} JSDF-G Apron|#§"), ),
        206 : (CustomizedName("Sojo Univ. Apron (North)|#§"), ),
        207 : (CustomizedName("Sojo Univ. Apron (North)|#§"), ),
        301 : (CustomizedName("Sojo Univ. Apron (South)|#§"), ),
        401 : (CustomizedName("GA Apron (Papa Apron)|#§"), ),
        501 : (CustomizedName("Kumamoto Pref. Apron|#§"), ),
    },
}