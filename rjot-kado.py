# -- coding: utf-8 --

# Copyright (C) 2025 GroundServicesJP (Legotatsu1985)
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
version = 1.3
icao="rjot"

@AlternativeStopPositions
def customOffsetGate_0(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffsetGate_2(aircraftData):
    table = {
        0: 0,
        319: -5.60,
        320: -5.60,
        321: -5.60,
        737: -5.60,
        170: -5.60,
        175: -5.60,
        190: -5.60,
    }
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffsetGate_3(aircraftData):
    table = {
        0: 0,
        319: -7.85,
        320: -7.85,
        321: -7.85,
        737: -7.85,
        170: -1.80,
        175: -1.80,
        190: -1.80,
    }
    table_787 = {
        8: -1.80,
        9: 0.,
        10: 0.,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(table_787.get(aircraftData.idMinor, 0))
    else:
        try:
            return Distance.fromMeters(table.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffsetGate_5_6(aircraftData):
    table = {
        0: 0,
        319: -3.40,
        320: -3.40,
        321: -3.40,
        737: -3.40,
        170: -1.65,
        175: -1.65,
        190: -1.65,
    }
    table_787 = {
        8: -1.65,
        9: 0.,
        10: 0.,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(table_787.get(aircraftData.idMinor, 0))
    else:
        try:
            return Distance.fromMeters(table.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0.)

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("Apron Gate|SPOT 2 [JAL]"), customOffsetGate_2),
        3 : (CustomizedName("Apron Gate|SPOT 3 [ANA]"), customOffsetGate_3),
        5 : (CustomizedName("Apron Gate|SPOT 5 [JJP/INTL/FDA]"), customOffsetGate_5_6),
        6 : (CustomizedName("Apron Gate|SPOT 6 [INTL]"), customOffsetGate_5_6),
    },
    PARKING : {
        None : (),
        1 : (CustomizedName("Apron Stand|SPOT 1"), customOffsetGate_0),
        7 : (CustomizedName("Apron Stand|SPOT 7"), customOffsetGate_0),
        12 : (CustomizedName("East Apron|C"), ),
        13 : (CustomizedName("East Apron|E"), ),
        14 : (CustomizedName("East Apron|G"), ),
        15 : (CustomizedName("East Apron|F"), ),
        16 : (CustomizedName("East Apron|D"), ),
        18 : (CustomizedName("East Apron|K"), ),
        19 : (CustomizedName("East Apron|J"), ),
        20 : (CustomizedName("East Apron|L"), ),
        21 : (CustomizedName("East Apron|M"), ),
        22 : (CustomizedName("East Apron|N"), ),
        23 : (CustomizedName("East Apron|O"), ),
        24 : (CustomizedName("East Apron|P"), ),
        31 : (CustomizedName("West Apron|W"), ),
        32 : (CustomizedName("West Apron|X"), ),
        33 : (CustomizedName("West Apron|Y"), ),
        34 : (CustomizedName("West Apron|Z"), ),
        35 : (CustomizedName("East Apron|B"), ),
        36 : (CustomizedName("East Apron|A"), ),
    },
}