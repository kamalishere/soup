import  requests
from bs4 import BeautifulSoup

url="https://codewithharry.com"
#step1:get  the html
r=requests.get(url)
htmlcontent=r.content

#step2:parse the html
soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())
#step3:tree traversal
title=soup.title
#print(type(title))

#get all p tags
paras=soup.find_all('p')

anchor=soup.find_all('a')
#print(soup.find('p')['class'])
print(soup.find('h1').get_text())
print(soup.find('a').get_href())


