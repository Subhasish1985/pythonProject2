'''
Create a note-taking program. When a user starts it up, it should prompt them for a filename.
If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file.
 After they enter the text, it should save the file and exit.
If they enter a file name that already exists, it should ask the user if they want:
A) Read the file
B) Delete the file and start over
C) Append the file
If the user wants to read the file it should simply show the contents of the file on the screen.
If the user wants to start over then the file should be deleted and another empty one made in its place.
If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file.
Extra Credit:
Allow the user to select a 4th option:
D) Replace a single line
If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
1) The line number they want to update.
2) The text that should replace that line.
'''
# import os package to remove the file
#import os

# prompt them for a filename.

fileName = input("Please enter a file name:\n")

# trying to open a non-existing file name


# print(" If the file doesn't exists.Please create a new file:\n")

# fileOpenWrite = open(fileName, "w")

# fileOpenWrite.write("Name:Subhasish")

# fileOpenWrite.close()


# ******Reading the existing file

'''
fileOpenRead = open(fileName, "r")
print(fileOpenRead.readline())
fileOpenRead.close()
'''
# ******deleting the file
'''
if os.path.exists("hola.txt"):
    os.remove("hola.txt")
else:
    print("The file does not exist")
'''

# creating and writing in the file
'''
fileOpenWrite = open(fileName, "w")
fileOpenWrite.write("Hello Everyone...How Are you doing\n")
fileOpenWrite.close()
'''


#fileOpenWrite1 = open(fileName, "a")
#fileOpenWrite1.write("My name is Subhasish.Nice to  meet you")
#fileOpenWrite1.close()

# prints appended values to the file.
fileOpenRead = open(fileName, "r")
print(fileOpenRead.read())

fileOpenRead.close()


