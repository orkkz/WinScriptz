import subprocess

message = "I am watching you."

subprocess.Popen(f'echo {message} > %TEMP%\c.txt && notepad %TEMP%\c.txt', shell=True, text=True)