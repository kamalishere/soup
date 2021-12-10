# import  requests
# from bs4 import BeautifulSoup

# webpage= requests.get('https://www.flipkart.com/electric-jugheatertravel-kettles/~cs-cvqunrtid0/pr?sid=j9e%2Cm38%2Cxrv&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&sort=popularity&p%5B%5D=facets.price_range.from%3D499&p%5B%5D=facets.price_range.to%3DMax&hpid=9-hEqwd0Z9elvA-D2nDclap7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_f6b9709a-fe95-44fd-9533-f88e4c2a7484_3.E827MYUMQMN4&ssid=9r7irx1fr40000001638589106330&otracker=hp_omu_Top%2BOffers_4_3.dealCard.OMU_E827MYUMQMN4_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Top%2BOffers_NA_dealCard_cc_4_NA_view-all_3&cid=E827MYUMQMN4')

# soup=BeautifulSoup(webpage.content,'html.parser')
# print(soup.find_all('section').prettify)
import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
# for i in soup.find_all("div.div.code"):
#     print(i.prettify())
    # We can also do it like this
    # print(i.get_text())
# print(soup.find('p')['class'])
# print(soup.get_text())
paras=soup.find_all("p")
anchors=soup.find_all("a")
title=soup.title
h4=soup.find_all("h4")
# for i in h4:
#     print(i.prettify())
all_links=set()
for link in anchors:
    if(link.get("href")!= "#"):
        linktext = link.get("href")
print(linktext)        
    

