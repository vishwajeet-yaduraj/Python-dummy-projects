import requests
import datetime as dt

MY_LAT = 28.61390
MY_LONG = 77.20901


def is_over_head():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 <= longitude <= MY_LAT + 5 and MY_LONG - 5 <= latitude <= MY_LONG + 5:
        return True


time_now = dt.datetime.now().time().hour


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if sunset <= time_now <= sunrise:
        return True


if is_night() and is_over_head():
    print("look up in the sky")
