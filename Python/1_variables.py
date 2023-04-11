# https://www.w3schools.com/python/default.asp
# Comments start with #
# Comments can be placed at the end of a line, and Python will ignore the rest of the line

print("Hello, World!")

"""
Python does not really have a syntax for multiline comments.
You can use a multiline string.
Add a multiline string (triple quotes) in your code, and place your comment inside it
"""

# Python uses indentation to indicate a block of code. Python will give you an error if you skip the indentation
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5 > 2:
    print("Five is greater than two!")

# Python has no command for declaring a variable.
# Variable names are case-sensitive.
# A variable is created the moment you first assign a value to it.
y = "Hello, World!"
X = "Case-sensitive variable"
x = 5  # x will not overwrite X

print(x)
print(y)
print(X)

"""
    Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords: and, as, assert, def, del, False etc.
"""
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# There are several techniques you can use to make them more readable:
# Camel Case - Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case - Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case - Each word is separated by an underscore character:
my_variable_name = "John"

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = "Hello World"                                # x is of type str
x = 20                                           # x is of type int
x = 20.5                                         # x is of type float
x = 1j                                           # x is of type complex
x = ["apple", "banana", "cherry"]                # x is of type list
x = ("apple", "banana", "cherry")                # x is of type tuple
x = range(6)                                     # x is of type range
x = {"name": "John", "age": 36}                  # x is of type dict
x = {"apple", "banana", "cherry"}                # x is of type set
x = frozenset({"apple", "banana", "cherry"})     # x is of type frozenset
x = True                                         # x is of type bool
x = b"Hello"                                     # x is of type bytes
x = bytearray(5)                                 # x is of type bytearray
x = memoryview(bytes(5))                         # x is of type memoryview
x = None                                         # x is of type NoneType

# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")                           # x is of type str
x = int(20)                                      # x is of type int
x = float(20.5)                                  # x is of type float
x = complex(1j)                                  # x is of type complex
x = list(("apple", "banana", "cherry"))          # x is of type list
x = tuple(("apple", "banana", "cherry"))         # x is of type tuple
x = range(6)                                     # x is of type range
x = dict(name="John", age=36)                    # x is of type dict
x = set(("apple", "banana", "cherry"))           # x is of type set
x = frozenset(("apple", "banana", "cherry"))     # x is of type frozenset
x = bool(5)                                      # x is of type bool
x = bytes(5)                                     # x is of type bytes
x = bytearray(5)                                 # x is of type bytearray
x = memoryview(bytes(5))                         # x is of type memoryview

# Casting If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

# Get the Type. You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry

# In the print() function, you output multiple variables, separated by a comma:
print(x, y, z)  # apple banana cherry

# You can also use the + operator to output multiple variables. For numbers, the + character works as a mathematical operator
print(x + y + z)  # applebananacherry

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error: print(int1 + string1)
# To output multiple variables in the print() function is to separate them with commas, which even support different data types
int1 = 4
string1 = "What is your experience?"
print(string1, int1)


# We can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
# Use the format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # My name is John, and I am 36


# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
# I want 3 pieces of item 567 for 49.95 dollars.
print(myorder.format(quantity, itemno, price))


# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# I want to pay 49.95 dollars for 3 pieces of item 567.
print(myorder.format(quantity, itemno, price))


# Global Variables - variables that are created outside of a function. Global variables can be used by everyone, both inside of functions and outside.
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()  # Python is fantastic
print("Python is " + x)  # Python is awesome


# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()  # Python is fantastic
print("Python is " + x)  # Python is fantastic

"""
    Python has the following data types built-in by default, in these categories:
    Text Type:  str
    Numeric Types:  int, float, complex
    Sequence Types:  list, tuple, range
    Mapping Type:  dict
    Set Types:  set, frozenset
    Boolean Type:  bool
    Binary Types:  bytes, bytearray, memoryview
    None Type:  NoneType
"""

# You can convert from one type to another with the int(), float(), and complex() methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# convert from int to float:
a = float(x)        # 1.0
# convert from float to int:
b = int(y)          # 2
# convert from int to complex:
c = complex(x)      # (1+0j)

# Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Import the random module, and display a random number between 1 and 9:
"""
import random
print(random.randrange(1, 10))
"""

# String variables can be declared either by using single or double quotes
x = "John"
# is the same as
x = 'John'
# You can assign a multiline string to a variable by using three quotes """   """ Or three single quotes ''' ...  ''':
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):
b = "Hello, World!"
print(b[1])      # e

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Get the characters from position 2 to position 5 (not included):
print(b[2:5])    # llo

# Get the characters from the start to position 5 (not included):
print(b[:5])     # Hello

# Get the characters from position 2, and all the way to the end:
print(b[2:])     # llo, World!

# Use negative indexes to start the slice from the end of the string:
# Get the characters From: "o" in "World!" (position - 5) To, but not included: "d" in "World!" (position - 2):
print(b[-5:-2])  # orl

# we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)
# To get the length of a string, use the len() function.
print(len(b))  # 13


"""
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.
Method             Description
capitalize()       Converts the first character to upper case
casefold()         Converts string into lower case
center()           Returns a centered string
count()            Returns the number of times a specified value occurs in a string
encode()           Returns an encoded version of the string
endswith()         Returns true if the string ends with the specified value
expandtabs()       Sets the tab size of the string
find()             Searches the string for a specified value and returns the position of where it was found
format()           Formats specified values in a string
format_map()       Formats specified values in a string
index()            Searches the string for a specified value and returns the position of where it was found
isalnum()          Returns True if all characters in the string are alphanumeric
isalpha()          Returns True if all characters in the string are in the alphabet
isdecimal()        Returns True if all characters in the string are decimals
isdigit()          Returns True if all characters in the string are digits
isidentifier()     Returns True if the string is an identifier
islower()          Returns True if all characters in the string are lower case
isnumeric()        Returns True if all characters in the string are numeric
isprintable()      Returns True if all characters in the string are printable
isspace()          Returns True if all characters in the string are whitespaces
istitle()          Returns True if the string follows the rules of a title
isupper()          Returns True if all characters in the string are upper case
join()             Joins the elements of an iterable to the end of the string
ljust()            Returns a left justified version of the string
lower()            Converts a string into lower case
lstrip()           Returns a left trim version of the string
maketrans()        Returns a translation table to be used in translations
partition()        Returns a tuple where the string is parted into three parts
replace()          Returns a string where a specified value is replaced with a specified value
rfind()            Searches the string for a specified value and returns the last position of where it was found
rindex()           Searches the string for a specified value and returns the last position of where it was found
rjust()            Returns a right justified version of the string
rpartition()       Returns a tuple where the string is parted into three parts
rsplit()           Splits the string at the specified separator, and returns a list
rstrip()           Returns a right trim version of the string
split()            Splits the string at the specified separator, and returns a list
splitlines()       Splits the string at line breaks and returns a list
startswith()       Returns true if the string starts with the specified value
strip()            Returns a trimmed version of the string
swapcase()         Swaps cases, lower case becomes upper case and vice versa
title()            Converts the first character of each word to upper case
translate()        Returns a translated string
upper()            Converts a string into upper case
zfill()            Fills the string with a specified number of 0 values at the beginning
"""

# The upper() method returns the string in upper case:
print(b.upper())  # HELLO, WORLD!

# The lower() method returns the string in lower case:
print(b.lower())  # hello, world!

# The replace() method replaces a string with another string:
print(b.replace("H", "J"))  # Jello, World!


# The split() method returns a list where the text between the specified separator becomes the list items.
print(b.split(","))  # ['Hello', ' World!']


# The strip() method removes any whitespace from the beginning or the end the actual text:
a = "   strip method   "
print(a.strip())  # "strip method"

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text
txt = "The best things in life are free!"
print("free" in txt)  # True

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)  # True

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)  # HelloWorld

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World

# To insert characters that are illegal in a string, use an escape character - is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # We are the so-called "Vikings" from the north.
"""
   Other escape characters used in Python:
     \'      Single Quote
     \\      Backslash
     \n      New Line
     \r      Carriage Return
     \t      Tab
     \b      Backspace
     \f      Form Feed
     \ooo    Octal value
     \xhh    Hex value
"""
