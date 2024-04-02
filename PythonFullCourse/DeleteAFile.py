# Delete a file: Delete a file from the filesystem
import os

file_name = 'example.txt'
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' deleted successfully!")
else:
    print(f"File '{file_name}' does not exist")
