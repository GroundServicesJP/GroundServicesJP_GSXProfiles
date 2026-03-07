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
# Bus/Airline Correlation
# version =  1.0

def fetchBusCorrelation(url):
	"""Load bus_airline_correlation from a remote JSON URL using fetchJson().

	Converts the JSON structure back to the dict format:
	- Key: ICAO airline code (str)
	- Value: list of bus types (str)

	Returns the parsed dict, or None if the fetch failed.
	"""
	raw = fetchJson(url, timeout=10, etag=True)
	if not raw:
		return None

	result = {}
	for airline, bus_types in raw.items():
		result[airline] = list(bus_types)  # Ensure it's a list of strings
	return result

def provideARandomBus(bus_candidates):
  return random.choice(bus_candidates)

def getBusFromCorrelation(icao_airline, correlation_matrix, correlation_url):
	# Try to fetch correlation matrix from remote URL, fallback to hardcoded dict if fetch fails
	correlation = fetchBusCorrelation(correlation_url)
	if correlation is None:
		print("[GSJP Auto-Bus] Failed to fetch remote correlation matrix, using fallback.")
		correlation = correlation_matrix
	else:
		print("[GSJP Auto-Bus] Successfully fetched remote correlation matrix.")

	bus_list = correlation.get(icao_airline, [])
	print(bus_list)
	print(icao_airline)

	bus = provideARandomBus(bus_list) if bus_list else ""

	return bus

def selectBusForAirline(self, gsx_candidates, icao_airline, correlation_matrix, correlation_url):
	selected_bus = getBusFromCorrelation(icao_airline, correlation_matrix, correlation_url)
	for candidate in gsx_candidates:
		if candidate.title and candidate.title == selected_bus:
			candidate.boostScore(100) # Give a big boost to the randomly selected ANA Mototok
			print(f"[GSJP Mototok] Boosting score for {candidate.title} since airline is {icao_airline}.")