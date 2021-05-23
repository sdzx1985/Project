import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver")

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
browser.switch_to.frame('iframeResult') 

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()

# Select through text
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# The same text partically
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(5)

browser.quit()


