import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome("./chromedriver")
browser.get('https://www.w3schools.com/html/')

time.sleep(5)

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[61]')

# 1st. ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 2nd. : (x, y) info use
# xy = elem.location_once_scrolled_into_view
# print("type : ", type(xy)) # check
# print("value : ", xy) # check

elem.click() 


time.sleep(5)
browser.quit()
