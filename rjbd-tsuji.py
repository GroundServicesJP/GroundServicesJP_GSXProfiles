# -- coding: utf-8 --

# Copyright (C) 2025 GroundServicesJP (Rokumaru)
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

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

parkings = {
    GATE : {
        None : (),
        1 : (CustomizedName("Apron (South)|SPOT #§"), customOffset_noOffset),
        2 : (CustomizedName("Apron (South)|SPOT # {Gate}§"), customOffset_noOffset),
        3 : (CustomizedName("Apron (South)|SPOT #§"), customOffset_noOffset),
    }, 

    N_PARKING : {
        None : (),
        1 : (CustomizedName("North Apron|1"), ),
        2 : (CustomizedName("North Apron|2"), ),
        3 : (CustomizedName("North Apron|3"), ),
        4 : (CustomizedName("North Apron|4"), ),

        6: (CustomizedName("North Apron|A"), ),
        8: (CustomizedName("North Apron|C"), ),
    }, 

    S_PARKING : {
        None : (),
        1 : (CustomizedName("South Apron (GA)|A"), ),
        2 : (CustomizedName("South Apron (GA)|B"), ),
        4 : (CustomizedName("South Apron (GA)|D"), ),
        5 : (CustomizedName("South Apron (GA)|E"), ),

        6: (CustomizedName("South Apron (GA)|F"), ),
        7: (CustomizedName("South Apron (GA)|G"), ),
        8: (CustomizedName("South Apron (GA)|H"), ),
        9: (CustomizedName("South Apron (GA)|I"), ),
        10: (CustomizedName("South Apron (GA)|J"), ),
    }, 
}