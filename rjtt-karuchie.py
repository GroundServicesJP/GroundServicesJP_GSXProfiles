# -- coding: utf-8 --

# Copyright (C) 2025 GroundServicesJP TEAM HANEDA (Rokumaru, RIN, ANA7875)
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
version = 1.2

## No offset
@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

## Terminal 1 + West Cargo Area ##
@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    # (Other) 0 (320/737/175/190) -3.6
    mainTable = {
        0: 0.,
        767: 0.,
        787: 0.,
        320: -3.6,
        321: -3.6,
        737: -3.6,
        190: -3.6,
        170: -3.6,
        175: -3.6,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot2(aircraftData):
    # (773) 0, (772/359) 0.83, (787/763) 2.93, 
    # (737/320) 8.21, (170/175/190) 10.50
    mainTable = {
        0: 0.,
        350: -0.83,
        767: -2.93,
        787: -2.93,
        320: -8.21,
        321: -8.21,
        737: -8.21,
        190: -10.5,
        170: -10.5,
        175: -10.5,
    }

    table777 = {
        200: -0.83,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # (773/350/772) 0, (787/767) 3.71, 
    # (737/320/170/175/190) 10.18
    mainTable = {
        0: 0.,
        350: 0.,
        767: -3.71,
        787: -3.71,
        320: -10.18,
        321: -10.18,
        737: -10.18,
        190: -10.18,
        170: -10.18,
        175: -10.18,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot7(aircraftData):
    # (773) 0, (350/772) 0.65, (787/767) 3.13, 
    # (737/320) 9.82, (170/175/190) 11.13
    mainTable = {
        0: 0.,
        350: -0.65,
        767: -3.13,
        787: -3.13,
        320: -9.82,
        321: -9.82,
        737: -9.82,
        190: -11.13,
        170: -11.13,
        175: -11.13,
    }

    table777 = {
        200: -0.65,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot8(aircraftData):
    # (773) 0, (772) 0.6, (359) 1.83, (763) 3.61, 
    # (788) 5.15, (737/320) 8.99, (170/175/190) 10.32
    mainTable = {
        0: 0.,
        350: -1.83,
        767: -3.61,
        787: -5.15,
        320: -8.99,
        321: -8.99,
        737: -8.99,
        190: -10.32,
        170: -10.32,
        175: -10.32,
    }

    table777 = {
        200: -0.6,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot9(aircraftData):
    # (773) 0, (772) 1.14, (359) 1.89, (763) 2.96, 
    # (788) 5.50, (737/320) 9.94, (170/175/190) 9.94
    mainTable = {
        0: 0.,
        350: -1.89,
        767: -2.96,
        787: -5.50,
        320: -9.94,
        321: -9.94,
        737: -9.94,
        190: -9.94,
        170: -9.94,
        175: -9.94,
    }

    table777 = {
        200: -1.14,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot11(aircraftData):
    # (359) +0.63, (773) 0, (763) -0.63, (772) -1.82 (788) -5.37
    mainTable = {
        350: 0.63,
        0: 0.,
        767: -0.63,
        787: -5.37,
        320: -11.63,
        321: -11.63,
        737: -11.63,
        190: -11.63,
        170: -11.63,
        175: -11.63,
    }

    table777 = {
        200: -1.82,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot12(aircraftData):
    # (359) 0, (773) -0.88, (763) -3.66, (772) -4.40 (788) -5.02
    # (737/320) 10.37, (190/170/175) 15.05
    mainTable = {
        350: 0.,
        0: 0.,
        767: -3.66,
        787: -5.02,
        320: -10.37,
        321: -10.37,
        737: -10.37,
        190: -15.05,
        170: -15.05,
        175: -15.05,
    }

    table777 = {
        200: -4.40,
        300: -0.88,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot17(aircraftData):
    # (359) +1.93, (773) 0, (763) -1.17, (772) -3.63 (788) -4.63
    # (737/320/190/175/170) -10.10
    mainTable = {
        350: 1.93,
        0: 0.,
        767: -1.17,
        787: -4.63,
        320: -10.10,
        321: -10.10,
        737: -10.10,
        190: -10.10,
        170: -10.10,
        175: -10.10,
    }

    table777 = {
        200: -3.63,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot18(aircraftData):
    # (773) 0, (772/359) 1.73, (763/788) 3.08, 
    # (737/320) 11.75, (170/175/190) 11.75
    mainTable = {
        0: 0.,
        350: -1.73,
        767: -3.08,
        787: -3.08,
        320: -11.75,
        321: -11.75,
        737: -11.75,
        190: -11.75,
        170: -11.75,
        175: -11.75,
    }

    table777 = {
        200: -1.73,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot21(aircraftData):
    # (773/772/359) 0, (763/788) 6, 
    # (737/320/170/175/190) 10.99
    mainTable = {
        0: 0.,
        350: 0.,
        767: -6,
        787: -6,
        320: -10.99,
        321: -10.99,
        737: -10.99,
        190: -10.99,
        170: -10.99,
        175: -10.99,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot22(aircraftData):
    # (773/772/359) 0, (763/788) 6, 
    # (737/320/170/175/190) 10.99
    mainTable = {
        0: 0.,
        320: -10.19,
        321: -10.19,
        737: -10.19,
        190: -10.19,
        170: -10.19,
        175: -10.19,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot38(aircraftData):
    # (773/359) +3.71, (763/788/772) 0, 
    # (737/320/170/175/190) -3.4
    mainTable = {
        0: 0.,
        350: 3.71,
        767: 0.,
        787: 0.,
        320: -3.4,
        321: -3.4,
        737: -3.4,
        190: -3.4,
        170: -3.4,
        175: -3.4,
    }

    table777 = {
        200: 0.,
        300: 3.71,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

################
## Terminal 2 ##
@AlternativeStopPositions
def customOffset_Spot53(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -1.07,
        767: -1.07,
        320: -13.05,
        321: -13.05,
        737: -13.05,
        190: -17.36,
        170: -17.36,
        175: -17.36,
    }

    table777 = {
        200: -1.07,
        300: 0.97,
    }

    table787 = {
        8: -3.15,
        9: -3.15,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot54(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -13,
        320: -16.95,
        321: -16.95,
        737: -18.65,
        190: -18.65,
        170: -18.65,
        175: -18.65,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: 0.,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot55(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -10.67,
        320: -17.47,
        321: -17.47,
        737: -18.65,
        190: -18.65,
        170: -18.65,
        175: -18.65,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: 0.,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot56(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -8.51,
        320: -16., #Real:-17.72
        321: -16., #Real:-17.72
        737: -16., #Real:-18
        190: -16.,
        170: -16.,
        175: -16.,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: 0.,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot58(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -2.02,
        320: -7.5, # Real: -9.30
        321: -7.5, # Real: -9.30
        737: -7.5, # Real:-10.40
        190: -7.5,
        170: -7.5,
        175: -7.5,
    }

    table777 = {
        200: -2.02,
        300: 2.45,
    }

    table787 = {
        8: -2.02,
        9: -2.02,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot65(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -2.96,
        350: -5.97,
        767: -5.43,
        320: -11.73,
        321: -11.73,
        737: -15.69,
        190: -15.69,
        170: -15.69,
        175: -15.69,
    }

    table777 = {
        200: -2.68,
        300: 2.32,
    }

    table787 = {
        8: -6.47,
        9: -5.43,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot66(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -2.96,
        350: -5.97,
        767: -5.97,
        320: -17.07,
        321: -17.07,
        737: -17.07, #Real: -25.05
        190: -17.07,
        170: -17.07,
        175: -17.07,
    }

    table777 = {
        200: -5.97,
        300: -2.96,
    }

    table787 = {
        8: -6.95,
        9: -5.97,
        10: -2.96,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot68(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -0.99,
        350: -3.93,
        767: -7.33,
        320: -15.38,
        321: -15.38,
        737: -15.38, # Real: -18.52
        190: -15.38,
        170: -15.38,
        175: -15.38,
    }

    table777 = {
        200: -3.93,
        300: -0.99,
    }

    table787 = {
        8: -7.33,
        9: -3.93,
        10: -0.99,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot69(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -3.24,
        320: -16.09,
        321: -16.09,
        737: -19.27,
        190: -19.27,
        170: -19.27,
        175: -19.27,
    }

    table777 = {
        200: 0.,
        300: 0., # changed from 2.17
    }

    table787 = {
        8: -7.65,
        9: -6.28,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot70(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        320: 0.,
        321: 0.,
        737: -1.,
        190: -1.,
        170: -1.,
        175: -1.,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: 0.,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot71(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -4.04,
        320: -10., #Real:-12.05
        321: -10., #Real:-12.05
        737: -10., #Real:-17
        190: -10.,
        170: -10.,
        175: -10.,
    }

    table777 = {
        200: -1.97,
        300: 0.,
    }

    table787 = {
        8: -6.49,
        9: -6.49,
        10: -1.97,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot73(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -0.99,
        350: -3.06,
        767: -4.10,
        320: -13., #Real: -18.57
        321: -13., #Real: -18.57
        737: -13., #Real: -18.57
        190: -13.,
        170: -13.,
        175: -13.,
    }

    table777 = {
        200: -3.06,
        300: 2.42,
    }

    table787 = {
        8: -4.10,
        9: -3.06,
        10: -0.99,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

################
## Spots 81-84 ##
@AlternativeStopPositions
def customOffset_Spot81(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: -1.08,
        320: -10.06,
        321: -10.06,
        737: -8.35,
        190: -8.35,
        170: -8.35,
        175: -8.35,
        1008: -8.35,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -1.08,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot84(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: -2.92,
        320: -10.06,
        321: -10.06,
        737: -8.35,
        190: -8.35,
        170: -8.35,
        175: -8.35,
        1008: -8.35,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -2.92,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

################
## East Cargo Area + T2 Satellite ##
@AlternativeStopPositions
def customOffset_SpotVS(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: -3.45,
        787: -3.45,
        320: -8.49,
        321: -9.04,
        737: -14.0,
        190: -14.0,
        170: -14.0,
        175: -14.0,
        1008: -14.0,
    }

    table777 = {
        200: -0.46,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot401(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.85,
        767: -1.15,
        787: -2.57,
        320: -5.12,
        321: -5.76,
        737: -7.98,
        190: -7.98,
        170: -7.98,
        175: -7.98,
        1008: -7.98,
    }

    table777 = {
        200: 0.,
        300: 0.85,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot402(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.93,
        767: -1.13,
        787: -3.91,
        320: -5.72,
        321: -5.72,
        737: -7.98,
        190: -7.98,
        170: -7.98,
        175: -7.98,
        1008: -7.98,
    }

    table777 = {
        200: 0.,
        300: 0.93,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot406(aircraftData):
    mainTable = {
        0: 0.,
        350: -1.56,
        767: -5.10,
        320: -13.32,
        321: -13.32,
        737: -13.32,
        190: -13.32,
        170: -13.32,
        175: -13.32,
    }

    table777 = {
        200: -1.56,
        300: 0.,
    }

    table787 = {
        8: -6.57,
        9: -6.57,
        10: -5.78,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot501(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -13.36,
        321: -13.36,
        737: -13.36,
        190: -13.36,
        170: -13.36,
        175: -13.36,
        1008: -13.36,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot502(aircraftData):
    mainTable = {
        0: 0.,
        350: -3.,
        767: -3.,
        787: -3.,
        320: -4.86,
        321: -4.86,
        190: -6.4,
        170: -6.4,
        175: -6.4,
        1008: -6.4,
    }

    table777 = {
        200: -3.,
        300: 0.,
    }

    table737 = {
        700: -6.4,
        800: -4.86,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot505(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: -2.2,
        320: -13.4,
        321: -13.4,
        190: -16.86,
        170: -16.86,
        175: -16.86,
        1008: -16.86,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table737 = {
        700: -16.86,
        800: -13.4,
    }

    table787 = {
        8: -2.2,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot503(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: -1.04,
        320: -3.03,
        321: -3.03,
        190: -3.89,
        170: -3.89,
        175: -3.89,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table737 = {
        700: -3.89,
        800: -3.03,
    }

    table787 = {
        8: -1.04,
        9: -1.04,
        10: -1.04,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 737:
        return Distance.fromMeters(table737.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot506(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -1.,
        321: -1.,
        737: -3.24,
        190: -3.24,
        170: -3.24,
        175: -3.24,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot507(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -5.77,
        321: -5.77,
        737: -5.77,
        190: -5.77,
        170: -5.77,
        175: -5.77,
        1008: -5.77,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

################
## SE Parking
@AlternativeStopPositions
def customOffset_Spot601(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -4.48,
        321: -4.48,
        737: -4.48,
        190: -4.48,
        170: -4.48,
        175: -4.48,
        1008: -4.48,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot604(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -5.7,
        321: -5.7,
        737: -5.7,
        190: -5.7,
        170: -5.7,
        175: -5.7,
        1008: -5.7,
    }

    table777 = {
        200: 0.,
        300: 3.30,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot801(aircraftData):
    mainTable = {
        0: -7.80,
        350: -7.80,
        767: -7.80,
        787: -7.80,
        320: -7.80,
        321: -7.80,
        737: -7.80,
        190: -7.80,
        170: -7.80,
        175: -7.80,
        1008: -7.80,
    }

    table777 = {
        200: -7.80,
        300: -1.96,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot802(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -10.83,
        321: -10.83,
        737: -10.83,
        190: -10.83,
        170: -10.83,
        175: -10.83,
        1008: -10.83,
    }

    table777 = {
        200: 0.,
        300: 15.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot803(aircraftData):
    mainTable = {
        0: -5.84,
        350: -5.84,
        767: -5.84,
        787: -5.84,
        320: -5.84,
        321: -5.84,
        737: -5.84,
        190: -5.84,
        170: -5.84,
        175: -5.84,
        1008: -5.84,
    }

    table777 = {
        200: -5.84,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot804(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -7.26,
        321: -7.26,
        737: -7.26,
        190: -7.26,
        170: -7.26,
        175: -7.26,
        1008: -7.26,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot806(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: -10.24,
        320: -12.67,
        321: -12.67,
        737: -12.67,
        190: -12.67,
        170: -12.67,
        175: -12.67,
        1008: -12.67,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: -10.24,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot807(aircraftData):
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        320: -2.52,
        321: -2.52,
        737: -2.52,
        190: -2.52,
        170: -2.52,
        175: -2.52,
        1008: -2.52,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    table787 = {
        8: 0.,
        9: 0.,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot701(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -14.86,
        321: -14.86,
        737: -14.86,
        190: -14.86,
        170: -14.86,
        175: -14.86,
        1008: -14.86,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot702(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -3.85,
        787: -3.85,
        320: -14.86,
        321: -14.86,
        737: -14.86,
        190: -14.86,
        170: -14.86,
        175: -14.86,
        1008: -14.86,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot704(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        787: 0.,
        320: -10.35,
        321: -10.35,
        737: -10.35,
        190: -10.35,
        170: -10.35,
        175: -10.35,
        1008: -10.35,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot705(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -14.47,
        787: 0.,
        320: -24.45,
        321: -24.45,
        737: -24.45,
        190: -24.45,
        170: -24.45,
        175: -24.45,
        1008: -24.45,
    }

    table777 = {
        200: 0.,
        300: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot706(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 4.77,
        350: 4.77,
        767: 4.77,
        787: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        190: 0.,
        170: 0.,
        175: 0.,
        1008: 0.,
    }

    table777 = {
        200: 4.77,
        300: 4.77,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

################
## T3 Parking
@AlternativeStopPositions
def customOffset_Spot101(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0., # 48.51m-54.94m-61.37m
        319: -8.51, # 33.84m
        320: -6.09, # 37.57m
        321: -6.09, # 44.51m
        737: -8.51, # 31–43.8m
        190: -8.51, # 36.25m
        170: -8.51, # 29.90m
        175: -8.51, # 31.67m
        1008: -8.51, # 32.8m
        221: -8.51, # 35m
        223: -8.51, # 38.71m
        747: 0., # 70.7m/76.25m
        380: 0., # 72.72m
    }

    table330 = {
        200: 0., # 58.82m
        300: 0., # 63.66m
        800: 0., # 58.82m
        900: 0., # 63.66m
    }

    table340 = {
        200: 0., # 59.4m
        300: 0., # 63.69m
        500: 0., # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
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

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot121(aircraftData):
    # Product of GSJP
    # Manufactured Solution
    mainTable = {
        0: 0.,
        767: 0., # 48.51m-54.94m-61.37m
        319: -3.46, # 33.84m
        320: -3.46, # 37.57m
        321: -3.46, # 44.51m
        737: -3.46, # 31–43.8m
        190: -3.46, # 36.25m
        170: -3.46, # 29.90m
        175: -3.46, # 31.67m
        1008: -3.46, # 32.8m
        221: -3.46, # 35m
        223: -3.46, # 38.71m
        747: 1.92, # 70.7m/76.25m
        380: 1.92, # 72.72m
    }

    table330 = {
        200: 0., # 58.82m
        300: 0., # 63.66m
        800: 0., # 58.82m
        900: 0., # 63.66m
    }

    table340 = {
        200: 0., # 59.4m
        300: 0., # 63.69m
        500: 0., # 67.93m
        600: 1.92, # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 1.92, # 73.79m
    }

    table777 = {
        200: 0., # 63.73m
        300: 1.92, # 73.86m
    }

    table787 = {
        8: 0., # 56.72m
        9: 0., # 62.81m
        10: 0., # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot123(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0., # 48.51m-54.94m-61.37m
        319: -3.46, # 33.84m
        320: -3.46, # 37.57m
        321: -3.46, # 44.51m
        737: -3.46, # 31–43.8m
        190: -3.46, # 36.25m
        170: -3.46, # 29.90m
        175: -3.46, # 31.67m
        1008: -3.46, # 32.8m
        221: -3.46, # 35m
        223: -3.46, # 38.71m
        747: 0., # 70.7m/76.25m
        380: 0., # 72.72m
    }

    table330 = {
        200: 0., # 58.82m
        300: 0., # 63.66m
        800: 0., # 58.82m
        900: 0., # 63.66m
    }

    table340 = {
        200: 0., # 59.4m
        300: 0., # 63.69m
        500: 0., # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
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

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot151(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -5.06, # 48.51m-54.94m-61.37m
        319: -11.03, # 33.84m
        320: -11.03, # 37.57m
        321: -11.03, # 44.51m
        737: -11.03, # 31–43.8m
        190: -11.03, # 36.25m
        170: -11.03, # 29.90m
        175: -11.03, # 31.67m
        1008: -11.03, # 32.8m
        221: -11.03, # 35m
        223: -11.03, # 38.71m
        747: 0., # 70.7m/76.25m
        380: 0., # 72.72m
    }

    table330 = {
        200: -3.07, # 58.82m
        300: -1.05, # 63.66m
        800: -3.07, # 58.82m
        900: -1.05, # 63.66m
    }

    table340 = {
        200: -3.07, # 59.4m
        300: -1.05, # 63.69m
        500: -1.05, # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: -1.05, # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: -1.05, # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: -3.07, # 56.72m
        9: -1.05, # 62.81m
        10: -1.05, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

################
## T3 Terminal
@AlternativeStopPositions
def customOffset_Spot105(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -5.26, # 48.51m-54.94m-61.37m
        319: -15.31, # 33.84m
        320: -15.31, # 37.57m
        321: -15.31, # 44.51m
        # Should be -25.4, Changed to -15.31 for animation
        737: -15.31, # 31–43.8m
        190: -15.31, # 36.25m
        170: -15.31, # 29.90m
        175: -15.31, # 31.67m
        1008: -15.31, # 32.8m
        221: -15.31, # 35m
        223: -15.31, # 38.71m
        747: 0., # 70.7m/76.25m
        380: -2.35, # 72.72m
    }

    table330 = {
        200: -5.26, # 58.82m
        300: -3.02, # 63.66m
        800: -5.26, # 58.82m
        900: -3.02, # 63.66m
    }

    table340 = {
        200: -5.26, # 59.4m
        300: -3.02, # 63.69m
        500: -2.35, # 67.93m
        600: 0., # 75.36m (Changed from +2.04)
    }

    table350 = {
        900: -4., # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: -3.02, # 63.73m
        300: -2.35, # 73.86m (Changed from +2.04)
    }

    table787 = {
        8: -5.26, # 56.72m
        9: -3.02, # 62.81m
        10: -2.35, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot106(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -5.27, # 48.51m-54.94m-61.37m
        319: -9.26, # 33.84m
        320: -7.3, # 37.57m
        321: -7.3, # 44.51m
        737: -9.26, # 31–43.8m
        190: -9.26, # 36.25m
        170: -9.26, # 29.90m
        175: -9.26, # 31.67m
        1008: -9.26, # 32.8m
        221: -9.26, # 35m
        223: -9.26, # 38.71m
        747: -2.27, # 70.7m/76.25m
        380: -1.27, # 72.72m
    }

    table330 = {
        200: -3.99, # 58.82m
        300: -3.99, # 63.66m
        800: -3.99, # 58.82m
        900: -3.99, # 63.66m
    }

    table340 = {
        200: -3.99, # 59.4m
        300: -3.99, # 63.69m
        500: -3.99, # 67.93m
        600: -1.27, # 75.36m
    }

    table350 = {
        900: 0., # 66.8m (Changed from +3.1)
        1000: 0., # 73.79m (Changed from +3.1)
    }

    table777 = {
        200: -1.27, # 63.73m
        300: 0., # 73.86m (Changed from +3.1)
    }

    table787 = {
        8: -5.27, # 56.72m
        9: -5.27, # 62.81m
        10: -5.27, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot111(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -5.32, # 48.51m-54.94m-61.37m
        319: -21.24, # 33.84m
        320: -15.25, # 37.57m
        321: -15.25, # 44.51m
        737: -21.24, # 31–43.8m
        190: -21.24, # 36.25m
        170: -21.24, # 29.90m
        175: -21.24, # 31.67m
        1008: -21.24, # 32.8m
        221: -21.24, # 35m
        223: -21.24, # 38.71m
        747: 0, # 70.7m/76.25m
        380: 0, # 72.72m
    }

    table330 = {
        200: -5.32, # 58.82m
        300: -2.28, # 63.66m
        800: -5.32, # 58.82m
        900: -2.28, # 63.66m
    }

    table340 = {
        200: -5.32, # 59.4m
        300: -2.28, # 63.69m
        500: 0, # 67.93m
        600: 2.1, # 75.36m
    }

    table350 = {
        900: -4.07, # 66.8m
        1000: 0, # 73.79m
    }

    table777 = {
        200: -2.82, # 63.73m
        300: 2.1, # 73.86m
    }

    table787 = {
        8: -5.32, # 56.72m
        9: -5.32, # 62.81m
        10: -5.32, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot111SP(aircraftData):
    # Product of GSJP
    # Catering Animation
    mainTable = {
        0: 0.,
        767: -5.32, # 48.51m-54.94m-61.37m
        319: -15.25, # 33.84m
        320: -15.25, # 37.57m
        321: -15.25, # 44.51m
        737: -15.25, # 31–43.8m
        190: -15.25, # 36.25m
        170: -15.25, # 29.90m
        175: -15.25, # 31.67m
        1008: -15.25, # 32.8m
        221: -15.25, # 35m
        223: -15.25, # 38.71m
        747: 0, # 70.7m/76.25m
        380: 0, # 72.72m
    }

    table330 = {
        200: -5.32, # 58.82m
        300: -2.28, # 63.66m
        800: -5.32, # 58.82m
        900: -2.28, # 63.66m
    }

    table340 = {
        200: -5.32, # 59.4m
        300: -2.28, # 63.69m
        500: 0, # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: -4.07, # 66.8m
        1000: 0, # 73.79m
    }

    table777 = {
        200: -2.82, # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: -5.32, # 56.72m
        9: -5.32, # 62.81m
        10: -5.32, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot140(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: 0., # 48.51m-54.94m-61.37m
        319: -8.98, # 33.84m
        320: -7.90, # 37.57m
        321: -7.90, # 44.51m
        737: -8.98, # 31–43.8m
        190: -8.98, # 36.25m
        170: -8.98, # 29.90m
        175: -8.98, # 31.67m
        1008: -8.98, # 32.8m
        221: -8.98, # 35m
        223: -8.98, # 38.71m
        747: 0., # 70.7m/76.25m
        380: 0., # 72.72m
    }

    table330 = {
        200: 0., # 58.82m
        300: 0., # 63.66m
        800: 0., # 58.82m
        900: 0., # 63.66m
    }

    table340 = {
        200: 0., # 59.4m
        300: 0., # 63.69m
        500: 0., # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
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

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot145(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -4.11, # 48.51m-54.94m-61.37m
        319: -15.71, # 33.84m
        320: -10.01, # 37.57m
        321: -10.01, # 44.51m
        737: -15.71, # 31–43.8m
        190: -15.71, # 36.25m
        170: -15.71, # 29.90m
        175: -15.71, # 31.67m
        1008: -15.71, # 32.8m
        221: -15.71, # 35m
        223: -15.71, # 38.71m
        747: -1.08, # 70.7m/76.25m
        380: -1.08, # 72.72m
    }

    table330 = {
        200: -4.11, # 58.82m
        300: -2.06, # 63.66m
        800: -4.11, # 58.82m
        900: -2.06, # 63.66m
    }

    table340 = {
        200: -4.11, # 59.4m
        300: -2.06, # 63.69m
        500: 0., # 67.93m
        600: 1.85, # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: -4.11, # 63.73m
        300: 1.85, # 73.86m
    }

    table787 = {
        8: -4.11, # 56.72m
        9: -4.11, # 62.81m
        10: -4.11, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot145SP(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -4.11, # 48.51m-54.94m-61.37m
        319: -15.71, # 33.84m
        320: -10.01, # 37.57m
        321: -10.01, # 44.51m
        737: -15.71, # 31–43.8m
        190: -15.71, # 36.25m
        170: -15.71, # 29.90m
        175: -15.71, # 31.67m
        1008: -15.71, # 32.8m
        221: -15.71, # 35m
        223: -15.71, # 38.71m
        747: -1.08, # 70.7m/76.25m
        380: -1.08, # 72.72m
    }

    table330 = {
        200: -4.11, # 58.82m
        300: -2.06, # 63.66m
        800: -4.11, # 58.82m
        900: -2.06, # 63.66m
    }

    table340 = {
        200: -4.11, # 59.4m
        300: -2.06, # 63.69m
        500: 0., # 67.93m
        600: 0., # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: -4.11, # 63.73m
        300: 0., # 73.86m
    }

    table787 = {
        8: -4.11, # 56.72m
        9: -4.11, # 62.81m
        10: -4.11, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot149(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        767: -3.04, # 48.51m-54.94m-61.37m
        319: -14.25, # 33.84m
        320: -13.24, # 37.57m
        321: -13.24, # 44.51m
        737: -14.25, # 31–43.8m
        190: -14.25, # 36.25m
        170: -14.25, # 29.90m
        175: -14.25, # 31.67m
        1008: -14.25, # 32.8m
        221: -14.25, # 35m
        223: -14.25, # 38.71m
        747: 0., # 70.7m/76.25m
        380: 0., # 72.72m
    }

    table330 = {
        200: -3.04, # 58.82m
        300: -0.79, # 63.66m
        800: -3.04, # 58.82m
        900: -0.79, # 63.66m
    }

    table340 = {
        200: -3.04, # 59.4m
        300: -0.79, # 63.69m
        500: 0., # 67.93m
        600: 1.82, # 75.36m
    }

    table350 = {
        900: 0., # 66.8m
        1000: 0., # 73.79m
    }

    table777 = {
        200: -0.79, # 63.73m
        300: 1.82, # 73.86m
    }

    table787 = {
        8: -3.04, # 56.72m
        9: -3.04, # 62.81m
        10: -3.04, # 68.28m
    }

    if aircraftData.idMajor == 330:
        return Distance.fromMeters(table330.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 340:
        return Distance.fromMeters(table340.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 350:
        return Distance.fromMeters(table350.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
# Product of GSJP

parkings = {
    GATE :{
        None : (),
        # Terminal 1
        1 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SFJ]"), customOffset_Spot1),
        2 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SFJ]"), customOffset_Spot2),
        3 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SFJ/JAL/JTA]"), customOffset_Spot2),
        4 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot2),
        5 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot5),
        6 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_noOffset),
        7 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot7),
        8 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot8),
        9 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot9),
        10 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot9),
        11 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot11),
        12 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot12),
        13 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot12),
        14 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL/JTA]"), customOffset_Spot9),
        15 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL]"), customOffset_Spot9),
        16 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL]"), customOffset_Spot9),
        17 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL]"), customOffset_Spot17),
        18 : (CustomizedName("Gates-T1 Domestic|Spot #§ [JAL]"), customOffset_Spot18),
        19 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SKY]"), customOffset_noOffset),
        20 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SKY]"), customOffset_noOffset),
        21 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SKY/JAL]"), customOffset_Spot21),
        22 : (CustomizedName("Gates-T1 Domestic|Spot #§ [SKY]"), customOffset_Spot22),
        23 : (CustomizedName("Gates-T1 Domestic|[CLSD] Spot #§"), ),
        24 : (CustomizedName("Gates-T1 Domestic|[CLSD] Spot #§"), ),

        # Terminal 2
        53 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [SNA/ADO/ANA]"), customOffset_Spot53),
        54 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [SNA/ADO/ANA]"), customOffset_Spot54),
        55 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ADO/SNA/ANA]"), customOffset_Spot55),
        56 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ADO/SNA/ANA]"), customOffset_Spot56),
        57 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA/SNA/ADO]"), customOffset_Spot53),
        58 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot58),
        59 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        60 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        61 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        62 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        63 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        64 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        65 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA]"), customOffset_Spot65),
        66 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot66),
        67 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot71),
        68 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot68),
        69 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot69),
        70 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot70),
        71 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot71),
        72 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot73),
        73 : (CustomizedName("Gates-T2 (66-73) International|Spot #§ [ANA]"), customOffset_Spot73),

        # Terminal 3
        105 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot105),
        106 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot106),
        107 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        108 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        109 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        110 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        111 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111),
        112 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        113 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        114 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot111SP),
        140 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot140),
        141 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_noOffset),
        142 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145SP),
        143 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145),
        144 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145),
        145 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145),
        146 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145),
        147 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145),
        148 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot145),
        149 : (CustomizedName("Gates-T3 International|Spot #§ [INTL]"), customOffset_Spot149),

        # Terminal 2 Satellite
        406 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA/SNA]"), customOffset_Spot406),
        407 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA/SNA]"), customOffset_Spot406),
        408 : (CustomizedName("Gates-T2 (406-408, 50-65) Domestic|Spot #§ [ANA/SNA]"), customOffset_noOffset),

        # Terminal 2 Boarding Station
        503 : (CustomizedName("Gates-T2 (500s) Boarding Station|Spot #§ [ANA/SNA]"), customOffset_Spot503),
        504 : (CustomizedName("Gates-T2 (500s) Boarding Station|Spot #§ [ANA/SNA]"), customOffset_Spot503),
        506 : (CustomizedName("Gates-T2 (500s) Boarding Station|Spot #§ [ANA/SNA]"), customOffset_Spot506),
    },

    PARKING :{
        None : (),
        # Terminal 1 Okidome
        31 : (CustomizedName("Open Spots 31-41|[CLSD] Spot #§"), ),
        32 : (CustomizedName("Open Spots 31-41|[CLSD] Spot #§"), ),
        33 : (CustomizedName("Open Spots 31-41|[CLSD] Spot #§"), ),
        34 : (CustomizedName("Open Spots 31-41|Spot #§ [J-Air]"), customOffset_noOffset),
        35 : (CustomizedName("Open Spots 31-41|Spot #§ [J-Air]"), customOffset_noOffset),
        36 : (CustomizedName("Open Spots 31-41|Spot #§ [J-Air]"), customOffset_noOffset),
        37 : (CustomizedName("Open Spots 31-41|Spot #§ [JAL]"), customOffset_noOffset),
        38 : (CustomizedName("Open Spots 31-41|Spot #§ [JAL]"), customOffset_Spot38),
        39 : (CustomizedName("Open Spots 31-41|Spot #§ [JAL]"), customOffset_Spot38),
        40 : (CustomizedName("Open Spots 31-41|Spot #§ [JAL]"), customOffset_Spot38),
        41 : (CustomizedName("Open Spots 31-41|Spot #§ [JAL/SKY]"), customOffset_Spot38),

        # Terminal 2/East Side Okidome
        81 : (CustomizedName("Open Spots 81-84|Spot #§ [ANA]"), customOffset_Spot81),
        82 : (CustomizedName("Open Spots 81-84|Spot #§ [ANA]"), customOffset_Spot81),
        83 : (CustomizedName("Open Spots 81-84|Spot #§ [ANA]"), customOffset_Spot81),
        84 : (CustomizedName("Open Spots 81-84|Spot #§ [ANA]"), customOffset_Spot84),

        401 : (CustomizedName("Open Spots 400s|Spot #§ [ALL]"), customOffset_Spot401),
        402 : (CustomizedName("Open Spots 400s|Spot #§ [ALL]"), customOffset_Spot402),

        501 : (CustomizedName("Open Spots 500s|Spot #§ [SKY/ANA/SNA/ADO]"), customOffset_Spot501),
        502 : (CustomizedName("Open Spots 500s|Spot #§ [ANA/SNA/ADO]"), customOffset_Spot502),
        505 : (CustomizedName("Open Spots 500s|Spot #§ [ANA/SNA/ADO]"), customOffset_Spot505),
        507 : (CustomizedName("Open Spots 500s|Spot #§ [ANA/SNA/ADO]"), customOffset_Spot507),
        508 : (CustomizedName("Open Spots 500s|Spot #§ [ANA/SNA/ADO]"), customOffset_Spot507),
        509 : (CustomizedName("Open Spots 500s|Spot #§ [ANA/SNA/ADO]"), customOffset_Spot507),

        601 : (CustomizedName("Open Spots 600s|Spot #§ [SFJ/ANA/SNA]"), customOffset_Spot601),
        602 : (CustomizedName("Open Spots 600s|Spot #§ [SFJ/ANA/SNA]"), customOffset_Spot601),
        603 : (CustomizedName("Open Spots 600s|Spot #§ [SFJ/ANA/SNA]"), customOffset_Spot601),
        604 : (CustomizedName("Open Spots 600s|Spot #§ [ALL]"), customOffset_Spot604),
        605 : (CustomizedName("Open Spots 600s|Spot #§ [ALL]"), customOffset_Spot604),

        701 : (CustomizedName("Open Spots 700s|Spot #§ [ANA/ADO]"), customOffset_Spot701),
        702 : (CustomizedName("Open Spots 700s|Spot #§ [JAL]"), customOffset_Spot702),
        703 : (CustomizedName("Open Spots 700s|Spot #§ [JAL]"), customOffset_Spot702),
        704 : (CustomizedName("Open Spots 700s|Spot #§ [JAL]"), customOffset_Spot704),
        705 : (CustomizedName("Open Spots 700s|Spot #§ [JAL]"), customOffset_Spot705),
        706 : (CustomizedName("Parking Spots 700s|Spot #§ [ANA]"), customOffset_Spot706),
        707 : (CustomizedName("Parking Spots 700s|Spot #§ [ANA]"), customOffset_noOffset),
        708 : (CustomizedName("Parking Spots 700s|Spot #§ [ANA]"), customOffset_noOffset),
        709 : (CustomizedName("Parking Spots 700s|Spot #§ [ANA]"), customOffset_noOffset),
        710 : (CustomizedName("Parking Spots 700s|Spot #§ [ANA]"), customOffset_noOffset),
        711 : (CustomizedName("Parking Spots 700s|Spot #§ [JAL]"), customOffset_noOffset),
        712 : (CustomizedName("Parking Spots 700s|Spot #§ [ANA]"), customOffset_noOffset),

        801 : (CustomizedName("Open Spots 800s|Spot #§ [ANA]"), customOffset_Spot801),
        802 : (CustomizedName("Open Spots 800s|Spot #§ [JAL]"), customOffset_Spot802),
        803 : (CustomizedName("Open Spots 800s|Spot #§ [ANA]"), customOffset_Spot803),
        804 : (CustomizedName("Open Spots 800s|Spot #§ [ANA]"), customOffset_noOffset),
        805 : (CustomizedName("Open Spots 800s|Spot #§ [ANA]"), customOffset_Spot803),
        806 : (CustomizedName("Open Spots 800s|Spot #§ [JAL]"), customOffset_Spot806),
        807 : (CustomizedName("Open Spots 800s|Spot #§ [ANA]"), customOffset_Spot807),
        808 : (CustomizedName("Parking Spots 800s|Spot #§ [ANA]"), customOffset_noOffset),
        809 : (CustomizedName("Parking Spots 800s|Spot #§ [ANA]"), customOffset_noOffset),
        810 : (CustomizedName("Parking Spots 800s|Spot #§ [JAL]"), customOffset_noOffset),
        811 : (CustomizedName("Parking Spots 800s|Spot #§ [ANA]"), customOffset_noOffset),

        # Terminal 3 Okidome
        101 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot101),
        102 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot101),
        103 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot101),
        104 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot101),
        121 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot121),
        122 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot121),
        123 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_noOffset),
        124 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_noOffset),
        131 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot121),
        132 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot121),
        133 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_noOffset),
        134 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_noOffset),
        149 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_noOffset),
        151 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot151),
        152 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot151),
        153 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot151),
        154 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot151),
        155 : (CustomizedName("Open Spots 100s|Spot #§ [INTL]"), customOffset_Spot151),

        # RW22 Stands
        301 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        302 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        303 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        304 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        305 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        311 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        312 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        313 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        314 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        315 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        331 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        332 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        333 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        341 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        342 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        343 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        344 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        351 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        352 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        353 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        354 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        355 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        361 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        362 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        363 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        364 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        365 : (CustomizedName("Parking Spots 300s|Spot #§"), ),
        366 : (CustomizedName("Parking Spots 300s|Spot #§"), ),

        # N-Area
        901 : (CustomizedName("N-Area|Spot #§"), ),
        902 : (CustomizedName("N-Area|Spot #§"), ),
        903 : (CustomizedName("N-Area|Spot #§"), ),
        904 : (CustomizedName("N-Area|Spot #§"), ),
        905 : (CustomizedName("N-Area|Spot #§"), ),
        906 : (CustomizedName("N-Area|Spot #§"), ),
        907 : (CustomizedName("N-Area|Spot #§"), ),
        908 : (CustomizedName("N-Area|Spot #§"), ),
        909 : (CustomizedName("N-Area|Spot #§"), ),
        921 : (CustomizedName("N-Area|Spot #§"), ),
        922 : (CustomizedName("N-Area|Spot #§"), ),
        931 : (CustomizedName("N-Area|Spot #§"), ),
        932 : (CustomizedName("N-Area|Spot #§"), ),
        933 : (CustomizedName("N-Area|Spot #§"), ),
        934 : (CustomizedName("N-Area|Spot #§"), ),
        935 : (CustomizedName("N-Area|Spot #§"), ),
        941 : (CustomizedName("N-Area|Spot #§"), ),
        942 : (CustomizedName("N-Area|Spot #§"), ),
        943 : (CustomizedName("N-Area|Spot #§"), ),
        944 : (CustomizedName("N-Area|Spot #§"), ),
        951 : (CustomizedName("N-Area|Spot #§"), ),
        952 : (CustomizedName("N-Area|Spot #§"), ),
        953 : (CustomizedName("N-Area|Spot #§"), ),
        954 : (CustomizedName("N-Area|Spot #§"), ),
        955 : (CustomizedName("N-Area|Spot #§"), ),
        956 : (CustomizedName("N-Area|Spot #§"), ),
        957 : (CustomizedName("N-Area|Spot #§"), ),
        961 : (CustomizedName("N-Area|Spot #§"), ),
        962 : (CustomizedName("N-Area|Spot #§"), ),
        963 : (CustomizedName("N-Area|Spot #§"), ),
        964 : (CustomizedName("N-Area|Spot #§"), ),
        965 : (CustomizedName("N-Area|Spot #§"), ),
        966 : (CustomizedName("N-Area|Spot #§"), ),
        967 : (CustomizedName("N-Area|Spot #§"), ),
        968 : (CustomizedName("N-Area|Spot #§"), ),
        969 : (CustomizedName("N-Area|Spot #§"), ),
        981 : (CustomizedName("N-Area|Spot #§"), ),
        982 : (CustomizedName("N-Area|Spot #§"), ),
        983 : (CustomizedName("N-Area|Spot #§"), ),
        984 : (CustomizedName("N-Area|Spot #§"), ),
        985 : (CustomizedName("N-Area|Spot #§"), ),
        991 : (CustomizedName("N-Area|Spot #§"), ),
        992 : (CustomizedName("N-Area|Spot #§"), ),
        993 : (CustomizedName("N-Area|Spot #§"), ),
        994 : (CustomizedName("N-Area|Spot #§"), ),

        # Hangar
        201 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [ANA]"), ),
        202 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [ANA]"), ),
        203 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [ANA]"), ),
        204 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [ANA]"), ),
        205 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [ANA]"), ),
        206 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [SKY]"), ),
        207 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [SKY]"), ),
        208 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [SKY]"), ),
        209 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [JAL]"), ),
        210 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [JAL]"), ),
        211 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [JAL]"), ),
        212 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [JAL]"), ),
        213 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [JAL]"), ),
        214 : (CustomizedName("Shin-Seibijo Hangars|Spot #§ [JAL]"), ),

        # Washing Spots
        2 : (CustomizedName("Washing Spots|Spot WA2"), ),
        3 : (CustomizedName("Washing Spots|Spot WA3"), ),
    }, 

    GATE_V : {
        None : (),
        # Terminal 1 Okidome
        1 : (CustomizedName("Open VIP Spots|[CLSD] Spot #§"), ),
        2 : (CustomizedName("Open VIP Spots|[CLSD] Spot #§"), ),
        0 : (CustomizedName("Open VIP Spots|Spot V#§ [ALL]"), customOffset_SpotVS),
    }
}
