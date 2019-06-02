"""
@Author: Ariel Kipervasser
@Purpose: This program should implement the OutRain assignment which checks
the location according to your IP address, than checks the weather at that
location and prints the result to the screen
@Date: 29/05/19
@Version: 1.0
@file: outrain.py
"""

import json

from urllib.error import HTTPError
from urllib.request import urlopen

LOCATION_URL = "https://ipinfo.io/json"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather?q={}," \
			  "{}&appid={}"

API_KEY = "3dd1eacea99c2c067dd60b8a59b1d328"
KELVIN_TO_CELSIUS_CONVERTOR = 273.15


def fetch_weather(city, country):
	"""
	Receive a city and country and return the temperature in celsius
	:param city: The city of the IP location
	:type: C{str}
	:param country: The country of the IP location
	:type: C{str}
	:return: The temperature
	:rtype: C{int}
	"""
	try:
		response = urlopen(WEATHER_URL.format(city, country, API_KEY))
	except HTTPError:
		print("No such city as {} or country as {} in the weather website "
			  "openweathermap.org".format(city, country))
		return None
	else:
		data = json.load(response)

	# Temperature retrieved from the data and converted to celsius as integer
	return int(data['main']['temp'] - KELVIN_TO_CELSIUS_CONVERTOR)
	

def out_rain():
	"""
	Check the location according to your IP address, than check the weather
	at that location and print the result to the screen
	"""
	response = urlopen(LOCATION_URL)
	data = json.load(response)
	city = data['city']
	country = data['country']

	temperature = fetch_weather(city, country)

	if temperature is not None:
		print("The weather in {}, {} is {} degrees.".format(
			city, country, temperature)
		)
	

if __name__ == '__main__':
	out_rain()
