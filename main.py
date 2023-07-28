#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


API_KEY = your_sheety_api_key

sheety_endpoint = 'https://api.sheety.co/b24d40efccfe08788e5556a7c3725302/flightDeals/prices'
sheety_response = requests.get(url=sheety_endpoint)
print(sheety_response.json())
sheet_data = sheety_response.json()['prices']
print(sheet_data)

flightsearch = FlightSearch(API_KEY, sheet_data)
datamanager = DataManager(sheety_endpoint, sheet_data)
for sheet in sheet_data:
	flightdata = FlightData(API_KEY, sheet_data)
	if sheet['iataCode'] == flightdata.iatacode:
		print(flightdata.price)


print('code completed')




