# -- coding: utf-8 --

# Copyright (C) 2025 GroundServicesJP
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
version = 1.0

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot1221(aircraftData):
    exempt_aircraft = {"B788", "B762", "B763"}

    t_stop = 0
    first_stop =  -10.5 #m

    if (aircraftData.aircraftGroup in {"ARC-A", "ARC-B", "ARC-C"}) or (aircraftData.icaoTypeDesignator in exempt_aircraft):
        return Distance.fromMeters(first_stop)
    return Distance.fromMeters(t_stop)

@AlternativeStopPositions
def customOffset_Spot22(aircraftData):
    exempt_aircraft = {"B788", "B762", "B763"}

    t_stop = 0
    first_stop =  -4.84 #m
    second_stop = -23.08 #m

    if (aircraftData.aircraftGroup in {"ARC-C"}) or (aircraftData.icaoTypeDesignator in exempt_aircraft):
        return Distance.fromMeters(first_stop)
    elif (aircraftData.aircraftGroup in {"ARC-A", "ARC-B"}):
        return Distance.fromMeters(second_stop)
    return Distance.fromMeters(t_stop)

parkings = {
    GATE : {
        None : (),
        10 : (CustomizedName("West Apron Stands|SPOT #§", 2), customOffset_noOffset),
        11 : (CustomizedName("West Apron Stands|SPOT #§", 2), customOffset_noOffset),
        12 : (CustomizedName("West Apron Gates|SPOT #§ [INTL]", 1), customOffset_Spot1221),
        21 : (CustomizedName("West Apron Gates|SPOT #§ [INTL/Domestic]", 1), customOffset_Spot1221),
        22 : (CustomizedName("West Apron Gates|SPOT #§ [Domestic]", 1), customOffset_Spot22),
    }, 

    GATE_H :{
        None : (),
        1 : (CustomizedName("Saga Pref. Disaster Prevention Apron|8", 4), customOffset_noOffset),
    },

    PARKING : {
        None : (),
        1 : (CustomizedName("East Apron (General Aviation)|SPOT #§", 3), ),
        2 : (CustomizedName("East Apron (General Aviation)|SPOT #§", 3), ),
        3 : (CustomizedName("East Apron (General Aviation)|SPOT #§", 3), ),
        4 : (CustomizedName("East Apron (General Aviation)|SPOT #§", 3), ),
    }
}