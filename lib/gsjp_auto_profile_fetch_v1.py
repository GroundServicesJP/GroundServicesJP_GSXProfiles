# -- coding: utf-8 --

# Copyright (C) 2026 GroundServicesJP
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

########################################################################

# Shared Library for GroundServicesJP Handlers
# Auto GSX Profile (ini/py) Fetch
# version =  1.0

def checkIfNeedAutoFetchProfile(self, INI_PROFILE_URL, PY_PROFILE_URL):
  auto_fetch_profile_options =["Yes", "No"]
  auto_fetch_profile_choice = choiceBox("GSXプロファイルを更新しますか? \nDo you want to fetch the latest GSX profile?", 
                                        caption="GroundServicesJP Auto Profile Download",
                                        choices=auto_fetch_profile_options, 
                                        default=1)
  if auto_fetch_profile_choice == 0:
    print("[GSJP Auto-Fetch] User opted-in of automatic profile updates. Local profile files will be used.")
  else:
    print("[GSJP Auto-Fetch] User opted-out of automatic profile updates. Attempting to fetch latest profile files from GitHub.")

    ini_fetched = fetchINI(INI_PROFILE_URL)
    py_fetched = fetchPY(PY_PROFILE_URL)
    good_message = ""
    if ini_fetched:
      good_message += ".iniプロファイルを更新しました。\n.ini profile fetched successfully.\n"
      print("[GSJP Auto-Fetch] .ini profile fetched successfully.")
    if py_fetched:
      good_message += ".pyプロファイルを更新しました。\n.py profile fetched successfully.\n"
      print("[GSJP Auto-Fetch] .py profile fetched successfully.")

    if ini_fetched or py_fetched:
      messageBox(good_message, caption="GroundServicesJP Auto Profile Download", style=MB_OK | MB_ICONINFO)
    elif ini_fetched == False and py_fetched == False:
      print("[GSJP Auto-Fetch] No new .ini and .py profiles available.")