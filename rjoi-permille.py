# -- coding: utf-8 --

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

msfs_mode = 1
version = 1.1

@AlternativeStopPositions
def customOffset_noOffset(aircraftData):
    return Distance.fromMeters(0.)

@AlternativeStopPositions
def customOffset_Spot1(aircraftData):
    return Distance.fromMeters(-5.5)

parkings = {
    GATE : {
        None : (),
        1 : (CustomizedName("Civil Apron|SPOT #§"), customOffset_Spot1),
        2 : (CustomizedName("Civil Apron|SPOT #§"), customOffset_noOffset),
    },
    E_PARKING : {
        None : (CustomizedName("{MIL} MAG RAMP|#§"), ),
    },
    NE_PARKING : {
        None : (CustomizedName("{MIL}-AFDS|#§"), ),
    },
    N_PARKING : {
        None : (CustomizedName("{MIL} TAC VAL/CVW-5 RAMP|#§"), ),
    },
    SE_PARKING : {
        None : (CustomizedName("{MIL} JSDF-M EAST|#§"), ),
    },
    SW_PARKING : {
        None : (CustomizedName("{MIL} VMGR RAMP|#§"), ),
    },
    W_PARKING : {
        None : (CustomizedName("{MIL} VISITING ACFT LINE|#§"), ),
    },
    S_PARKING : {
        None : (CustomizedName("{MIL} CALA|#§"), ),
        0 : (CustomizedName("{MIL} N/S CLBR LINES|#§"), ),
    }
}