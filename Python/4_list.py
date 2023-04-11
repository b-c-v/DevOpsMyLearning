# Python Collections (Arrays)

# There are four collection data types in the Python programming language:
"""
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# List
"""
   Lists are used to store multiple items in a single variable.
   Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
   List items are ordered, changeable, and allow duplicate values.
   List items are indexed, the first item has index [0], the second item has index [1] etc.
   Ordered, it means that the items have a defined order, and that order will not change.
   If you add new items to a list, the new items will be placed at the end of the list.
   Note: There are some list methods that will change the order, but in general: the order of the items will not change.
   Changeable, meaning that we can change, add, and remove items in a list after it has been created.
   Allow Duplicates. Since lists are indexed, lists can have items with the same value
"""

# From Python's perspective, lists are defined as objects with the data type 'list': <class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))  # <class 'list'>

# It is also possible to use the list() constructor when creating a new list.
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)  # ['apple', 'banana', 'cherry']

# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))   # 3

# List items can be of any data type:
# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
