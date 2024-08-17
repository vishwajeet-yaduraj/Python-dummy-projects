import requests
from twilio.rest import Client
import os

api_key = os.getenv("API_KEY")
parameters = {
    "lat": "28.8",
    "lon": "70.11",
    "appid": api_key,
    "cnt": 4
}
account_sid = "ACd0b9c3aeee0a8602cefc1776c157dba4"
auth_token = os.getenv("AUTH_TOKEN")

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()['list']

for x in data:
    curr_id = x['weather'][0]['id']
    if curr_id < 700:
        print("Bring an Umbrella.")
        client = Client(account_sid, auth_token)
        message = client.messages.create(
          from_='+12085409435',
          body='Bring a fucking Umbrella, or you gonna get wet and dirty.',
          to=os.getenv("PHONE")
        )
        print(message.status)
        break

# print(data[0])


