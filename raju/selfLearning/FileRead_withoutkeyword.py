# opening the file in Read mode using the open() function
inputFile = open("../configurations/tutorialsFile.txt", "r")

# handling the exceptions using try-catch blocks
try:
   print(inputFile.read())
finally:
   # closing the file
   inputFile.close()