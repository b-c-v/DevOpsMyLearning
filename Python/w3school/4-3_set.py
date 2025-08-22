# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable, unindexed and do not allow duplicate values.

# Sets are written with curly brackets.
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Sets automatically remove duplicates. Even though you defined the elements in a specific order, Python does not guarantee that they will be stored or printed in that order
unordered = {1, 3, 5, 8, 2, 6, 9, 8, 1, 5, 2, 1, 5}
print("Unordered and without duplicates -", unordered)

# Unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can remove items and add new items.

# Set items can be of any data type. String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:
# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

# Can delete elements from one set using another set
# The - operator performs a set difference, meaning: "Give me all the elements in set1 that are not in set2."
set1 = {1, 5, 7, 9, 3}
set2 = {1, 6, 8, 3, 9}
print("Difference -", set1 - set2)  # {5, 7}
# You can also use the .difference() method, which is functionally the same:
print("Difference -", set1.difference(set2))  # {5, 7}

# Join (concatenation) and multiplication operations don't work with sets.
# print('Concatenate -', set1 + set2)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print('Multiplication -', set1 * set2)  # TypeError: unsupported operand type(s) for *: 'set' and 'set'

# From Python's perspective, sets are defined as objects with the data type 'set': <class 'set'>
myset = {"apple", "banana", "cherry"}
print(type(myset))  # <class 'set'>

# The set() Constructor. It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print("set() constructor -", thisset)

# Sets cannot have two items with the same value.
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
# {'apple', 'banana', 'cherry'}
print("do not allow duplicate values", thisset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
# {True, 2, 'apple', 'cherry', 'banana'}
print("The values True and 1 -", thisset)

# Get the Length of a Set. To determine how many items a set has, use the len() function.
thisset = {"apple", "banana", "cherry"}
print("len() function -", len(thisset))  # 3


# ***Access Set Items***
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print("using a for loop", x)

# Check if "banana" is present in the set:
print('Check if "banana" is present -', "banana" in thisset)  # True


# ***Add Set Items***
# To add one item to a set use the add() method.
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print("add() method -", thisset)  # {'orange', 'banana', 'apple', 'cherry'}

# Add Sets. To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
# {'cherry', 'apple', 'mango', 'banana', 'pineapple', 'papaya'}
print("update() method -", thisset)


# Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
# {'apple', 'orange', 'cherry', 'kiwi', 'banana'}
print("update() method any iterable object -", thisset)


# ***Remove Set Items***
# To remove an item in a set, use the remove(), or the discard() method.
# Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print("remove() method -", thisset)  # {'apple', 'cherry'}

# Remove "banana" by using the discard() method:
# Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print("discard() method -", thisset)  # {'apple', 'cherry'}


# You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
# Remove a random item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print("pop() method", x)
print("pop() method", thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print("clear() method -", thisset)

# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
# print(thisset) #NameError: name 'thisset' is not defined


# ***Loop Sets***
# You can loop through the set items by using a for loop:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print("for loop -", x)

"""
Method                             Description
add()                              Adds an element to the set
clear()                            Removes all the elements from the set
copy()                             Returns a copy of the set
difference()                       Returns a set containing the difference between two or more sets
difference_update()                Removes the items in this set that are also included in another, specified set
discard()                          Remove the specified item
intersection()                     Returns a set, that is the intersection of two other sets (keeps ONLY the duplicates)
intersection_update()              Removes the items in this set that are not present in other, specified set(s)
isdisjoint()                       Returns whether two sets have a intersection or not
issubset()                         Returns whether another set contains this set or not
issuperset()                       Returns whether this set contains another set or not
pop()                              Removes an element from the set
remove()                           Removes the specified element
symmetric_difference()             Returns a set with the symmetric differences of two sets
symmetric_difference_update()      inserts the symmetric differences from this set and another
union()                            Return a set containing the union of sets
update()                           Update the set with the union of this set and others
"""

# ***Join Sets***

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("union() method -", set3)  # {1, 2, 3, 'b', 'a', 'c'}

# joining multiple sets into one new set called set4
set4 = set1 | set2 | set3
print("Joining set: ", set4)

# The update() method inserts the items in set2 into set1:
set1.update(set2)
print("update() method -", set1)  # {1, 'b', 2, 'c', 3, 'a'}
# Note: Both union() and update() will exclude any duplicate items.

# The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print("intersection_update() method -", x)  # {'apple'}

# The intersection() method will return a new set, that only contains the items that are present in both sets.
z = x.intersection(y)
print("intersection() method -", z)  # {'apple'}

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x.symmetric_difference_update(y)
print("symmetric_difference_update() method -", x)  # {'microsoft', 'google'}

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
z = x.symmetric_difference(y)
print("symmetric_difference() method -", z)  # {'apple'}

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)
# {2, 'cherry', 'banana', 'google'}
print("True and 1 are considered the same value -", z)
