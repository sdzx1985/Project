import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
browser = webdriver.Chrome("./chromedriver")
browser.get('https://www.w3schools.com/')

browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()

browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()
# browser.find_element_by_link_text('Contact Form').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

first_name = "Aiden"
last_name = "Oh"
country = "Canada"
subject = "Complete"

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()
