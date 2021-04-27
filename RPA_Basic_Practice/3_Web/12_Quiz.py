import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
browser = webdriver.Chrome("./chromedriver")
browser.get('https://www.w3schools.com/')

learn_html = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
how_to = browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
contact_form = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[116]').click()

fName = "Aiden"
lName = "Oh"
subject = "Complete"

f_Name = browser.find_element_by_xpath('//*[@id="fname"]')
f_Name.send_keys(fName)
l_Name = browser.find_element_by_xpath('//*[@id="lname"]')
l_Name.send_keys(lName)
country = browser.find_element_by_xpath('//*[@id="country"]/option[contains(text(), "Ca")]').click()
subj = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
subj.send_keys(subject)

time.sleep(5)
submit = browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()