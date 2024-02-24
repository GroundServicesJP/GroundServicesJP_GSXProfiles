msfs_mode = 1

@AlternativeStopPositions
def customOffset_zero(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot9(aircraftData):
    myTable = {
        0: 26.,
        1008: 0.,
    }
    # If not in my table, set to 20m displacement
    if myTable.get(aircraftData.idMajor) == None:
        return Distance.fromMeters(21.)
    return Distance.fromMeters( myTable.get(aircraftData.idMajor) )

parkings = {
    GATE : {
        None : (),
        2 : (CustomizedName("Apron Stand|Spot #§"), customOffset_zero),
        5 : (CustomizedName("Apron Gate|Spot #§ [ANA/SNA/APJ]"), customOffset_zero),
        6 : (CustomizedName("Apron Gate|Spot #§ [ANA/SNA/APJ]"), customOffset_zero),
        7 : (CustomizedName("Apron Gate|Spot #§ [JAL/JTA]"),customOffset_zero ),
        8 : (CustomizedName("Apron Gate|Spot #§ [JAL/JTA]"), customOffset_zero),
        9 : (CustomizedName("Apron Spot 9|Spot #§ [RAC/INTL]"), customOffset_Spot9),
    },
    0 : {
        None : (),
        10 : (CustomizedName("Apron Stand|Spot #§"), customOffset_zero),
    }
}