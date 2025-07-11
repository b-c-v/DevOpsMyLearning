# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# to work with arrays in Python you will have to import a library, like the NumPy library.
# Arrays are used to store multiple values in one single variable:

# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]


# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
# If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:
car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
# The solution is an array!
# An array can hold many values under a single name, and you can access the values by referring to an index number.

# Access the Elements of an Array. You refer to an array element by referring to the index number.
# Get the value of the first array item:
x = cars[0]

# Modify the value of the first array item:
cars[0] = "Toyota"

# The Length of an Array. Use the len() method to return the length of an array (the number of elements in an array).
# Note: The length of an array is always one more than the highest array index.

x = len(cars)
print("len() -", x)  # 3

# Looping Array Elements. You can use the for in loop to loop through all the elements of an array.
# Print each item in the cars array:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(" Looping Array -", x)

"""
Array Methods
Python has a set of built-in methods that you can use on lists/arrays.
Method      Description
append()    Adds an element at the end of the list
clear()     Removes all the elements from the list
copy()      Returns a copy of the list
count()     Returns the number of elements with the specified value
extend()    Add the elements of a list (or any iterable), to the end of the current list
index()     Returns the index of the first element with the specified value
insert()    Adds an element at the specified position
pop()       Removes the element at the specified position
remove()    Removes the first item with the specified value
reverse()   Reverses the order of the list
sort()      Sorts the list
"""

# Adding Array Elements. You can use the append() method to add an element to an array.
# Add one more element to the cars array:
cars.append("Honda")
print("append() method -", cars)  # ['Ford', 'Volvo', 'BMW', 'Honda']

# Removing Array Elements. You can use the pop() method to remove an element from the array.
# Delete the second element of the cars array:
cars.pop(1)
print("pop() method -", cars)  # ['Ford', 'BMW', 'Honda']


# You can also use the remove() method to remove an element from the array.
# Note: The list's remove() method only removes the first occurrence of the specified value.

cars.remove("Honda")
print("remove() -", cars)  # ['Ford', 'BMW']

# Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print("insert() -", fruits)  # ['apple', 'lemon', 'banana', 'cherry']
