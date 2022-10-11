from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

"""
    Get name song
"""
DOMAIN = "https://www.billboard.com/charts/hot-100/"

travel_day = input("which year do you want to travel to? Type the date in this format YYYY-MM-DD\n")
# travel_day = "2000-08-12"

URL = f"{DOMAIN}{travel_day}/"

reponse = requests.get(url=URL)

billboard_page_by_date = reponse.text

soup = BeautifulSoup(billboard_page_by_date, 'html.parser')

titles_tag = soup.select(selector="ul.lrv-a-unstyle-list li h3#title-of-a-story")

titles_name = [tag.getText().split("\t")[9] for tag in titles_tag]

"""
    Authorize
"""
CLIENT_ID = "94abc43c1383463e99f871f5ce0c2e05"
CLIENT_SECRET = "a550c58016fa4f92a89f0cb5487a191e"

scope = "playlist-modify-private"

spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scope=scope,
                              redirect_uri="http://zoan.com/callback/", show_dialog=True,
                              cache_path="token.txt"))

user_id = spotify.current_user()['id']
song_uris = []

year = travel_day.split('-')[0]

for song in titles_name:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        # print(f"{song} doesn't exist in Spotify. Skipped.")
        pass

playlist = spotify.user_playlist_create(user=user_id, name=f"{travel_day} Billboard 100", public=False)

spotify.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

print("Done")
