import requests
import datetime
import os

pixela_url = "https://pixe.la/v1/users"
TOKEN = os.getenv("TOKEN")
USERNAME = "yaduraj-vishu"

first_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=first_params)

graph_url = f"{pixela_url}/{USERNAME}/graphs"
graph_params = {
    "id": "vishu-graph",
    "name": "habit-tracking-graph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_url, json=graph_params, headers=headers)

post_value_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/vishu-graph"

today = datetime.datetime.now()
DATE = today.strftime("%Y%m%d")

post_params = {
    "date": DATE,
    "quantity": "14"
}
response = requests.post(url=post_value_url, headers=headers, json=post_params)

# Let's update the data a bit.
update_url = f"{pixela_url}/{USERNAME}/graphs/vishu-graph/{DATE}"
# response = requests.put(url=update_url, headers=headers, json={"quantity": "7"})

print(response.text)
