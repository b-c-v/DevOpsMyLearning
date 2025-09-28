# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.


# The function changecase is the decorator.
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


# By placing cdchangecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
@changecase
# The function myfunction is the function that gets decorated.
def myfunction():
    return "Hello Sally"


print(myfunction())  # HELLO SALLY


# ***Multiple Decorator Calls***
# A decorator can be called multiple times. Just place the decorator above the function you want to decorate.
# Using the @changecase decorator on two functions:
def changecase(func):
    def myinner():
        return func().upper()

    return myinner


@changecase
def myfunction():
    return "Hello Sally"


@changecase
def otherfunction():
    return "I am speed!"


print(myfunction())  # HELLO SALLY
print(otherfunction())  # I AM SPEED!


# ***Arguments in the Decorated Function***
# Functions that requires arguments can also be decorated, just make sure you pass the arguments to the wrapper function:
# Functions with arguments can also be decorated:
def changecase(func):
    def myinner(x):
        return func(x).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))  # HELLO JOHN


# *args and **kwargs
# Sometimes the decorator function has no control over the arguments passed from decorated function, to solve this problem, add (*args, **kwargs) to the wrapper function, this way the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
# Secure the function with *args and **kwargs arguments:
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return myinner


@changecase
def myfunction(nam):
    return "Hello " + nam


print(myfunction("John"))  # HELLO JOHN


# ***Decorator With Arguments***
# Decorators can accept their own arguments by adding another wrapper level.
# A decorator factory that takes an argument and transforms the casing based on the argument value.
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print("Decorator With Arguments:", myfunction()) # hello linus


# ***Multiple Decorators***
# You can use multiple decorators on one function.
# This is done by placing the decorator calls on top of each other.
# The decorators are called in the order they are specified.
# One decorator for upper case, and one for adding a greeting:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting
def myfunction():
  return "Tobias"

print("Multiple Decorators:", myfunction()) # HELLO TOBIAS HAVE A GOOD DAY!


# ***Preserving Function Metadata***
# Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes.
# Normally, a function's name can be returned with the __name__ attribute:
def myfunction():
  return "Have a great day!"

print("Preserving Function Metadata:", myfunction.__name__) # myfunction

# But, when a function is decorated, the metadata of the original function is lost.
# Try returning the name from a decorated function and you will not get the same result:
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__) # myinner

# To fix this, Python has a built-in function called functools.wraps that can be used to preserve the original function's name and docstring.
# Import functools.wraps to preserve the original function name and docstring.
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print("functools.wraps:", myfunction.__name__) # myfunction