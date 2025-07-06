# Python has several functions for creating, reading, updating, and deleting files.
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist. Will append to the end of the file
"w" - Write - Opens a file for writing, creates the file if it does not exist. Will overwrite any existing content
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

# To open a file for reading it is enough to specify the name of the file:
# Make sure the file exists, or else you will get an error: No such file or directory:
f = open("0_print.py")

# The code above is the same:
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.
f = open("0_print.py", "rt")


# ***Read Files***
# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("0_print.py", "r")
print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:
"""f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())"""

# ***Read Only Parts of the File***
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
# Return the 5 first characters of the file:
f = open("0_print.py", "r")
print("return only 5 first characters -", f.read(5))

# ***Read Lines***
# You can return one line by using the readline() method:
# Read one line of the file:
f = open("0_print.py", "r")
print(f.readline())

# By calling readline() two times, you can read the two first lines:
f = open("0_print.py", "r")
print("calling two times -", f.readline())
print("calling two times -", f.readline())

# By looping through the lines of the file, you can read the whole file, line by line:
f = open("0_print.py", "r")
for x in f:
    print("loop -", x)


# ***Close Files***
# It is a good practice to always close the file when you are done with it.
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.
f = open("0_print.py", "r")
print(f.readline())
f.close()


# ***Write to an Existing File***
# To write to an existing file, you must add a parameter ("a" or "w") to the open() function:
# Open the file "demofile2.txt" and append content to the file:
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read()) 

# Open the file "demofile.txt" and overwrite the content:
# Note: the "w" method will overwrite the entire file.
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read()) 


# ***Create a New File***
# To create a new file in Python, use the open() method, with one of the following parameters ("x", "a", "w"):
# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

# Create a new file if it does not exist:
f = open("myfile.txt", "w")

# ***Delete a File***
# To delete a file, you must import the OS module, and run its os.remove() function:
import os

os.remove("demofile.txt")
os.remove("demofile2.txt")
os.remove("myfile.txt")
