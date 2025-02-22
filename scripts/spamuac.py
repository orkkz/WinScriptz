import ctypes
import sys
import os

def spam_ufc():
    script = sys.argv[0]
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd", None, None, 1)

if __name__ == "__main__":
    for i in range(100):
        spam_ufc()
