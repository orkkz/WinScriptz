import pyautogui
import time
import threading

# Duration in seconds. Default is 60 seconds.

pyautogui.FAILSAFE = False
def freeze_mouse(duration=60):
    x, y = pyautogui.position()
    start_time = time.time()
    while time.time() - start_time < duration:
        for i in range(5):
            threading.Thread(target=pyautogui.moveTo, args=(x, y,)).start()

freeze_mouse()