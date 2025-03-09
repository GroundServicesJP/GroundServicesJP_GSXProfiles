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
def customOffset_Spot3(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -0.94

    mainTable = {
        0: T_loc,
        767: first,
        787: first,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,T_loc))

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -0.6
    second = -0.9

    mainTable = {
        0: first,
        319: first,
        320: first,
        321: first,
        737: T_loc,
        # ERJ
        195: T_loc, 
        190: T_loc,
        175: T_loc, 
        170: T_loc, 
        # Q400
        1008: T_loc,
        #Heavy
        767: second,
        787: second,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,first))

@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    # Product of GSJP
    T_loc = 0.
    first = -0.9
    second = -18.5

    mainTable = {
        0: first,
        319: first,
        320: first,
        321: first,
        737: first,
        # ERJ
        195: first, 
        190: first,
        175: second, 
        170: second, 
        # Q400
        1008: second,
        #Heavy
        767: T_loc,
        787: T_loc,
    }

    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,first))


parkings = {
    0 : {
        None : (),
        1 : (CustomizedName("Apron Stand|Spot #§"), customOffset_noOffset),
        2 : (CustomizedName("Apron Gate|Spot #§"), customOffset_noOffset),
        3 : (CustomizedName("Apron Gate|Spot #§"), customOffset_Spot3),
        5 : (CustomizedName("Apron Gate|Spot #§"), customOffset_Spot5),
        6 : (CustomizedName("Apron Stand|Spot #§"), customOffset_Spot6),
        11 : (CustomizedName("East Apron|Spot #§"), ),
        12 : (CustomizedName("East Apron|Spot #§"), ),
        13 : (CustomizedName("East Apron|Spot #§"), ),
        14 : (CustomizedName("East Apron|Spot #§"), ),
        15 : (CustomizedName("East Apron|Spot #§"), ),
        16 : (CustomizedName("East Apron|Spot #§"), ),
        17 : (CustomizedName("East Apron|Spot #§"), ),
        101 : (CustomizedName("AK Apron|1"), ),
        102 : (CustomizedName("AK Apron|2"), ),
        103 : (CustomizedName("AK Apron|3"), ),
        105 : (CustomizedName("AK Apron|5"), ),
        106 : (CustomizedName("JSDF Apron|#§"), ),
        107 : (CustomizedName("JSDF Apron|#§"), ),
        108 : (CustomizedName("JSDF Apron|#§"), ),
        109 : (CustomizedName("JSDF Apron|#§"), ),
        110 : (CustomizedName("JSDF Apron|#§"), ),
        111 : (CustomizedName("JSDF Apron|#§"), ),
    }
}
