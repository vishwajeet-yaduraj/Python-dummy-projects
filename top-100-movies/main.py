import requests
from bs4 import BeautifulSoup

empire_top_100_movies_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=empire_top_100_movies_url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

all_movies = soup.find_all('h3', class_='title')
movies = []
for movie in all_movies:
    movies.append(movie.text)

movies.reverse()
# print(movies)

for movie in movies:
    with open('movies.txt', 'a', encoding='utf-8') as file:
        file.write(movie+"\n")


# print(soup.prettify())
