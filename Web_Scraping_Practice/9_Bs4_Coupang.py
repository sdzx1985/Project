import sys
import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text)

for item in items:

    # No Ad items
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print ("  < this is ad item >")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text() #Item
    if "Apple" in name:
        print(" < Remove Apple items > ")
        continue

    price = item.find("strong", attrs={"class":"price-value"}).get_text() #Price

    # More than 100 review, and more than 4.5 rate
    rate = item.find("em", attrs={"class":"rating"}) #Rating
    if rate:
        rate = rate.get_text()
    else:
        print (" < No rate >")
        continue

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}) #Number of rating
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1] # Slicing
        # print("Review count: ", rate_cnt)
    else:
        print (" < No rate count >")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
