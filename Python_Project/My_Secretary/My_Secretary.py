import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime 

def datetimenow():
    now = datetime.now()
    return (now)

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return(soup)

def create_browser(url):
    options = webdriver.ChromeOptions()
    options.headless = True

    browser = webdriver.Chrome("./chromedriver", options = options)
    browser.get(url)
    return (browser)

def today_weather():
    now = datetimenow() 

    url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome..69i57.968j0j15&sourceid=chrome&ie=UTF-8"
    soup = create_soup(url)

    cast = soup.find("img", attrs={"class":"wob_tci"})
    curr_temp = soup.find("span", attrs={"class":"wob_t TVtOme"}).get_text()
    daily_temp = soup.find("div", attrs={"class":"wNE31c"})
    max_temp = daily_temp.find_all("span")[0].get_text()
    min_temp = daily_temp.find_all("span")[2].get_text()

    prec = soup.find("span", attrs={"id":"wob_pp"}).get_text()
    humid = soup.find("span", attrs={"id":"wob_hm"}).get_text()
    wind = soup.find("span", attrs={"id":"wob_ws"}).get_text()

    print("[Today's Weather ({})]".format(now.strftime('%Y-%m-%d')))
    print()

    print("Today is {}.".format(cast.get('alt').lower()))
    print("Current temperature is {}°. (Min {}°, Max {}°)".format(curr_temp, min_temp, max_temp))
    print()
    print("Precipitation : {}, Humidity : {}, Wind : {}.".format(prec, humid, wind))
    print()


def headline_news():
    now = datetimenow()

    url = "https://www.cnn.com/"
    browser = create_browser(url)
    soup = create_soup(url)
    
    print("[Today's headline news ({})]".format(now.strftime('%Y-%m-%d')))

    news_1 = browser.find_element_by_xpath('//*[@id="homepage1-zone-1"]/div[2]/div/div[1]/ul/li[1]/article/a/h2').click()
    firstnews = soup.find("h1", attrs={"class":"pg-headline"})
    print(firstnews.get_text())




    # headlines = soup.find("h2", attrs={"class":"banner-text screaming-banner-text banner-text-size--char-47"})
    # print(headlines)
    
    # for headline in headlines:
    #     print(headline.get_text())


    # for index, news in enumerate(headline):
    #     title = news.find("a").get_text().strip() 
    #     link = url + news.find("a")["href"]
    #     print_news(index, title, link)
    # print()

def IT_news():
    pass

def english_study():
    now = datetimenow() 

    url = "https://www.ted.com/"
    soup = create_soup(url)
    iframes = soup.find_all('iframe')

    print("[Today's TED Talk ({})]".format(now.strftime('%Y-%m-%d')))


    # TEDs = soup.find_all("div", attrs={"class":"slick-slide slick-active d:f flx-d:c a-i:s p-x:.4"})
    
    # for TED in TEDs:
        # print(TED.get_text())




if __name__ == "__main__":
    # today_weather()
    headline_news()
    # IT_news()
    # english_study()
