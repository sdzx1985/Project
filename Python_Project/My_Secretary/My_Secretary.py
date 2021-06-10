import re
import requests
import smtplib
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime
from email.message import EmailMessage
from email.mime.text import MIMEText
from Account import *


def datetimenow():
    now = datetime.now()
    return (now)


def create_soup(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return(soup)


def create_browser(url):
    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome("./chromedriver", options=options)
    browser.get(url)
    return (browser)


def today_weather():
    now = datetimenow()

    url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57.968j0j15&sourceid=chrome&ie=UTF-8"
    soup = create_soup(url)

    cast = soup.find("img", attrs={"class": "wob_tci"})
    curr_temp = soup.find("span", attrs={"class": "wob_t TVtOme"}).get_text()
    daily_temp = soup.find("div", attrs={"class": "wNE31c"})
    max_temp = daily_temp.find_all("span")[0].get_text()
    min_temp = daily_temp.find_all("span")[2].get_text()

    prec = soup.find("span", attrs={"id": "wob_pp"}).get_text()
    humid = soup.find("span", attrs={"id": "wob_hm"}).get_text()
    wind = soup.find("span", attrs={"id": "wob_ws"}).get_text()

    print("[Today's Weather ({})]".format(now.strftime('%Y-%m-%d')))
    print()

    print("Today is {}.".format(cast.get('alt').lower()))
    print("Current temperature is {}°. (Min {}°, Max {}°)".format(
        curr_temp, min_temp, max_temp))
    print()
    print("Precipitation : {}, Humidity : {}, Wind : {}.".format(prec, humid, wind))
    print()


def headline_news():
    now = datetimenow()

    url = "https://www.cnn.com/us"
    browser = create_browser(url)

    print("[Today's headline news ({})]".format(now.strftime('%Y-%m-%d')))
    print()

    soup = BeautifulSoup(browser.page_source, "html.parser")

    headlines = soup.find_all("h3", class_='cd__headline', limit=3)

    index = 1
    for headline in headlines:
        print("{}. ".format(index), headline.text.strip())
        print("  Link : https://www.cnn.com" +
              headline.a.get('href').replace('//', ' '))
        index += 1

    print()
    browser.quit()


def IT_news():
    now = datetimenow()

    url = "https://www.computerworld.com/news/"

    print("[Today's IT issues ({})]".format(now.strftime('%Y-%m-%d')))
    print()

    soup = create_soup(url)

    news_list = soup.find(
        "div", attrs={"class": "main-col"}).find_all("h3", limit=3)

    for index, news in enumerate(news_list):
        a_idx = 0
        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]

        print("{}. {}".format(index+1, title))
        print("  Link : {}".format(link))

    print()


def ted_talk():
    now = datetimenow()

    url = "https://www.ted.com/talks"
    browser = create_browser(url)

    print("[Today's TED Talk ({})]".format(now.strftime('%Y-%m-%d')))
    print()

    soup = BeautifulSoup(browser.page_source, "html.parser")

    teds = soup.find("div", class_='media__message')

    print("Topic :", teds.a.get_text().strip())
    print("Author :", teds.h4.get_text().strip())
    print("  Link : https://www.ted.com" +
          teds.a.get('href').replace('//', ' '))


print()

if __name__ == "__main__":

    today_weather()
    headline_news()
    IT_news()
    ted_talk()
