# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime
import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

START_CITY = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_data_flight_destination()
flight_search = FlightSearch()
if sheet_data[0]['iataCode'] == '':
    from flight_search import FlightSearch

    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.reponse_code(row['city'])
    data_manager.data_flight = sheet_data
    # data_manager.update_data_flight_destination()
    # print(data_manager.data_flight)

tommrrow = datetime.datetime.now() + datetime.timedelta(days=1)
six_month = datetime.datetime.now() + datetime.timedelta(days=30 * 6)

for row in sheet_data:
    flight = flight_search.check_flight(
        START_CITY,
        row['iataCode'],
        time_start=tommrrow,
        time_end=six_month
    )

