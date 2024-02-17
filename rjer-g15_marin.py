msfs_mode = 1

@AlternativeStopPositions
def customOffset_RJER(aircraftData):
    myTable = {
        0: 0.,
        42: -0.8,
        737: 0.,
    }
    return Distance.fromMeters( myTable.get(aircraftData.idMajor) )

parkings = {
    PARKING :{
        None : (),
        1 : (CustomizedName("Apron|Spot #§"), customOffset_RJER),
        2 : (CustomizedName("Apron|Spot #§ [ANA/HAC]"), customOffset_RJER),
        3 : (CustomizedName("Apron|Spot #§"), ),
        5 : (CustomizedName("Apron|Spot #§"), ),
    }
}