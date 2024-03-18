# opening the file in write mode using the open() function
inputFile = open("../configurations/tutorialsFile.txt", "w")

# handling the exceptions using try-catch blocks
try:
   # writing text into the file
   text=input("Enter the text")
   inputFile.write(text)
finally:
   # closing the file
   inputFile.close()