import datetime

import requests

MY_LAT = 16.054407
MY_LONG = 108.202164

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# response.raise_for_status()
# data = response.json()
# print(data)
# print(response.raise_for_status())
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (latitude, longitude)
# print(iss_position)

# if response.status_code == 404:
#     # raise Exception("Bad response from ISS API")
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("error")

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted":0
}

reponse = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(reponse.raise_for_status())
data = reponse.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
print(data)
print(sunrise.split("T")[1].split(":")[0])
print(sunset)

time_now = datetime.datetime.now()
print(time_now)
