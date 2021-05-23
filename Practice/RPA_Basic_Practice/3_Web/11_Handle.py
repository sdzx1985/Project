import time
from selenium import webdriver
 
browser = webdriver.Chrome("./chromedriver")
browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
curr_handle = browser.current_window_handle
print(curr_handle) # window handle info

browser.find_element_by_xpath('//*[@id="main"]/div[2]/a').click()

handles = browser.window_handles # all handle info
for handle in handles:
    print(handle)
    browser.switch_to_window(handle)
    print(browser.title)
    print()

# new browser

#quit the new browser
print("close")
browser.close()

print("original handle")
browser.switch_to_window(curr_handle)
print(browser.title)

time.sleep(5)
browser.get('http://google.com')

time.sleep(5)
browser.quit()