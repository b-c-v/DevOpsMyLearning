# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
import math
x = min(5, 10, 25)
y = max(5, 10, 25)

print('min() functions -', x)  # 5
print('max() functions -', y)  # 25

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print('abs() function -', x)  # 7.25

# The pow(x, y) function returns the value of x to the power of y (xy).
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print('pow(x, y) function -', x)  # 64

# The Math Module which extends the list of mathematical functions.
# To use it, you must import the math module: import math
# When you have imported the math module, you can start using methods and constants of the module.

# The math.sqrt() method for example, returns the square root of a number:
x = math.sqrt(64)
print('math.sqrt() method -', x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
x = math.ceil(1.4)
y = math.floor(1.4)

print('math.ceil() method -', x)  # 2
print('math.ceil() method -', y)  # 1

# The math.pi constant, returns the value of PI (3.14...):
x = math.pi
print('math.pi constant -', x)  # 3.141592653589793
