import datetime as dt
import os
from flight_search import FlightSearch
import requests

flight = FlightSearch()


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.AMADEUS_API_KEY = os.getenv("AMADEUS_API_KEY")
        self.AMADEUS_API_SECRET = os.getenv("API_SECRET")
        self.token = flight.token
        self.originLocationCode = 'DEL'
        self.date_today = dt.date.today()

    def find_cheapest_flight(self):
        FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        body = {
            "originLocationCode": self.originLocationCode,
            "destinationLocationCode": "PAR",
            "departureDate": self.date_today,
            "adults": "1",
            "currencyCode": "USD",

        }
        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = requests.get(url=FLIGHT_ENDPOINT, data=body, headers=headers)
        response.raise_for_status()
        print(response.json())


test = FlightData()
test.find_cheapest_flight()
