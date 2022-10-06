import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os
MY_LAT = 16.054407
MY_LONG = 108.202164

# api_key = os.environ.get("69f04e4613056b159c2761a9d9e664d2")
# OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
#
# account_sid = "ACdd7d6146dc3cddbd76c415d4d8d03f45"
# auth_token = "a7b336a3a2e1060e708afb545d309a46"

api_key = os.environ.get("OWN_API_KEY")
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "ACdd7d6146dc3cddbd76c415d4d8d03f45"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

reponse = requests.get(OWN_Endpoint, params=weather_params)
# reponse.raise_for_status()
print(reponse.status_code)
# print(reponse.json())
weather_data = reponse.json()
print(weather_data)

weather_slice = [item['weather'][0]['id'] for item in weather_data['hourly'][:12]]

will_rain = False
for id in weather_slice:
    if int(id) < 700:
        will_rain = True

print(will_rain)

if will_rain:
    print("Bring an umbrella")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['http_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+12057362627",
        to="+84905642739"
    )
    print(message.status)
