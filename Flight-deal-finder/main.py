import requests
import os

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
url = "https://test.api.amadeus.com/"

auth_url = f"{url}v1/security/oauth2/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
output = {'type': 'amadeusOAuth2Token', 'username': 'vishupicsbackup786@gmail.com',
          'application_name': 'Flight Deals',
          'client_id': 'Kpd3gjeeeT0VkBOGp3xNlKvvYOcwC5Td',
          'token_type': 'Bearer', 'access_token': 'utqGgjR78eJ9ujbRvtEmzB6h5AnK',
          'expires_in': 1799, 'state': 'approved', 'scope': ''}

body = {
    "grant_type": "client_credentials",
    "client_id": API_KEY,
    "client_secret": API_SECRET
}

flight_header = {
    "Authorization": "Bearer utqGgjR78eJ9ujbRvtEmzB6h5AnK"
}
flights_url = f"{url}v1/shopping/flight-destinations"
flight_body = {
    "origin": "PAR",
    "maxPrice": 3500
}

# auth_response = requests.post(url=auth_url, data=body, headers=headers)
# print(auth_response.json())

flight_response = requests.post(url=flights_url, headers=flight_header, json=flight_body)
print(flight_response.json())
