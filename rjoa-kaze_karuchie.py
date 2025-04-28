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
version = 1.3

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    first = -3.

    mainTable = {
        0: 0.,
        767: first,
        319: first,
        320: first,
        321: first,
        737: first,
        # ERJ
        195: first, 
        190: first,
        175: first, 
        170: first, 
        # CRJ700
        700 : first,
    }

    table330 = {
        200: first, # 58.82m
        300: first, # 63.66m
        800: first, # 58.82m
        900: 0., # 63.66m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: first, # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: first, # 56.72m
        9: first, # 62.81m
        10: 0., # 68.28m
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot7L(aircraftData):
    if aircraftData.idMajor == 777:
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor == 330:
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(0.)
    elif aircraftData.idMajor == 767:
        return Distance.fromMeters(0.)
    return Distance.fromMeters(-12.)

@AlternativeStopPositions
def customOffset_Spot8(aircraftData):
    # Product of GSJP
    first = -3.
    second = -9.64-7.
    third = -30.

    mainTable = {
        0: first,
        767: first,
        319: second,
        320: second,
        321: second,
        737: second,
        # ERJ
        195: second, 
        190: second,
        175: second, 
        170: second, 
        # CRJ700
        700 : second,
        # Q400
        1008: third,
        # ATR
        42: third,
        72: third,
    }

    table330 = {
        200: first, # 58.82m
        300: first, # 63.66m
        800: first, # 58.82m
        900: first, # 63.66m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: first, # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: first, # 56.72m
        9: first, # 62.81m
        10: 0., # 68.28m
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot9(aircraftData):
    if aircraftData.idMajor == 42:
        return Distance.fromMeters(-38.)
    elif aircraftData.idMajor == 72:
        return Distance.fromMeters(-38.)
    elif aircraftData.idMajor == 1008:
        return Distance.fromMeters(-38.)
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot10(aircraftData):
    # Product of GSJP
    first = -3.
    second = -38.

    mainTable = {
        0: 0.,
        767: 0.,
        318: first,
        319: first,
        320: first,
        321: first,
        737: first,
        # ERJ
        195: first, 
        190: first,
        175: first, 
        170: first, 
        # CRJ700
        700 : second,
        # Q400
        1008: second,
        # ATR
        42: second,
        72: second,
    }

    table330 = {
        200: 0., # 58.82m
        300: 0., # 63.66m
        800: 0., # 58.82m
        900: 0., # 63.66m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0, # 73.79m
    }

    table777 = {
        200: 0., # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: 0., # 56.72m
        9: 0., # 62.81m
        10: 0., # 68.28m
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("Apron Gates|SPOT #§ [ANA/IBEX]"), customOffset_Spot5),
        3 : (CustomizedName("Apron Gates|SPOT #§ [JAL]"), customOffset_Spot5),
        5 : (CustomizedName("Apron Gates|SPOT #§ [ANA]"), customOffset_Spot5),
        6 : (CustomizedName("Apron Gates|SPOT #§ [DOM/INTL]"), customOffset_noOffset),
        7 : (CustomizedName("Apron Gates|SPOT #§ [INTL]"), customOffset_Spot7L),
        8 : (CustomizedName("Apron Gates|SPOT #§ [INTL]"), customOffset_Spot8),

    },
    PARKING : {
        None : (),
        1 : (CustomizedName("Apron Stands|SPOT #§"), customOffset_noOffset),
        9 : (CustomizedName("Apron Stands|SPOT #§"), customOffset_Spot9),
        10 : (CustomizedName("Apron Stands|SPOT #§"), customOffset_Spot10),
    },

    E_PARKING : {
        None : (CustomizedName("Hiroshima Perf Bousai|#§"), ),
    },

    S_PARKING : {
        None : (CustomizedName("Sub Apron|#§"), ),
    },

    0 : {
        None : (CustomizedName("GA SPOTs (H/I/J)|#§"), ),
    }
}
