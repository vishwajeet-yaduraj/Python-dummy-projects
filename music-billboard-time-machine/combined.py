from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup

load_dotenv()
billboard_url = "https://www.billboard.com/charts/hot-100/"

date = input("What date you would like to travel to? Enter in YYYY-MM-DD format.\n")
billboard_url = billboard_url + date
response = requests.get(billboard_url).text
soup = BeautifulSoup(response, 'html.parser')

all_artists = soup.find_all('span', class_='u-max-width-230@tablet-only')
artists = []
for song in all_artists:
    artists.append(song.getText())

artists = [artist.strip() for artist in artists]
# print(artists)

all_songs = soup.find_all('h3', class_='u-max-width-230@tablet-only')
songs = []
for song in all_songs:
    songs.append(song.getText().strip())


username = os.getenv("SPOTIFY_USERNAME")
code = os.getenv("CODE")

sp_oauth = SpotifyOAuth(client_id=os.getenv("SPOTIFY_AUTH"),
                        client_secret=os.getenv("SPOTIFY_SECRET"),
                        redirect_uri='http://example.com',
                        scope='user-library-read')

auth_url = sp_oauth.get_authorize_url()
print(f'Please go to this URL to authorize: {auth_url}')

# Step 3: After authorization, get the code and exchange it for an access token

token_info = sp_oauth.get_access_token(code)

# Step 4: Use the access token to create a Spotify object
access_token = token_info['access_token']
sp = spotipy.Spotify(auth=access_token)

# Example: Get current user's playlists
playlists = sp.current_user_playlists()
# for playlist in playlists['items']:
#     print(playlist['name'])


user_id = sp.current_user()['id']
# print(user_id)

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
