# Booleans represent one of two values: True or False.
print(10 > 9)  # True
print(10 == 9)  # False
print(10 < 9)  # False

# The bool() function allows you to evaluate any value, and give you True or False in return,
"""
   Almost any value is evaluated to True if it has some sort of content.
   Any string is True, except empty strings.
   Any number is True, except 0.
   Any list, tuple, set, and dictionary are True, except empty ones.
"""

# Evaluate a string and a number:
print(bool("Hello"))  # True
print(bool(15))  # True
print(bool(["apple", "cherry", "banana"]))  # True

# values that evaluate to False are (), [], {}, "", the number 0, the value None and the value False.
print(bool(()))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(""))  # False
print(bool(0))  # False
print(bool(None))  # False
print(bool(False))  # False

# Value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))  # False

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int)) # True

# You can create functions that returns a Boolean Value:


def myFunction():
    return True


print(myFunction())  # True

# You can execute code based on the Boolean answer of a function:


def myFunction():
    return True


if myFunction():
    print("YES!")  # YES!
else:
    print("NO!")
