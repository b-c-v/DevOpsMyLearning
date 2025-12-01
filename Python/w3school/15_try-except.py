# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement:
# The try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("An exception occurred")
# Since the try block raises an error, the except block will be executed.

# Without the try block, the program will crash and raise an error:
# print(x) # NameError: name 'x' is not defined

# except can handle specific exception types
try:
    number = int("any_text")
except ValueError:
    print("A ValueError occurred")

# To handle errors correctly, you must first understand which exceptions a statement can raise.
try:
    number = int("any_text")
except Exception as error:
    print(f"Exception type: {type(error).__name__}")  # ValueError
    print(f"Error message: {error}")

# Many Exceptions. You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
# Print one message if the try block raises a NameError and another for other errors:
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")  # Variable x is not defined


# Else. You can use the else keyword to define a block of code to be executed if no errors were raised:
# In this example, the try block does not generate any error:
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")  # Hello Nothing went wrong

# Finally. The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# This can be useful to close objects and clean up resources:
# Try to open and write to a file that is not writable:
# The program can continue, without leaving the file object open.
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    # Something went wrong when opening the file
    print("Something went wrong when opening the file")

# Raise an exception.
# As a Python developer you can choose to throw an exception if a condition occurs.
# To throw (or raise) an exception, use the raise keyword.
# Raise an error and stop the program if x is lower than 0:
x = -1
if x < 0:
    # Exception: Sorry, no numbers below zero
    raise Exception("Sorry, no numbers below zero")

# You can define what kind of error to raise, and the text to print to the user.
# Raise a TypeError if x is not an integer:
x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")


# Raising and handling custom exceptions.
# Custom exceptions must inherit from Exception and except block must reference the exact exception class


class MyCustomError(Exception):
    print("Raised when a value is not of the expected type.")
    pass


try:
    value = "hello"
    if not isinstance(value, int):
        raise MyCustomError("Only integers are allowed")  # raising a Custom Exception
except MyCustomError:  # catching the Custom Exception
    print("A custom type error occurred")
