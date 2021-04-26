import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("./chromedriver")
browser.get('https://shopping.naver.com/home/p/index.nhn')

elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('wireless mouse')

time.sleep(1)
elem.send_keys(Keys.ENTER)

# Scroll
# browser.execute_script('window.scrollTo(0, 1440)')
# browser.execute_script('window.scrollTo(0, 2840)')

# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

interval = 2 # scroll down every 2 seconds

prev_height= browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(interval) # wait page loading

    curr_heught = browser.execute_script('return document.body.scrollHeight')
    if curr_heught ==  prev_height: # no height change
        break # end loop
    
    prev_height = curr_heught

# scroll up
browser.execute_script('window.scrollTo(0, 0)')



time.sleep(5)
browser.quit()