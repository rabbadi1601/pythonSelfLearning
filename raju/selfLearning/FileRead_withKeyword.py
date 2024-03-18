# opening the file in Read mode using the open() function
with open("../configurations/tutorialsFile.txt", "r") as my_file:
   content=my_file.read()
print(content)