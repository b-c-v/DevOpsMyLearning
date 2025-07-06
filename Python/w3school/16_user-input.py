# Python allows for user input.
# That means we are able to ask the user for input.
# Python stops executing when it comes to the input() function, and continues when the user has given some input.

# The method is a bit different in Python 3.6 than Python 2.7.
# Python 3.6 uses the input() method.
# Python 2.7 uses the raw_input() method.

# The following example asks for the username, and when you entered the username, it gets printed on the screen:
# Python 3.6
username = input("Enter username: ")
print("Username is: " + username)
# Another way to print, and here no space is needed after :
print("Username is:", username)
# Ещё один способ вывода данных: функция input() используется прямо внутри print()
print("Username is:", input("Enter your name: "))

# Python 2.7
# username = raw_input("Enter username:")
# print("Username is: " + username)

# ***Multiple Inputs***
# You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:
name = input("Enter your name: ")
print(f"Hello {name}")
fav1 = input("What is your favorite animal: ")
fav2 = input("What is your favorite color: ")
fav3 = input("What is your favorite number: ")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# ***Input number***
# The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string. You can convert the input into a number with the float() function:
# To find the square root, the input has to be converted into a number:
import math

x = input("Enter a number: ")
# find the square root of the number:
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")

# ***Validate input***
# It is a good practice to validate any input from the user. In the example above, an error will occur if the user inputs something other than a number.
# To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again", and allowed to make a new input:
y = True
while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")

print("Thank you!")



