import requests
import PIL
import io

url = 'https://server.api'
screenshot = PIL.ImageGrab.grab()
img_byte_arr = io.BytesIO()
screenshot.save(img_byte_arr, format='PNG')
img_byte_arr.seek(0)
files = {'file': ('screenshot.png', img_byte_arr, 'image/png')}
response = requests.post(url, files=files)
print(response.json())
