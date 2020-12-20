import pyautogui
import time

while True:
    pyautogui.typewrite("Text You Want to Write automatically")
    time.sleep(3)
    pyautogui.press('enter')

