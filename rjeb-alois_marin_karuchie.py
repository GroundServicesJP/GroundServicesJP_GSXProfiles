msfs_mode = 1

@AlternativeStopPositions
def customOffset_zero(aircraftData):
    return Distance.fromMeters(0.)

parkings = {
    0 :{
        None : (),
        1 : (CustomizedName("Apron|Spot #§"), customOffset_zero),
        2 : (CustomizedName("Apron|Spot #§"), customOffset_zero),
        3 : (CustomizedName("Apron|Spot #§ [ANA]"), customOffset_zero),
        4 : (CustomizedName("GA Parking|#§"), ),
        5 : (CustomizedName("GA Parking|#§"), ),
        6 : (CustomizedName("GA Parking|#§"), ),
        7 : (CustomizedName("GA Parking|#§"), ),
    }
}