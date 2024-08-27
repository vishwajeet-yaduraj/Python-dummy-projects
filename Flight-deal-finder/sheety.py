import requests
from pprint import pprint

sheety_url = "https://api.sheety.co/726667eaff2af514f687dcb8822f5e89/flightDeals/prices"

response = requests.get(url=sheety_url)
print(response.json())
