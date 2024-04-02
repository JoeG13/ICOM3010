# File detection: Check if a file exists
import os

file_name = 'example.txt'
if os.path.exists(file_name):
    print(f"File '{file_name}' exists")
else:
    print(f"File '{file_name}' does not exist")
