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
version = 0.1

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    common_regional = {42, 72, 1008, 200, 700, 900, 1000, 175, 170}
    if (aircraftData.idMajor in common_regional) or (aircraftData.aircraftGroup in {"ARC-A", "ARC-B"}):
        return Distance.fromMeters(-12.38), Distance.fromMeters(-6.38)
    elif aircraftData.idMajor in {319, 320, 321, 737, 195, 190}:
        return Distance.fromMeters(-5.)
    else:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    common_regional = {42, 72, 1008, 200, 700, 900, 1000, 195, 190, 175, 170}
    if (aircraftData.idMajor in common_regional) or (aircraftData.idMajor in {319, 320, 321, 737}):
        return Distance.fromMeters(-6.42)
    else:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot4(aircraftData):
    common_regional = {42, 72, 1008, 200, 700, 900, 1000, 195, 190, 175, 170}
    if (aircraftData.idMajor in common_regional) or (aircraftData.aircraftGroup in {"ARC-A", "ARC-B"}):
        return Distance.fromMeters(-35.), Distance.fromMeters(-11.46)
    elif aircraftData.idMajor in {319, 320, 321, 737}:
        return Distance.fromMeters(-6.42)
    else:
        return Distance.fromMeters(0.)


parkings = {
    GATE :{
        None : (),
        1 : (CustomizedName("Apron Gates|SPOT 3 [ANA]"), customOffset_Spot3),
        2 : (CustomizedName("Apron Gates|SPOT 4"), customOffset_Spot4),
    },

    PARKING :{
        None : (),
        1 : (CustomizedName("Apron Stands|SPOT 1"), customOffset_noOffset),
        2 : (CustomizedName("Apron Stands|SPOT 2"), customOffset_Spot2),
    },

    NE_PARKING :{
        None : (CustomizedName("Japan Aviation Academy Apron|#§"),),
    },
}