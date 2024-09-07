import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")

y_c_data = response.text
# print(y_c_data)

soup = BeautifulSoup(y_c_data, 'html.parser')

# print(soup.prettify())


all_anchor_tags = soup.find_all('span', class_='titleline')
all_score_tags = soup.find_all('span', class_='score')

titles = []
all_links = []
upvote = []
for text in all_anchor_tags:
    titles.append(text.find('a').getText())
    all_links.append(text.find('a').get('href'))

for votes in all_score_tags:
    upvote.append(votes.getText())

upvote = [int(vote.split(' ')[0]) for vote in upvote]


# print(titles)
# print(all_links)
# print(upvote)

req_index = upvote.index(max(upvote))
print(titles[req_index])
print(all_links[req_index])
