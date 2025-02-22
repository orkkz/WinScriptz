import pyautogui
import random
import string
import time

random_text = ''.join(random.choices(string.ascii_letters, k=1000))

for i in range(100):
    pyautogui.typewrite(random_text)
    time.sleep(0.7)
    pyautogui.press('enter')
    time.sleep(0.5)