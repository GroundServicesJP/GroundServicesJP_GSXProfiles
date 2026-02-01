# -- coding: utf-8 --

# Copyright (C) 2026 GroundServicesJP
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

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("Apron Gate|SPOT #§ [JJP/JAL/SJO]", 1), customOffset_noOffset),
        3 : (CustomizedName("Apron Gate|SPOT #§ [JAL/JJP]", 1), customOffset_noOffset),
        4 : (CustomizedName("Apron Gate|SPOT #§ [ADO/ANA]", 1), customOffset_noOffset),
        5 : (CustomizedName("Apron Gate|SPOT #§ [ADO/ANA/INTL]", 1), customOffset_noOffset),
    },
    PARKING : {
        None : (),
        1 : (CustomizedName("Apron Stand|SPOT #§", 2), customOffset_noOffset),
        11 : (CustomizedName("GA Parking|SPOT #§", 3), ),
        12 : (CustomizedName("GA Parking|SPOT #§", 3), ),
        13 : (CustomizedName("GA Parking|SPOT #§", 3), ),
        14 : (CustomizedName("GA Parking|SPOT #§", 3), ),
        15 : (CustomizedName("GA Parking|SPOT #§", 3), ),
    },
    E_PARKING : {
        None : (),
        1 : (CustomizedName("GA Parking|SPOT 1-E", 3),),
    },
    W_PARKING : {
        None : (),
        1 : (CustomizedName("GA Parking|SPOT 1-W", 3),),
    },
}

