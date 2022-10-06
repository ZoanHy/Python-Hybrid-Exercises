import requests
from datetime import datetime
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "gk3Sss-xeWQN-vTQVbs1_AEDvNsyhWd0"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def reponse_code(self, name_city):
        headers = {
            'apikey': TEQUILA_API_KEY
        }
        params = {
            'term': name_city
        }
        location = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=headers)
        return location.json()['locations'][0]['code']

    def check_flight(self, start_city_code, destination_city_code, time_start: datetime, time_end: datetime):
        headers = {
            'apikey': TEQUILA_API_KEY
        }
        params = {
            "fly_from": start_city_code,
            "fly_to": destination_city_code,
            "date_from ": time_start.strftime("%d/%m/%Y"),
            "date_to ": time_end.strftime("%d/%m/%Y")
        }

        reponse = requests.get(url=f"{TEQUILA_ENDPOINT}/search", params=params, headers=headers)
        try:
            data = reponse.json()['data'][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}")
            return None

        flight_data = FlightData(
            price=data['price'],
            start_city=data['route'][0]["cityFrom"],
            start_port=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_port=data['route'][0]['flyTo'],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data['route'][1]['local_departure'].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
