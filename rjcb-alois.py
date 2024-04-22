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
def customOffset_Spot35(aircraftData):
    myTable = {
        0: 0.,
        42: -7.5,
        72: -7.5,
        320: -7.5,
        321: -7.5,
        170: -7.5,
        175: -7.5,
        190: -7.5,
        195: -7.5,
        1008: -7.5,
        737: -7.5,
        737: -7.5,
        767: -7.5,
    }
    # If not in my table, set to zero displacement
    if myTable.get(aircraftData.idMajor) == None:
        return Distance.fromMeters(0.)
    return Distance.fromMeters( myTable.get(aircraftData.idMajor) )

@AlternativeStopPositions
def customOffset_Spot12(aircraftData):
    myTable = {
        0: 0.,
        42: -6.5,
        72: -6.5,
        320: -6.5,
        321: -6.5,
        170: -6.5,
        175: -6.5,
        190: -6.5,
        195: -6.5,
        1008: -6.5,
        737: -6.5,
        737: -6.5,
        767: -6.5,
    }
    # If not in my table, set to zero displacement
    if myTable.get(aircraftData.idMajor) == None:
        return Distance.fromMeters(0.)
    return Distance.fromMeters( myTable.get(aircraftData.idMajor) )


parkings = {
    GATE :{
        None : (),
        1 : (CustomizedName("Apron A Gate|Spot #§ [INTL]"), customOffset_Spot12),
        2 : (CustomizedName("Apron A Gate|Spot #§ [ADO]"), customOffset_Spot12),
        3 : (CustomizedName("Apron A Gate|Spot #§ [JAL]"), customOffset_Spot35),
        5 : (CustomizedName("Apron A Stand|Spot #§"), customOffset_Spot35),
    },
    PARKING :{
        None : (),
        11 : (CustomizedName("Apron B|Spot #§"), ),
        12 : (CustomizedName("Apron B|Spot #§"), ),
        13 : (CustomizedName("Apron B|Spot #§"), ),
        14 : (CustomizedName("Apron B|Spot #§"), ),
        15 : (CustomizedName("Apron B|Spot #§"), ),
        16 : (CustomizedName("Apron B|Spot #§"), ),
    },
    N_PARKING :{
        None : (),
        1 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        2 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        3 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        4 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        5 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        6 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        7 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        8 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        9 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        10 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        11 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
        12 : (CustomizedName("Charlie Apron [CAC]|#§"), ),
    }
}
