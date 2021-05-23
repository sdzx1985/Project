import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory':r'/Users/aidenoh/Documents/GitHub/Project'})

browser = webdriver.Chrome("./chromedriver", options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to_frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()