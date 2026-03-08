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
# Model Disabler
# version =  1.0

def disableModelByString(self, candidates, model_name):
  found = False
  for candidate in candidates:
    if candidate.title and model_name in candidate.title:
      candidate.boostScore(-100) # Give a big negative boost to effectively disable this model from being selected
      found = True
  if found:
    print(f"[GSJP Model Disabler] Disabled candidates with model name containing '{model_name}'.")

# To use these specific functions, candidates should be filtered to the specific vehicle type (e.g. BaggageLoader)
def disableCCL35S(self, candidates):
  print("[GSJP Model Disabler] Checking for CCL-35S models to disable in baggage loader candidates.")
  disableModelByString(self, candidates, "CCL35S")

def disableNeoplan(self, candidates):
  print("[GSJP Model Disabler] Checking for Neoplan models to disable in bus candidates.")
  disableModelByString(self, candidates, "neoplan")