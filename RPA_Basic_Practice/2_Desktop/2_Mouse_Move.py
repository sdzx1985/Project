import pyautogui

# pyautogui.moveTo(200, 100) # move mouse (x, y)
# pyautogui.moveTo(100, 200, duration=5) # 5sec

# pyautogui.moveTo(100, 100, duration=0.25)
# pyautogui.moveTo(200, 200, duration=0.25)
# pyautogui.moveTo(300, 300, duration=0.25)

# from currunt cursor
# pyautogui.moveTo(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())
# pyautogui.move(100, 100, duration=0.25)
# print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y
