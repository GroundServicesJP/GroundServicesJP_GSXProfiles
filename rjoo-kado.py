msfs_mode = 1
version = 1.3

## No offset
@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot0(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -7.10,
        190: -7.10,
        175: -7.10,
        170: -7.10,
        42: -7.10,
        72: -7.10,
        1008: -7.10,
        200: -7.10,
        700: -7.10,
        900: -7.10,
        1000: -7.10,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -3.16,
        190: -3.16,
        175: -3.16,
        170: -3.16,
        42: -3.16,
        72: -3.16,
        1008: -3.16,
        200: -3.16,
        700: -3.16,
        900: -3.16,
        1000: -3.16,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot5(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -5.07,
        320: -5.95,
        321: -5.95,
        737: -5.95,
        # ERJ
        195: -5.95, #Original: -20.55
        190: -5.95, #Original: -20.55
        175: -5.95, #Original: -20.55
        170: -5.95, #Original: -20.55
        # ATR
        42: -20.55,
        72: -20.55,
        # Q400
        1008: -20.55,
        # CRJ
        200: -20.55,
        700: -20.55,
        900: -20.55,
        1000: -20.55,
    }

    table777 = {
        200: -5.07,
        300: 0.,
    }

    table787 = {
        8: -5.07,
        9: -5.07,
        10: -5.07,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot6(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        320: -7.98,
        321: -7.98,
        737: -7.98,
        # ERJ
        195: -9.02,
        190: -9.02,
        175: -9.02,
        170: -9.02,
        # ATR
        42: -9.02,
        72: -9.02,
        # Q400
        1008: -9.02,
        # CRJ
        200: -9.02,
        700: -9.02,
        900: -9.02,
        1000: -9.02,
    }

    table777 = {
        200: -7.98,
        300: 0.,
    }

    table787 = {
        8: -7.98,
        9: -7.98,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot7(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -1.82,
        320: -1.82,
        321: -1.82,
        737: -1.82,
        # ERJ
        195: -1.82, # Original:-17.11
        190: -1.82, # Original:-17.11
        175: -1.82, # Original:-17.11
        170: -1.82, # Original:-17.11
        # ATR
        42: -17.11,
        72: -17.11,
        # Q400
        1008: -17.11,
        # CRJ
        200: -17.11,
        700: -17.11,
        900: -17.11,
        1000: -17.11,
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
def customOffset_Spot8(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -0.68,
        320: -0.68,
        321: -0.68,
        737: -0.68,
        # ERJ
        195: -0.68, #Original:-8.14
        190: -0.68, #Original:-8.14
        175: -0.68, #Original:-8.14
        170: -0.68, #Original:-8.14
        # ATR
        42: -8.14,
        72: -8.14,
        # Q400
        1008: -8.14,
        # CRJ
        200: -8.14,
        700: -8.14,
        900: -8.14,
        1000: -8.14,
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
def customOffset_Spot9(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -0.94,
        767: -7.69,
        320: -7.69, #Original:-18.30
        321: -7.69, #Original:-18.30
        737: -7.69, #Original:-18.30
        # ERJ
        195: -7.69, #Original:-18.30
        190: -7.69, #Original:-18.30
        175: -7.69, #Original:-18.30
        170: -7.69, #Original:-18.30
        # ATR
        42: -18.30,
        72: -18.30,
        # Q400
        1008: -18.30,
        # CRJ
        200: -18.30,
        700: -18.30,
        900: -18.30,
        1000: -18.30,
    }

    table777 = {
        200: -0.94,
        300: 0.,
    }

    table787 = {
        8: -0.94,
        9: -0.94,
        10: -0.94,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))
    
@AlternativeStopPositions
def customOffset_Spot10(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -5.76,
        320: -10.51,
        321: -10.51,
        737: -10.51,
        # ERJ
        195: -10.51,
        190: -10.51,
        175: -10.51,
        170: -10.51,
        # ATR
        42: -10.51,
        72: -10.51,
        # Q400
        1008: -10.51,
        # CRJ
        200: -10.51,
        700: -10.51,
        900: -10.51,
        1000: -10.51,
    }

    table777 = {
        200: -5.76,
        300: 0.,
    }

    table787 = {
        8: -5.76,
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
def customOffset_Spot11(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: 0.,
        320: -10.45,
        321: -10.45,
        737: -10.45,
        # ERJ
        195: -10.45,
        190: -10.45,
        175: -10.45,
        170: -10.45,
        # ATR
        42: -10.45,
        72: -10.45,
        # Q400
        1008: -10.45,
        # CRJ
        200: -10.45,
        700: -10.45,
        900: -10.45,
        1000: -10.45,
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
def customOffset_Spot12(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: -5.76,
        321: -5.76,
        737: -5.76,
        195: -10.51,
        190: -10.51,
        175: -10.51,
        170: -10.51,
        42: -10.51,
        72: -10.51,
        1008: -10.51,
        200: -10.51,
        700: -10.51,
        900: -10.51,
        1000: -10.51,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot13(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -1.7,
        767: -1.7,
        320: -11.86,
        321: -11.86,
        737: -11.86,
        # ERJ
        195: -11.86, # Original:-25.35
        190: -11.86, # Original:-25.35
        175: -11.86, # Original:-25.35
        170: -11.86, # Original:-25.35
        # ATR
        42: -25.35,
        72: -25.35,
        # Q400
        1008: -25.35,
        # CRJ
        200: -25.35,
        700: -25.35,
        900: -25.35,
        1000: -25.35,
    }

    table777 = {
        200: -1.7,
        300: 0.,
    }

    table787 = {
        8: -4.14,
        9: -4.14,
        10: -4.14,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot14(aircraftData):
    # Product of GSJP
    mainTable = {
        0: -1.36,
        350: -1.36,
        767: -6.24,
        320: -7.54, # Original:-17.30
        321: -7.54, # Original:-17.30
        737: -7.54, # Original:-17.30
        # ERJ
        195: -7.54, # Original:-17.30
        190: -7.54, # Original:-17.30
        175: -7.54, # Original:-17.30
        170: -7.54, # Original:-17.30
        # ATR
        42: -17.30,
        72: -17.30,
        # Q400
        1008: -17.30,
        # CRJ
        200: -17.30,
        700: -17.30,
        900: -17.30,
        1000: -17.30,
    }

    table777 = {
        200: -6.24,
        300: -1.36,
    }

    table787 = {
        8: -6.24,
        9: -6.24,
        10: -6.24,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot15(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -5.02,
        767: -5.02,
        320: -9.77,
        321: -9.77,
        737: -9.77,
        # ERJ
        195: -9.77,
        190: -9.77,
        175: -9.77,
        170: -9.77,
        # ATR
        42: -9.77,
        72: -9.77,
        # Q400
        1008: -9.77,
        # CRJ
        200: -9.77,
        700: -9.77,
        900: -9.77,
        1000: -9.77,
    }

    table777 = {
        200: -5.02,
        300: 0.,
    }

    table787 = {
        8: -5.02,
        9: -5.02,
        10: -5.02,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot16(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -2.06,
        190: -2.06,
        175: -2.06,
        170: -2.06,
        42: -2.06,
        72: -2.06,
        1008: -2.06,
        200: -2.06,
        700: -2.06,
        900: -2.06,
        1000: -2.06,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot17(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -2.27,
        767: -9.05,
        320: -9.05,
        321: -9.05,
        737: -9.05,
        # ERJ
        195: -9.05,
        190: -9.05,
        175: -9.05,
        170: -9.05,
        # ATR
        42: -9.05,
        72: -9.05,
        # Q400
        1008: -9.05,
        # CRJ
        200: -9.05,
        700: -9.05,
        900: -9.05,
        1000: -9.05,
    }

    table777 = {
        200: -2.27,
        300: 0.,
    }

    table787 = {
        8: -6.07,
        9: -6.07,
        10: -6.07,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot18(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: -3.11,
        767: -5.06,
        320: -6.98,
        321: -6.98,
        737: -6.98,
        # ERJ
        195: -6.98,
        190: -6.98,
        175: -6.98,
        170: -6.98,
        # ATR
        42: -6.98,
        72: -6.98,
        # Q400
        1008: -6.98,
        # CRJ
        200: -6.98,
        700: -6.98,
        900: -6.98,
        1000: -6.98,
    }

    table777 = {
        200: -5.06,
        300: 0.,
    }

    table787 = {
        8: -3.11,
        9: -3.11,
        10: -3.11,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot19(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        350: 0.,
        767: -9.85,
        320: -11.6,
        321: -11.6,
        737: -11.6,
        # ERJ
        195: -11.6,
        190: -11.6,
        175: -11.6,
        170: -11.6,
        # ATR
        42: -20.34,
        72: -20.34,
        # Q400
        1008: -20.34,
        # CRJ
        200: -20.34,
        700: -20.34,
        900: -20.34,
        1000: -20.34,
    }

    table777 = {
        200: -4.92,
        300: 0.,
    }

    table787 = {
        8: -9.85,
        9: -4.92,
        10: 0.,
    }

    if aircraftData.idMajor == 777:
        return Distance.fromMeters(table777.get(aircraftData.idMinor,0))
    elif aircraftData.idMajor == 787:
        return Distance.fromMeters(table787.get(aircraftData.idMinor,0))
    else:
        return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot20(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -2.96,
        190: -2.96,
        175: -2.96,
        170: -2.96,
        42: -8.83,
        72: -8.83,
        1008: -8.83,
        200: -8.83,
        700: -8.83,
        900: -8.83,
        1000: -8.83,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot21(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -1.92,
        190: -1.92,
        175: -1.92,
        170: -1.92,
        42: -7.5, # Original:-4.18
        72: -7.5, # Original:-4.18
        1008: -7.5, # Original:-4.18
        200: -7.5, # Original:-4.18
        700: -7.5, # Original:-4.18
        900: -7.5, # Original:-4.18
        1000: -7.5, # Original:-4.18
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot22(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -6.82,
        190: -6.82,
        175: -6.82,
        170: -6.82,
        42: -6.82,
        72: -6.82,
        1008: -6.82,
        200: -6.82,
        700: -6.82,
        900: -6.82,
        1000: -6.82,
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot23(aircraftData):
    # Product of GSJP
    mainTable = {
        0: 0.,
        320: 0.,
        321: 0.,
        737: 0.,
        195: -2.53,
        190: -2.53,
        175: -2.53,
        170: -2.53,
        42: -24., # Original:-11.46
        72: -24., # Original:-11.46
        1008: -24., # Original:-11.46
        200: -24., # Original:-11.46
        700: -24., # Original:-11.46
        900: -24., # Original:-11.46
        1000: -24., # Original:-11.46
    }
    return Distance.fromMeters(mainTable.get(aircraftData.idMajor,0))

@AlternativeStopPositions
def customOffset_Spot24(aircraftData):
    return Distance.fromMeters(-7.60)

parkings = {
    GATE : {
        None : (),
        4 : (CustomizedName("Apron 1 Gate (4A-7)|SPOT 4A [ANA/IBEX]"), customOffset_noOffset),
        5 : (CustomizedName("Apron 1 Gate (4A-7)|SPOT 5 [ANA]"), customOffset_Spot5),
        6 : (CustomizedName("Apron 1 Gate (4A-7)|SPOT 6 [ANA]"), customOffset_Spot6),
        7 : (CustomizedName("Apron 1 Gate (4A-7)|SPOT 7 [ANA]"), customOffset_Spot7),
        8 : (CustomizedName("Apron 2 Gate (8-11)|SPOT 8 [ANA]"), customOffset_Spot8),
        9 : (CustomizedName("Apron 2 Gate (8-11)|SPOT 9 [ANA]"), customOffset_Spot9),
        11 : (CustomizedName("Apron 2 Gate (8-11)|SPOT 11 [ANA]"), customOffset_Spot11),
        12 : (CustomizedName("Apron 3 Gate (12-15)|SPOT 12 [ANA]"), customOffset_Spot12),
        13 : (CustomizedName("Apron 3 Gate (12-15)|SPOT 13 [ANA]"), customOffset_Spot13),
        14 : (CustomizedName("Apron 3 Gate (12-15)|SPOT 14 [JAL/J-AIR]"), customOffset_Spot14),
        15 : (CustomizedName("Apron 3 Gate (12-15)|SPOT 15 [JAL/J-AIR]"), customOffset_Spot15),
        16 : (CustomizedName("Apron 4 Gate (16-19)|SPOT 16 [JAL/J-AIR]"), customOffset_Spot16),
        17 : (CustomizedName("Apron 4 Gate (16-19)|SPOT 17 [JAL/J-AIR]"), customOffset_Spot17),
        19 : (CustomizedName("Apron 4 Gate (16-19)|SPOT 19 [JAL/J-AIR]"), customOffset_Spot19),
        20 : (CustomizedName("Apron 5 Gate (20-23)|SPOT 20 [JAL/J-AIR]"), customOffset_Spot20),
        21 : (CustomizedName("Apron 5 Gate (20-23)|SPOT 21 [JAL/J-AIR]"), customOffset_Spot21),
        22 : (CustomizedName("Apron 5 Gate (20-23)|SPOT 22 [JAL/J-AIR]"), customOffset_Spot22),
        23 : (CustomizedName("Apron 5 Gate (20-23)|SPOT 23 [J-AIR/AMX/JAC]"), customOffset_Spot23),
    },
    PARKING : {
        None : (),
        0 : (CustomizedName("Apron 1 Stand (0-4)|SPOT #§ [ANA/IBEX]"), customOffset_Spot0),
        1 : (CustomizedName("Apron 1 Stand (0-4)|SPOT #§ [ANA/IBEX]"), customOffset_noOffset),
        2 : (CustomizedName("Apron 1 Stand (0-4)|SPOT #§ [ANA/IBEX]"), customOffset_noOffset),
        3 : (CustomizedName("Apron 1 Stand (0-4)|SPOT #§ [ANA/IBEX]"), customOffset_noOffset),
        4 : (CustomizedName("Apron 1 Stand (0-4)|SPOT #§ [ANA/IBEX]"), customOffset_noOffset),
        18 : (CustomizedName("Apron 4 Gate (16-19)|SPOT 18 [JAL/J-AIR]"), customOffset_Spot18),
        24 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 24 [J-AIR/JAC]"), customOffset_Spot24),
        25 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 25 [J-AIR/JAC]"), customOffset_noOffset),
        26 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 26 [J-AIR/JAC]"), customOffset_noOffset),
        27 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 27 [J-AIR/JAC]"), customOffset_noOffset),
        41 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 41 [J-AIR]"), customOffset_noOffset),
        42 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 42 [J-AIR]"), customOffset_noOffset),
        43 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 43 [BROKEN]"), ),
        44 : (CustomizedName("Apron 5 Stand (24-27, 41-44)|SPOT 44 [BROKEN]"), ),
        45 : (CustomizedName("Apron 6 Stand (45-53)|SPOT #§ [J-AIR/JAC]"), customOffset_noOffset),
        46 : (CustomizedName("Apron 6 Stand (45-53)|SPOT 46 [J-AIR/JAC]"), customOffset_noOffset),
        47 : (CustomizedName("Apron 6 Stand (45-53)|SPOT 47 [J-AIR/JAC]"), customOffset_noOffset),
        48 : (CustomizedName("Apron 6 Stand (45-53)|SPOT 48 [J-AIR/JAC]"), customOffset_noOffset),
        51 : (CustomizedName("Apron 6 Stand (45-53)|SPOT #§"), ),
        52 : (CustomizedName("Apron 6 Stand (45-53)|SPOT #§"), ),
        53 : (CustomizedName("Apron 6 Stand (45-53)|SPOT #§"), ),
        70 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        71 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        72 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        73 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        74 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        75 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        76 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        77 : (CustomizedName("Apron 7 Stand (70s)|SPOT #§"), ),
        80 : (CustomizedName("Apron 8 Stand (80s)|SPOT #§"), ),
        81 : (CustomizedName("Apron 8 Stand (80s)|SPOT #§"), ),
        82 : (CustomizedName("Apron 8 Stand (80s)|SPOT #§"), ),
        83 : (CustomizedName("Apron 8 Stand (80s)|SPOT #§"), ),
        84 : (CustomizedName("Apron 8 Stand (80s)|SPOT #§"), ),
    },
    0 : {
        None : (),
        10 : (CustomizedName("Apron 2 Gate (8-11)|SPOT 10 [ANA]"), customOffset_Spot10),
    }
}