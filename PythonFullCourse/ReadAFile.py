# read a file: Reading the contents of a file
file_name = 'source.txt'

with open(file_name, 'r') as file:
    content = file.read()
    print("File content:")
    print(content)
