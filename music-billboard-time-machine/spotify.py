from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
import os


load_dotenv()
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
for playlist in playlists['items']:
    print(playlist['name'])


user_id = sp.current_user()['id']
print(user_id)

user_id = sp.current_user()["id"]

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
