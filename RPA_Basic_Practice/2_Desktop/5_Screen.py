import pyautogui
# Take a screenshot

# img = pyautogui.screenshot()
# img.save("screenshot.png")

# pyautogui.mouseInfo()
# 284,74
# 283,72 NA_on_macOS NA_on_macOS

pixel = pyautogui.pixel(284, 74)
print(pixel)

# print(pyautogui.pixelMatchesColor(284, 74, (60, 60, 60))) # True
# print(pyautogui.pixelMatchesColor(284, 74, (pixel))) # True
# print(pyautogui.pixelMatchesColor(284, 74, (61, 65, 66))) # True


