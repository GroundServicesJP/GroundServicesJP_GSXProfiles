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
version = 1.2

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -3.61

    mainTable = {
        0: T_loc,
        319: first,
        320: first,
        321: T_loc,
        737: T_loc,
        # ERJ
        195: first, 
        190: first,
        175: first, 
        170: first, 
        # Q400
        1008: first,
        #CRJ900
        900: first,
        #Q400
        1008: first,
        #ATR
        42: first,
        72: first,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0.))

@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -1.55
    second = -3.63
    third = -5.22

    mainTable = {
        0: T_loc,
        767: first,
        319: third,
        320: third,
        321: third,
        737: second,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        # Q400
        1008: second,
        #CRJ700
        700: second,
        #Q400
        1008: second,
        #ATR
        42: third,
        72: third,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0.))


@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -3.65

    mainTable = {
        0: T_loc,
        319: first,
        320: first,
        321: T_loc,
        737: T_loc,
        # ERJ
        195: first, 
        190: first,
        175: first, 
        170: first, 
        # Q400
        1008: first,
        #CRJ900
        900: first,
        #Q400
        1008: first,
        #ATR
        42: first,
        72: first,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0.))


@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -3.78

    mainTable = {
        0: T_loc,
        319: first,
        320: first,
        321: T_loc,
        737: T_loc,
        # ERJ
        195: first, 
        190: first,
        175: first, 
        170: first, 
        # Q400
        1008: first,
        #CRJ900
        900: first,
        #Q400
        1008: first,
        #ATR
        42: first,
        72: first,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0.))

parkings = {
    GATE :{
        None : (),
        1 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot1),
        2 : (CustomizedName("Apron Gate|SPOT #§ [ANA]"), customOffset_Spot2),
        3 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot3),
        5 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot5),
    },
}
