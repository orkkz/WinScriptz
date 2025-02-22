from fernet import Fernet
import base64

def generate_key():
    return Fernet.generate_key()

def encrypt(key, data):
    cipher_suite = Fernet(key)
    return cipher_suite.encrypt(data.encode())

def to_base64(data):
    return base64.b64encode(data).decode()