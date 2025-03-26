# -- coding: utf-8 --

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
version = 1.1

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    if aircraftData.idMajor == 42 or aircraftData.idMajor == 72:
        return Distance.fromMeters(-27.36)
    elif aircraftData.idMajor == 1008:
        return Distance.fromMeters(-27.36)
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    if aircraftData.idMajor == 42 or aircraftData.idMajor == 72:
        return Distance.fromMeters(-20.05)
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot3(aircraftData):
    if aircraftData.idMajor == 42 or aircraftData.idMajor == 72:
        return Distance.fromMeters(-16.62)
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot4(aircraftData):
    if aircraftData.idMajor == 42 or aircraftData.idMajor == 72:
        return Distance.fromMeters(-18.42)
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    if aircraftData.idMajor == 42 or aircraftData.idMajor == 72:
        return Distance.fromMeters(-18.42)
    elif aircraftData.idMajor == 1008:
        return Distance.fromMeters(-18.42)
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    if aircraftData.idMajor == 42 or aircraftData.idMajor == 72:
        return Distance.fromMeters(-15.77)
    elif aircraftData.idMajor == 1008:
        return Distance.fromMeters(-15.77)
    return Distance.fromMeters(0.)

parkings = {
    GATE : {
        None : (),
        1 : (CustomizedName("Apron A Stand|SPOT #§"), customOffset_Spot1),
        2 : (CustomizedName("Apron A Gate|SPOT #§ [ADO/ANA]"), customOffset_Spot2),
        3 : (CustomizedName("Apron A Gate|SPOT #§ [JAL/J-AIR]"), customOffset_Spot3),
        4 : (CustomizedName("Apron A Gate|SPOT #§ [HAC/J-AIR/JAL]"), customOffset_Spot4),
        5 : (CustomizedName("Apron A Stand|SPOT #§ [HAC]"), customOffset_Spot5),
        6 : (CustomizedName("Apron A Stand|SPOT #§"), customOffset_Spot6),
    },
    PARKING : {
        None : (CustomizedName("Apron B|SPOT #§"), ),
    }
}