import requests
from bs4 import BeautifulSoup

billboard_url = "https://www.billboard.com/charts/hot-100/"

date = input("What date you would like to travel to? Enter in YYYY-MM-DD format.\n")
billboard_url = billboard_url + date
print(billboard_url)
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

print(songs)

