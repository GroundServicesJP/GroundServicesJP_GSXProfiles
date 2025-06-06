msfs_mode = 1

@AlternativeStopPositions
def customOffset_0offset(aircraftData):
    return Distance.fromMeters(0.)

parkings = {
    GATE :{
        None : (),
        1 : (CustomizedName("Apron Gate|Spot #§ [INTL]"), customOffset_0offset),
        2 : (CustomizedName("Apron Gate|Spot #§ [INTL]"), customOffset_0offset),
        3 : (CustomizedName("Apron Gate|Spot #§ [JAL/ANA/AKX/FDA]"), customOffset_0offset),
        4 : (CustomizedName("Apron Gate|Spot #§ [JAL/ANA/AKX/FDA]"), customOffset_0offset),
        5 : (CustomizedName("Apron Gate|Spot #§ [JAL]"), customOffset_0offset),

    },
    PARKING :{
        None : (),
        6 : (CustomizedName("Apron Stand|Spot #§"), customOffset_0offset),
        1 : (CustomizedName("N Apron|Spot #§"), ),
        2 : (CustomizedName("N Apron|Spot #§"), ),
        3 : (CustomizedName("N Apron|Spot #§"), ),
        4 : (CustomizedName("N Apron|Spot #§"), ),
        5 : (CustomizedName("N Apron|Spot #§"), ),
        7 : (CustomizedName("N Apron|Spot #§"), ),
        8 : (CustomizedName("N Apron|Spot #§"), ),
        9 : (CustomizedName("N Apron|Spot #§"), ),
        10 : (CustomizedName("N Apron|Spot #§"), ),
        11 : (CustomizedName("N Apron|Spot #§"), ),
        12 : (CustomizedName("N Apron|Spot #§"), ),
        13 : (CustomizedName("N Apron|Spot #§"), ),
        14 : (CustomizedName("N Apron|Spot #§"), ),
        15 : (CustomizedName("N Apron|Spot #§"), ),
    }
}