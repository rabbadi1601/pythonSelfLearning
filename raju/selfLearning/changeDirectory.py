import os
from pathlib import Path

# Get the current directory
full_path = os.getcwd()
print(full_path)
print(Path(full_path).parents[0])
print(Path(full_path).parents[1])
print(Path(full_path).parents[2])
print("parents[3]",Path(full_path).parents[3])



# Create a new file path
new_file_path = str(Path(full_path).parents[2])+"/"+"new_file.txt"

print('New File Path:', new_file_path)
with open(new_file_path, "w") as new_file:
    new_file.write("Hello Raju how r u")


