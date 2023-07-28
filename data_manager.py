import requests


class DataManager:
    def __init__(self, endpoint, data_dict:dict):
        self.endpoint = endpoint
        self.data_dict = data_dict
        id = '["id"]'
        for state in self.data_dict:
            put_endpoint = f'{self.endpoint}/{state["id"]}'
            params = {
            'price': {
                'iataCode': state['iataCode']
            }
            }
            requests.put(url=put_endpoint, json=params)
