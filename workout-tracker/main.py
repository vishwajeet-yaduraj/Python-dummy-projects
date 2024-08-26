import os
import datetime as dt
import requests

API_ID = os.getenv("API_ID")
API_KEY = os.getenv("API_KEY")
host_url = "https://trackapi.nutritionix.com"
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
endpoint = "/v2/natural/exercise"

params = {
    "query": input("What did you do today?"),
    "gender": "Male",
    "weight_kg": 60,
    "height_cm": 178,
    "age": 21

}

sheety_url = "https://api.sheety.co/726667eaff2af514f687dcb8822f5e89/workoutTracking/workouts"

date = dt.datetime.now()

TIME = date.strftime("%H:%M:%S")
DATE = date.strftime("%d/%m/%Y")


response = requests.post(url=f"{host_url}{endpoint}", json=params, headers=headers)

exercise_array = response.json()["exercises"]

sheety_user = "vishuyaduraj"
sheety_PASS = os.getenv("SHEETY_PASS")
sheety_header = {
    "Authorization": os.getenv("SHEETY_AUTH")
}

for name in exercise_array:
    body = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": name["name"].title(),
            "duration": name['duration_min'],
            "calories": name['nf_calories']
        }
    }
    response = requests.post(url=sheety_url, json=body,headers=sheety_header)
    response.raise_for_status()
