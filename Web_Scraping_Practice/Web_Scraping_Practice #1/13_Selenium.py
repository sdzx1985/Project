import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.get("http://naver.com")

# 2. log in button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. log in click
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. new id 
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear
browser.find_element_by_id("id").send_keys("my_id")

# html info output
print(browser.page_source)

# 7. exit browser
browser.close() # tab 
# browser.quit() # all