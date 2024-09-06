import os
from pprint import pprint
import requests
from dotenv import load_dotenv

load_dotenv()
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_API_SECRET = os.getenv("API_SECRET")
        self.token = self._get_new_token()

    def _get_new_token(self):
        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self.AMADEUS_API_KEY,
            "client_secret": self.AMADEUS_API_SECRET
        }
        response = requests.post(url=token_url, headers=headers, data=body)
        response.raise_for_status()
        return response.json()['access_token']

    def get_city_code(self, city_name):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS"
        }
        response = requests.get(url=IATA_ENDPOINT, headers=headers, params=query)
        response.raise_for_status()
        return response.json()['data'][0]['iataCode']
