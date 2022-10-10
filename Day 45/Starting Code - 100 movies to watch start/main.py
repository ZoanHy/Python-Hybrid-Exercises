import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

reponse = requests.get(url=URL)

best_movie_web_page = reponse.text

soup = BeautifulSoup(best_movie_web_page, 'html.parser')

list_movies = soup.findAll(name="h3", class_="title")
name_movies = [list_movies[i].getText() for i in range(len(list_movies) - 1, -1, -1)]

with open("movies.txt", "w", encoding="utf8") as file:
    for name in name_movies:
        file.write(name + "\n")
