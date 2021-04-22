import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trashIcon.png")
# pyautogui.moveTo(trash_icon)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i)

# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trashIcon.png", grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. Select area
# trash_icon = pyautogui.locateOnScreen("trashIcon.png", region=(617,588, 1177 - 617, 1058 - 588))
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()
# 617,588
# 1177,1058

# 3. Adjust
# trash_icon = pyautogui.locateOnScreen("trashIcon.png", confidence=0.9) # 90%
# pyautogui.moveTo(trash_icon)

