import datetime
import os

import requests
APP_ID = os.environ["NUTRI_APP_ID"]
API_KEY =os.environ["NUTRI_APP_KEY"]

NUTRIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2"

SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

user_query = input("Tell me which exercises you did: ")

exercises_params = {
    "query": user_query,
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 172,
    "age": 20
}

exercises_endpoint = f"{NUTRIONIX_ENDPOINT}/natural/exercise"

reponse_result = requests.post(url=exercises_endpoint, json=exercises_params,headers=headers)

sheety_post_config = {
    "workout": reponse_result.json()
}

date = datetime.datetime.now().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%X")

headers = {
    "Authorization":f"Basic {os.environ['TOKEN']}"
}

for sheet in reponse_result.json()['exercises']:
    row = {
        'workout':{
            'date': date,
            'time': time,
            "exercise": sheet["name"].title(),
            "duration": sheet["duration_min"],
            "calories": sheet["nf_calories"]

        }
    }
    post_data = requests.post(url=SHEETY_ENDPOINT,json=row, headers=headers)

