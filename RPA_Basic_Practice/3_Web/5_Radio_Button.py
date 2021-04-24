import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') 
elem = browser.find_element_by_xpath('//*[@id="male"]')

if elem.is_selected() == False:
    print("Select")
    elem.click()
else:
    print("Selected")

time.sleep(5)

if elem.is_selected() == False:
    print("Select")
    elem.click()
else:
    print("Selected")

browser.quit()
