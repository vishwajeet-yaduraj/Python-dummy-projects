import requests
from pprint import *
import os
from dotenv import load_dotenv
from flight_search import FlightSearch

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, url, headers):
        self.username = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.url = url
        self.header = headers
        self.response = requests.get(url=self.url, headers=self.header)

    def put_data(self, data):
        for data in data:
            search = FlightSearch()
            city = search.get_city_code(data['city'])
            body = {
                'price': {'iataCode': city}
            }
            response = requests.put(url=f"{self.url}/{data['id']}", json=body, headers=self.header)
            response.raise_for_status()
            print(response.text)

    def get_data(self):
        return self.response.json()['prices']

# For testing purposes
# sheety_url = "https://api.sheety.co/cf8a35393f70acd530021cfeefaeaf18/flight/prices"
# sheety_header = {
#     "Authorization": os.getenv("AUTH")
# }
# data = DataManager(url=sheety_url,headers=sheety_header)
# print(data.get_data())
