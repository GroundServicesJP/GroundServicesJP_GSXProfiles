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
def customOffset_zero(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot9(aircraftData):
    myTable = {
        0: 26.,
        1008: 0.,
    }
    # If not in my table, set to 20m displacement
    if myTable.get(aircraftData.idMajor) == None:
        return Distance.fromMeters(21.)
    return Distance.fromMeters( myTable.get(aircraftData.idMajor) )

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("Apron Stand|Spot #§"), customOffset_zero),
        5 : (CustomizedName("Apron Gate|Spot #§ [ANA/SNA/APJ]"), customOffset_zero),
        6 : (CustomizedName("Apron Gate|Spot #§ [ANA/SNA/APJ]"), customOffset_zero),
        7 : (CustomizedName("Apron Gate|Spot #§ [JAL/JTA]"),customOffset_zero ),
        8 : (CustomizedName("Apron Gate|Spot #§ [JAL/JTA]"), customOffset_zero),
        9 : (CustomizedName("Apron Spot 9|Spot #§ [RAC/INTL]"), customOffset_Spot9),
    },
    0 : {
        None : (),
        10 : (CustomizedName("Apron Stand|Spot #§"), customOffset_zero),
    }
}