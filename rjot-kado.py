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
        9: 0.,
        10: 0.,
    }
    if aircraftData.idMajor == 787:
        return Distance.fromMeters(table_787.get(aircraftData.idMinor, 0))
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
        2 : (CustomizedName("Apron Gate|Spot 2 [JAL]"), customOffsetGate_2),
        3 : (CustomizedName("Apron Gate|Spot 3 [ANA/JJP]"), customOffsetGate_3),
        5 : (CustomizedName("Apron Gate|Spot 5 [ANA/JJP/INTL]"), customOffsetGate_5_6),
        6 : (CustomizedName("Apron Gate|Spot 6 [ANA/INTL]"), customOffsetGate_5_6),
    },
    PARKING : {
        None : (),
        1 : (CustomizedName("Apron Stand|Spot 1"), customOffsetGate_0),
        7 : (CustomizedName("Apron Stand|Spot 7"), customOffsetGate_0),
        12 : (CustomizedName("East Apron|C"), customOffsetGate_0),
        13 : (CustomizedName("East Apron|E"), customOffsetGate_0),
        14 : (CustomizedName("East Apron|G"), customOffsetGate_0),
        15 : (CustomizedName("East Apron|F"), customOffsetGate_0),
        16 : (CustomizedName("East Apron|D"), customOffsetGate_0),
        18 : (CustomizedName("East Apron|K"), customOffsetGate_0),
        19 : (CustomizedName("East Apron|J"), customOffsetGate_0),
        20 : (CustomizedName("East Apron|L"), customOffsetGate_0),
        21 : (CustomizedName("East Apron|M"), customOffsetGate_0),
        22 : (CustomizedName("East Apron|N"), customOffsetGate_0),
        23 : (CustomizedName("East Apron|O"), customOffsetGate_0),
        24 : (CustomizedName("East Apron|P"), customOffsetGate_0),
        31 : (CustomizedName("West Apron|W"), customOffsetGate_0),
        32 : (CustomizedName("West Apron|X"), customOffsetGate_0),
        33 : (CustomizedName("West Apron|Y"), customOffsetGate_0),
        34 : (CustomizedName("West Apron|Z"), customOffsetGate_0),
        35 : (CustomizedName("East Apron|B"), customOffsetGate_0),
        36 : (CustomizedName("East Apron|A"), customOffsetGate_0),
    },
}