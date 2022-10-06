import requests
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "gk3Sss-xeWQN-vTQVbs1_AEDvNsyhWd0"

headers = {
    'apikey':TEQUILA_API_KEY
}
params = {
    'term':"Paris"
}
location = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params ,headers=headers)
print(location.json()['locations'][0]['code'])