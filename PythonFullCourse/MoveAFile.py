# move a file: Move a file from one location to another
import shutil

source_file = 'source.txt'
destination_directory = 'destination_folder'

shutil.move(source_file, destination_directory)
print(f"File '{source_file}' moved to '{destination_directory}' successfully!")
