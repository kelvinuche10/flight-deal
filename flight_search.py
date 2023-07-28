import requests


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key, data_dict:dict):
        self.data_dict = data_dict
        api_key = api_key
        # city = ['PAR', 'sydney', 'berlin', 'tokyo', 'cape town', 'new york']
        kiwi_endpoint = 'https://api.tequila.kiwi.com/locations/query'

        header = {
            'apikey': api_key,
            'content_type': 'application/json'
        }
        for state in self.data_dict:
            params = {
                'term': state['city'],
                }
            kiwi_response = requests.get(url=kiwi_endpoint, headers=header, params=params)
            state['iataCode'] = kiwi_response.json()['locations'][0]['code']


# f = FlightSearch()