# module to be the same as a code library.
# A file containing a set of functions you want to include in your application.
# To create a module just save the code you want in a file with the file extension .py

# we can use the module we just created, by using the import statement:
import mymodule
# You can create an alias when you import a module, by using the as keyword:
# Create an alias for mymodule called mx:
import mymodule as mx
# Import From Module. You can choose to import only parts from a module, by using the from keyword.
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]
# Import only the person1 dictionary from the module:
from mymodule import person1
# There are several built-in modules in Python, which you can import whenever you like.
# Import and use the platform module:
import platform


# When using a function from a module, use the syntax: module_name.function_name.
mymodule.greeting("Jonathan")  # Hello, Jonathan

# The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)
a = mymodule.person1["age"]
print(a)  # 36

# use alias for mymodule called mx
a = mx.person1["age"]
print(a)

# use the platform module
x = platform.system()
print(x)

# Using the dir() Function. There is a built-in dir() function to list all the function names (or variable names) in a module.
# The dir() function can be used on all modules, also the ones you create yourself.
# List all the defined names belonging to the platform module:
x = dir(platform)
print(x)
