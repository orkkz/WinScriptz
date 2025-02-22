import ctypes
import time
import threading

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long), 
                ("top", ctypes.c_long), 
                ("right", ctypes.c_long), 
                ("bottom", ctypes.c_long)]
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
hdc = user32.GetDC(0)
def blink_screen(duration=60, interval=0):
    end_time = time.time() + duration
    rect = RECT(0, 0, screen_width, screen_height)

    while time.time() < end_time:
        user32.InvertRect(hdc, ctypes.byref(rect))
        time.sleep(interval)
    user32.ReleaseDC(0, hdc)

threading.Thread(target=blink_screen).start()
threading.Thread(target=blink_screen).start()
threading.Thread(target=blink_screen).start()
threading.Thread(target=blink_screen).start()
threading.Thread(target=blink_screen).start()
threading.Thread(target=blink_screen).start()
blink_screen()
