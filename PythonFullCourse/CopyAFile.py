# copy a file: Copies contents from one file to another
import shutil

source_file = 'Names.txt'
destination_file = 'NamesCopy.txt'

shutil.copyfile(source_file, destination_file)
print(f"Contents of {source_file} copied to {destination_file} successfully!")
