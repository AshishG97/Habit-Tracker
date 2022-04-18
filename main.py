import requests
from datetime import datetime

USERNAME = USER NAME
TOKEN = TOKEN HERE
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = GRAPH ID HERE

user_params = {
    "token": TOKEN,  # randomly typed by me
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# # response.raise_for_status()
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Book Reading Graph",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}
header = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today()
# print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you studied today ? please don't lie...\n"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=header)
print(response.text)
