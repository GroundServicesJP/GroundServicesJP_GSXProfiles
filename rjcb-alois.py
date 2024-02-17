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