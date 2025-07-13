# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)  # ('apple', 'banana', 'cherry')

# Tuple Items - Data Types. Tuple items can be of any data type: String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

# From Python's perspective, tuples are defined as objects with the data type 'tuple': <class 'tuple'>
mytuple = ("apple", "banana", "cherry")
print("tuples are defined as objects with the data type -",
      type(mytuple))  # <class 'tuple'>

# The tuple() Constructor. It is also possible to use the tuple() method to make a tuple.
# note the double round-brackets
thistuple = tuple(("apple", "banana", "cherry"))
print("tuple() method -", thistuple)


# ***Tuple Items***
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
# Tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# Allow Duplicates - they can have items with the same value:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length. To determine how many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print("len() function -", len(thistuple))  # 3

# Create Tuple With One Item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)  # One item tuple, remember the comma
print("One item tuple -", type(thistuple))


# ***Access Tuple Items***
# You can access tuple items by referring to the index number, inside square brackets:
# Note: The first item has index 0.
thistuple = ("apple", "banana", "cherry")
print("access tuple items -", thistuple[1])  # banana

# Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
print("Negative indexing -", thistuple[-1])  # cherry

# Range of Indexes. You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print("Range of Indexes -", thistuple[2:5])  # ('cherry', 'orange', 'kiwi')
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to, but NOT included, "kiwi":
# ('apple', 'banana', 'cherry', 'orange')
print("leaving out the start value -", thistuple[:4])

# By leaving out the end value, the range will go on to the end of the list:
# This example returns the items from "cherry" and to the end:
# ('cherry', 'orange', 'kiwi', 'melon', 'mango')
print("leaving out the end value -", thistuple[2:])

# Range of Negative Indexes. Specify negative indexes if you want to start the search from the end of the tuple:
# This example returns the items from index -4 (included) to index -1 (excluded)
# ('orange', 'kiwi', 'melon')
print("Range of Negative Indexes -", thistuple[-4:-1])

# Check if Item Exists. To determine if a specified item is present in a tuple use the in keyword:
if "apple" in thistuple:
    # Yes, 'apple' is in the fruits tuple
    print("Yes, 'apple' is in the fruits tuple")


# ***Update Tuples***
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print("Convert the tuple into a list -", x)  # ('apple', 'kiwi', 'cherry')

# Add Items.
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print("Add Items -", thistuple)  # ('apple', 'banana', 'cherry', 'orange')


# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:
# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
y = ("orange",)
thistuple += y
# ('apple', 'banana', 'cherry', 'orange', 'orange')
print("Add tuple to a tuple -", thistuple)

# Remove Items. Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print("Remove Items -", thistuple)  # ('banana', 'cherry')

# Or you can delete the tuple completely. The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # this will raise an error because the tuple no longer exists

# ***Unpack Tuples***
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print("Unpack Tuples -", green)
print("Unpack Tuples -", yellow)
print("Unpack Tuples -", red)

# Using Asterisk *
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print("Using Asterisk -", green)  # apple
print("Using Asterisk -", yellow)  # banana
print("Using Asterisk -", red)  # ['cherry', 'strawberry', 'raspberry']


# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print("asterisk is added to another variable -", green)  # apple
# ['mango', 'papaya', 'pineapple']
print("asterisk is added to another variable -", tropic) # ['mango', 'papaya', 'pineapple']
print("asterisk is added to another variable -", red)  # cherry

# ***Loop Tuples***
# Loop Through a Tuple by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print('for loop', x)

# Loop Through the Index Numbers by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print('len() functions and for -', thistuple[i])

# Using a While Loop
# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    i = i + 1

# Join Tuples
# To join (concatenate) two or more tuples you can use the + operator:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print('Join Tuples -', tuple3)  # ('a', 'b', 'c', 1, 2, 3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
# ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
print('Multiply Tuples -', mytuple)

"""
***Tuple Methods***
Python has two built-in methods that you can use on tuples.

count()    Returns the number of times a specified value occurs in a tuple
index()    Searches the tuple for a specified value and returns the position of where it was found
"""