import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# title=soup.title
# anchors=soup.find_all('a')
movies=soup.find('',class_="lister-item-content")
print(movies.get_text())
