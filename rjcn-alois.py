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

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0.,
        320: -3.1,
        321: -3.1,
        737: -3.1,
        195: -3.1,
        190: -3.1,
        175: -3.1,
        170: -3.1,
        42: -30.07,
        72: -30.07,
        1008: -30.07,
        200: -30.07,
        700: -30.07,
        900: -30.07,
        1000: -30.07,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        1008: 5.75,
        42: 5.75,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

parkings = {
    GATE : {
        None : (),
        1 : (CustomizedName("Apron Gate|SPOT #§ [ANA/AKX]"), customOffset_Spot1),
        2 : (CustomizedName("Apron Stand|SPOT #§ [HAC/AKX]"), customOffset_Spot2),
        3 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot2),
    }
}