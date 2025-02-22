import cv2
import numpy as np
import requests
from PIL import Image
import io
import ctypes
import time

# Image URLs
image_urls = [
    "https://st2.depositphotos.com/1268628/10355/i/450/depositphotos_103556100-stock-photo-ghost-girlhorror-background-for-halloween.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTu7Szoe5U9w8KpHh52uNlzg2mkMiIXNA489tt7hfpDKLqCP6U7zPv4SjIgqNybNpOjM3g&usqp=CAU"
]

def show_image(image_url, duration=5):
    response = requests.get(image_url, stream=True)
    image = Image.open(io.BytesIO(response.content))
    screen_width = ctypes.windll.user32.GetSystemMetrics(0)
    screen_height = ctypes.windll.user32.GetSystemMetrics(1)
    image = image.resize((screen_width, screen_height))
    image_np = np.array(image)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    cv2.namedWindow("Horror", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Horror", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Horror", image_np)
    cv2.waitKey(1)
    ctypes.windll.user32.SetForegroundWindow(ctypes.windll.user32.GetForegroundWindow())
    time.sleep(duration)
    cv2.destroyAllWindows()

# Display the two images one after another
for url in image_urls:
    show_image(url)
