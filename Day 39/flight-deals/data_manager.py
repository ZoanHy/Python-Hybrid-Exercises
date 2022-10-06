import requests

SHEETY_ENDPOINT = "https://api.sheety.co/a7705fee7c180ced905b3da4ff5345fc/flightDeals/prices"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data_flight={}
    def get_data_flight_destination(self):
        reponse = requests.get(url=SHEETY_ENDPOINT)
        self.data_flight = reponse.json()['prices']
        return self.data_flight

    def update_data_flight_destination(self):
        for row in self.data_flight:
            new_row = {
                'price':{
                    'iataCode':row['iataCode']
                }
            }
            reponse = requests.put(url=f"{SHEETY_ENDPOINT}/{row['id']}", json=new_row)
            print(reponse.text)