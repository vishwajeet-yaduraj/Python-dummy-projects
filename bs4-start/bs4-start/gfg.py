import requests
from bs4 import BeautifulSoup

# request to the ULR
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

# parsing HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# printing details from the HTML
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)
all_anchor_tags = soup.find_all("a")
for text in all_anchor_tags:
    print(text.get('href'))
