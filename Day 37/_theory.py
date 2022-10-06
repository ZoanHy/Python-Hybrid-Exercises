import datetime

import requests

USERNAME = "zoanhyhehe"
TOKEN = "afasdfas1231asfvxcv"

pixela_endpoint = "https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# reponse = requests.post(url=pixela_endpoint, json=user_params)
# print(reponse.text)

graph_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"Jogging Graph",
    "unit":"Km",
    "type":"float",
    "color":"momiji"
}

headers = {
    'X-USER-TOKEN':TOKEN
}

# reponse = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(reponse.text)


pixel_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.datetime.now().strftime("%Y%m%d")

pixel_graph_pixel_config = {
    "date":today,
    "quantity":"3",
}

# reponse = requests.post(url=pixel_graph_endpoint, json=pixel_graph_pixel_config, headers=headers)
# print(reponse.text)

pixel_graph_update_pixel = f"{pixel_graph_endpoint}/{today}"
pixel_graph_update_pixel_config = {
    "quantity":"2.3"
}
# reponse = requests.put(url=pixel_graph_update_pixel, json=pixel_graph_update_pixel_config, headers=headers)
# print(reponse.text)

reponse = requests.delete(url=pixel_graph_update_pixel, headers=headers)
print(reponse.text)