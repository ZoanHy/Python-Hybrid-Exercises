import requests

URL = "https://api.themoviedb.org/3/"
# search/keyword?api_key=71aa2f1925317c30fa164225647cf45d&query=Matrix"
API_KEY = '71aa2f1925317c30fa164225647cf45d'
query = 'The Matrix'
reponse = requests.get(
    url=f"{URL}search/movie?api_key={API_KEY}&query={query}")

list_movie = reponse.json()['results']
