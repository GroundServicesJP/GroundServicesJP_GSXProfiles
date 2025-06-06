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
def customOffset_Spot2(aircraftData):
    # Product of GSJP
    first = -2.1
    second = -3.2

    mainTable = {
        0: 0.,
        320: second,
        321: first,
        737: first,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        1008: second,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0.))

parkings = {
    GATE : {
        None : (),
        3 : (CustomizedName("Apron Gates|SPOT #§ [ANA]"), customOffset_Spot2),
    },
    PARKING : {
        None : (),
        1 : (CustomizedName("Apron Stands|SPOT #§"), customOffset_noOffset),
        2 : (CustomizedName("Apron Stands|Spot #§"), customOffset_Spot2),
    },
    0 : {
        5 : (CustomizedName("GA Parking|#§"), ),
        6 : (CustomizedName("GA Parking|#§"), ),
        7 : (CustomizedName("GA Parking|#§"), ),
        8 : (CustomizedName("GA Parking|#§"), ),
        9 : (CustomizedName("GA Parking|#§"), ),
    }
}
