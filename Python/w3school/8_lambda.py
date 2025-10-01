# A lambda function is a small anonymous function.
# Use lambda functions when an anonymous function is required for a short period of time.
# A lambda function can take any number of arguments, but can only have one expression.
"""
lambda arguments: expression
"""

# The expression is executed and the result is returned:

# Add 10 to argument a, and return the result:


def x(a):
    return a + 10


print(x(5))  # 15

# Lambda functions can take any number of arguments:
# Multiply argument a with argument b and return the result:


def x(a, b):
    return a * b


print("Multiply argument -", x(5, 6))

# Summarize argument a, b, and c and return the result:


def x(a, b, c):
    return a + b + c


print("Summarize -", x(5, 6, 2))  # 13

# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:


def myfunc(n):
    return lambda a: a * n


# Use that function definition to make a function that always doubles the number you send in:


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print("doubles the number -", mydoubler(11))  # 22

# Or, use the same function definition to make a function that always triples the number you send in:


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print("triples the number -", mytripler(11))  # 33

# Or, use the same function definition to make both functions, in the same program:


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print("both function -", mydoubler(11))
print("both function -", mytripler(11))
