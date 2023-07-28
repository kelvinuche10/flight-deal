from datetime import datetime, timedelta
import requests
from notification_manager import NotificationManager

today = datetime.now().strftime('%d/%m/%Y')
date_to = (datetime.now() + timedelta(days=60)).strftime('%d/%m/%Y')
return_from = (datetime.now() + timedelta(days=7)).strftime('%d/%m/%Y')
return_to = (datetime.now() + timedelta(days=28)).strftime('%d/%m/%Y')

class FlightData:
    def __init__(self, api_key, data_dict:dict):
        api_key = api_key
        self.data_dict = data_dict
        kiwi_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        
        header = {
            'apikey' : api_key,
            'content_type': 'application/json'
        }

        
        for state in self.data_dict:
            params = {
            'fly_from': 'LON',
            'fly_to': state['iataCode'],
            'date_from': today,
            'date_to': date_to,
            'curr': 'GBP',
            'return_to': return_to,
            'return_from': return_from,
        }
            response = requests.get(url=kiwi_endpoint, headers=header, params=params)
            self.iatacode = response.json()['data'][0]['flyTo']
            self.price = response.json()['data'][0]['price']
            self.outbound_date = response.json()['data'][0]['local_arrival'].split('T', 0)
            self.inbound_date = response.json()['data'][0]['local_departure'].split('T', 0)
            self.city_from = response.json()['data'][0]['cityFrom']
            self.city_to = response.json()['data'][0]['cityTo']

