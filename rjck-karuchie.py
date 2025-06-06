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
version = 1.3

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    T_mark = 0.
    first = -4.4
    second = -15.57

    myTable = {
        0: T_mark,
        42: second,
        72: second,
        1008: second,
        200: second,
        700: second,
        900: second,
        1000: second,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    T_mark = 0.
    first = -3.5
    second = -19.06

    myTable = {
        0: T_mark,
        42: second,
        72: second,
        1008: second,
        200: second,
        700: second,
        900: second,
        1000: second,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    # Product of GSJP
    T_mark = 0.
    first = -2.7
    second = -18.27

    myTable = {
        0: T_mark,
        42: second,
        72: second,
        1008: second,
        200: second,
        700: second,
        900: second,
        1000: second,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

parkings = {
    GATE : {
        None : (),
        3 : (CustomizedName("Apron Gates|Spot #§ [JAL]"), customOffset_Spot3),
        5 : (CustomizedName("Apron Gates|Spot #§ [ANA/ADO/APJ/JAL/HAC]"), customOffset_Spot5),
        6 : (CustomizedName("Apron Gates|Spot #§ [ANA/ADO/APJ]"), customOffset_Spot6),
    },
    PARKING : {
        None : (),
        1 : (CustomizedName("Apron Stands|Spot #§"), customOffset_noOffset),
        2 : (CustomizedName("Apron Stands|Spot #§ [HAC]"), customOffset_noOffset), 
        7 : (CustomizedName("Apron Stands|Spot #§ [HAC]"), customOffset_noOffset),
    },
    0 : {
        None : (CustomizedName("JCG Kushiro/GA Parking|#§"),),
    }
}
