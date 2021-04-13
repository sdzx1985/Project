import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size = 1920x1080")
# options.add_argument("user-agent = Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36")

# browser = webdriver.Chrome("./chromedriver", options = options)
# browser.maximize_window()

# url = "https://www.daum.net/"
url2 = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
# browser.get()

# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
#     }

res = requests.get(url2)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print ("=========== 매물{} ==========".format(index+1))
    print ("거래 : ", columns[0].get_text())
    print ("면적 : ", columns[1].get_text())
    print ("가격 : ", columns[2].get_text())
    print ("동  : ", columns[3].get_text())
    print ("층  : ", columns[4].get_text())
    



# browser.find_element_by_class_name("tf_keyword").click()
# browser.find_element_by_id("q").send_keys("송파 헬리오시티")
# browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()

# for i in range (1, 6):
#     col = soup.find("th", attrs={"class":"col"+[i]}).get_text()
#     print ()
    
 