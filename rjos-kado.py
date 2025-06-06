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

@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -1.92

    table = {
        0: T_loc,
        767: first,
        319: first,
        320: first,
        321: first,
        737: first,
        170: first,
        175: first,
        190: first,
    }
    
    return Distance.fromMeters(table.get(aircraftData.idMajor, 0.))

@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -2.24
    second = -6.94

    table = {
        0: T_loc,
        767: first,
        319: second,
        320: second,
        321: second,
        737: second,
        170: second,
        175: second,
        190: second,
    }
    
    return Distance.fromMeters(table.get(aircraftData.idMajor, 0.))

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("North Apron|SPOT #§ [INTL/FDA]"), customOffset_Spot2),
        3 : (CustomizedName("North Apron|SPOT #§ [JAL]"), customOffset_Spot3),
        4 : (CustomizedName("North Apron|SPOT #§ [ANA]"), customOffset_Spot3),
    }, 

    PARKING : {
        None : (),
        4 : (CustomizedName("{MIL} South Apron (JSDF-G)|#§"), ),
        5 : (CustomizedName("{MIL} South Apron (JSDF-G)|#§"), ),
        6 : (CustomizedName("{MIL} South Apron (JSDF-G)|#§"), ),
        7 : (CustomizedName("{MIL} South Apron (JSDF-G)|#§"), ),

        9 : (CustomizedName("{MIL} South Apron (JSDF-M)|#§"), ),
        10 : (CustomizedName("{MIL} South Apron (JSDF-M)|#§"), ),
        11 : (CustomizedName("{MIL} South Apron (JSDF-M)|#§"), ),
        12 : (CustomizedName("{MIL} South Apron (JSDF-M)|#§"), ),
    }, 
}