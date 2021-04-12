import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return(soup)

def today_weather():
    

    url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57.968j0j15&sourceid=chrome&ie=UTF-8"
    soup = create_soup(url)

    time = soup.find("div", attrs={"class":"wob_dts"}).get_text()

    cast = soup.find("img", attrs={"class":"wob_tci"})
    curr_temp = soup.find("span", attrs={"class":"wob_t TVtOme"}).get_text()
    daily_temp = soup.find("div", attrs={"class":"wNE31c"})
    max_temp = daily_temp.find_all("span")[0].get_text()
    min_temp = daily_temp.find_all("span")[2].get_text()

    prec = soup.find("span", attrs={"id":"wob_pp"}).get_text()
    humid = soup.find("span", attrs={"id":"wob_hm"}).get_text()
    wind = soup.find("span", attrs={"id":"wob_ws"}).get_text()

    print("[Today's Weather ({})]".format(time))
    print()

    print("Today is {}.".format(cast.get('alt').lower()))
    print("Current temperature is {}°. (Min {}°, Max {}°)".format(curr_temp, min_temp, max_temp))
    print()
    print("Precipitation : {}, Humidity : {}, Wind : {}.".format(prec, humid, wind))
    



if __name__ == "__main__":
    today_weather()
    # headline_news()
    # IT_news()
    # english_study()
