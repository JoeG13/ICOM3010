# write a file: Writing data to a file
file_name = 'output.txt'

with open(file_name, 'w') as file:
    file.write("Hello, Joe!")

print(f"Data written to {file_name} successfully!")
