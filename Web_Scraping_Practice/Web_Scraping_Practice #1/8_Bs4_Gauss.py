import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

#cartoons = soup.find_all("td", attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title)
# print("https://comic.naver.com" + link)

# title + link
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title, link)

# rating
total_rates = 0
cartoons_rates = soup.find_all("div", attrs={"class":"rating_type"})
for cartoons_rate in cartoons_rates:
    rate = cartoons_rate.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print ("Total rates : ", total_rates)
print ("Average : ", total_rates / len(cartoons_rates))