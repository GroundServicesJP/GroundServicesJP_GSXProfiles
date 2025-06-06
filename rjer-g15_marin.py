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
def customOffset_RJER(aircraftData):
    myTable = {
        0: 0.,
        42: -0.8,
        737: 0.,
    }
    # If not in my table, set to zero displacement
    if myTable.get(aircraftData.idMajor) == None:
        return Distance.fromMeters(0.)
    return Distance.fromMeters( myTable.get(aircraftData.idMajor) )

parkings = {
    PARKING :{
        None : (),
        1 : (CustomizedName("Apron|SPOT #§"), customOffset_RJER),
        2 : (CustomizedName("Apron|SPOT #§ [ANA/HAC]"), customOffset_RJER),
        3 : (CustomizedName("Apron|SPOT #§"), ),
        5 : (CustomizedName("Apron|SPOT #§"), ),
    }
}
