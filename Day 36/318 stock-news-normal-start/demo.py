import requests

key = "L4FZUA2OBM96TJDZ"

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=L4FZUA2OBM96TJDZ'
r = requests.get(url)
data = r.json()


print(data)