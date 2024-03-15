msfs_mode = 1
icao="rjot"

@AlternativeStopPositions
def customOffsetGate_0(aircraftData):
    return Distance.fromMeters(0)

@AlternativeStopPositions
def customOffsetGate_2(aircraftData):
    table = {
        0: 0,
        319: -5.60,
        320: -5.60,
        321: -5.60,
        737: -5.60,
    }
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)

@AlternativeStopPositions
def customOffsetGate_3(aircraftData):
    table = {
        0: 0,
        319: -7.85,
        320: -7.85,
        321: -7.85,
        737: -7.85,
    }
    table_787 = {
        8: -1.80,
        9: 0,
        10: 0,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(table_787.get(aircraftData.idMajor))
    else:
        try:
            return Distance.fromMeters(table.get(aircraftData.idMajor))
        except:
            return Distance.fromMeters(0)

@AlternativeStopPositions
def customOffsetGate_5_6(aircraftData):
    table = {
        0: 0,
        319: -3.40,
        320: -3.40,
        321: -3.40,
        737: -3.40,
    }
    try:
        return Distance.fromMeters(table.get(aircraftData.idMajor))
    except:
        return Distance.fromMeters(0)

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("TMNL GATE 2"), customOffsetGate_2),
        3 : (CustomizedName("TMNL GATE 3"), customOffsetGate_3),
        5 : (CustomizedName("TMNL GATE 5"), customOffsetGate_5_6),
        6 : (CustomizedName("TMNL GATE 6"), customOffsetGate_5_6),
    },
    PARKING : {
        None : (),
        1 : (CustomizedName("TMNL PARKING 1"), customOffsetGate_0),
        7 : (CustomizedName("TMNL PARKING 7"), customOffsetGate_0),
        12 : (CustomizedName("GA PARKING C"), customOffsetGate_0),
        13 : (CustomizedName("GA PARKING E"), customOffsetGate_0),
        14 : (CustomizedName("GA PARKING G"), customOffsetGate_0),
        15 : (CustomizedName("GA PARKING F"), customOffsetGate_0),
        16 : (CustomizedName("GA PARKING D"), customOffsetGate_0),
        18 : (CustomizedName("GA PARKING K"), customOffsetGate_0),
        19 : (CustomizedName("GA PARKING J"), customOffsetGate_0),
        20 : (CustomizedName("GA PARKING L"), customOffsetGate_0),
        21 : (CustomizedName("GA PARKING M"), customOffsetGate_0),
        22 : (CustomizedName("GA PARKING N"), customOffsetGate_0),
        23 : (CustomizedName("GA PARKING O"), customOffsetGate_0),
        24 : (CustomizedName("GA PARKING P"), customOffsetGate_0),
        31 : (CustomizedName("GA PARKING W"), customOffsetGate_0),
        32 : (CustomizedName("GA PARKING X"), customOffsetGate_0),
        33 : (CustomizedName("GA PARKING Y"), customOffsetGate_0),
        34 : (CustomizedName("GA PARKING Z"), customOffsetGate_0),
        35 : (CustomizedName("GA PARKING B"), customOffsetGate_0),
        36 : (CustomizedName("GA PARKING A"), customOffsetGate_0),
    },
}