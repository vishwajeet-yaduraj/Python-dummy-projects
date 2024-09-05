# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os

load_dotenv()

sheety_url = "https://api.sheety.co/726667eaff2af514f687dcb8822f5e89/flightPrices/prices"
sheety_header = {
    "Authorization": os.getenv("AUTH")
}
data = DataManager(url=sheety_url, headers=sheety_header)

sheet_data = data.get_data()

Data = DataManager(sheety_url, sheety_header)
Data.put_data(sheet_data)

# for data in sheet_data:
#     if data['iataCode'] == "":
#         data['iataCode'] = 'TESTING'
#     print(data)

