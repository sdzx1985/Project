import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # change frame

elem = browser.find_element_by_xpath('//*[@id="male"]')

elem.click()

browser.switch_to.default_content() 
 
time.sleep(5)

browser.quit()