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
    myTable = {
        0: 0,
        767: -6.9,
        320: -6.9,
        321: -6.9,
        737: -6.9,
        195: -6.9,
        190: -6.9,
        175: -6.9,
        170: -6.9,
        42: -16.25,
        72: -16.25,
        1008: -16.25,
        200: -16.25,
        700: -16.25,
        900: -16.25,
        1000: -16.25,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot4(aircraftData):
    myTable = {
        0: 0,
        767: -6.9,
        320: -6.9,
        321: -6.9,
        737: -6.9,
        195: -6.9,
        190: -6.9,
        175: -6.9,
        170: -6.9,
        42: -12.35,
        72: -12.35,
        1008: -12.35,
        200: -12.35,
        700: -12.35,
        900: -12.35,
        1000: -12.35,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    myTable = {
        0: 0,
        767: -6.52,
        320: -12.,
        321: -12.,
        737: -12.,
        195: -12.,
        190: -12.,
        175: -12.,
        170: -12.,
        42: -12.,
        72: -12.,
        1008: -12.,
        200: -12.,
        700: -12.,
        900: -12.,
        1000: -12.,

    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    myTable = {
        0: 0,
        767: -6.9,
        320: -6.9,
        321: -6.9,
        737: -6.9,
        195: -6.9,
        190: -6.9,
        175: -6.9,
        170: -6.9,
        42: -16.,
        72: -16.,
        1008: -16.,
        200: -16.,
        700: -16.,
        900: -16.,
        1000: -16.,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot7(aircraftData):
    myTable = {
        0: 0,
        767: -6.9,
        320: -6.9,
        321: -6.9,
        737: -6.9,
        195: -6.9,
        190: -6.9,
        175: -6.9,
        170: -6.9,
        42: -22.4,
        72: -22.4,
        1008: -22.4,
        200: -22.4,
        700: -22.4,
        900: -22.4,
        1000: -22.4,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot8(aircraftData):
    myTable = {
        0: 0,
        320: -8.33,
        321: -8.33,
        737: -8.33,
        195: -8.33,
        190: -8.33,
        175: -8.33,
        170: -8.33,
        42: -8.33,
        72: -8.33,
        1008: -8.33,
        200: -8.33,
        700: -8.33,
        900: -8.33,
        1000: -8.33,
    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot10(aircraftData):
    myTable = {
        0: 0,
        42: -14.5,
        72: -14.5,
        1008: -14.5,
        200: -14.5,
        700: -14.5,
        900: -14.5,
        1000: -14.5,

    }
    return Distance.fromMeters(myTable.get(aircraftData.idMajor,0))

parkings = {
    GATE :{
        None : (),
        3 : (CustomizedName("Apron Gate|SPOT #§"), customOffset_Spot3),
        4 : (CustomizedName("Apron Gate|SPOT #§"), customOffset_Spot4),
        5 : (CustomizedName("Apron Gate|SPOT #§"), customOffset_Spot5),
        6 : (CustomizedName("Apron Gate|SPOT #§"), customOffset_Spot6),
        7 : (CustomizedName("Apron Gate|SPOT #§"), customOffset_Spot7),
    }, 

    PARKING :{
        None : (),
        1 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot4),
        2 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot7),
        8 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot8),
        9 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot8),
        10 : (CustomizedName("Apron Stand|SPOT #§"), customOffset_Spot10),

        11 : (CustomizedName("{Heli} East Apron|Parking"), ),

        26 : (CustomizedName("{Heli} Airbus Helicopter|1"), ),
        27 : (CustomizedName("{Heli} Airbus Helicopter|3"), ),
        28 : (CustomizedName("{Heli} Airbus Helicopter|4"), ),
        29 : (CustomizedName("{Heli} Airbus Helicopter|2"), ),

        25 : (CustomizedName("{Heli/GA} Hirata Gakuen|H"), ),
        20 : (CustomizedName("{Heli/GA} Hirata Gakuen|1"), ),
        21 : (CustomizedName("{Heli/GA} Hirata Gakuen|2"), ),
        22 : (CustomizedName("{Heli/GA} Hirata Gakuen|3"), ),
        23 : (CustomizedName("{Heli/GA} Hirata Gakuen|4"), ),
        24 : (CustomizedName("{Heli/GA} Hirata Gakuen|5"), ),

        13 : (CustomizedName("{Heli} Kobe Fire Bureau|2"), ),
        14 : (CustomizedName("{Heli} Kobe Fire Bureau|1"), ),
        15 : (CustomizedName("{Heli} Kobe Fire Bureau|3"), ),
        16 : (CustomizedName("{Heli} Kobe Fire Bureau|6"), ),
        17 : (CustomizedName("{Heli} Kobe Fire Bureau|4"), ),
        18 : (CustomizedName("{Heli} Kobe Fire Bureau|5"), ),
        19 : (CustomizedName("{Heli} Kobe Fire Bureau|7"), ),
    }, 
}