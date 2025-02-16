import os
import random

def append_data(file_path, size_mb=100):
    size_bytes = size_mb * 1024 * 1024

    if not os.path.isfile(file_path):
        print("Error: File does not exist.")
        return

    with open(file_path, "ab") as exe_file:
        exe_file.write(os.urandom(size_bytes))
    print(f"Successfully appended {size_mb}MB of random data to {file_path}")
