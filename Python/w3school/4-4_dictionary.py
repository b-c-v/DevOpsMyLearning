# Dictionaries are used to store data values in key: value pairs.
# Dictionary items are presented in key: value pairs, and can be referred to by using the key name.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
# Changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# The values in dictionary items can be of any data type. String, int, boolean, and list data types:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# From Python's perspective, dictionaries are defined as objects with the data type 'dict': <class 'dict' >
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))  # <class 'dict'>

# It is also possible to use the dict() constructor to make a dictionary.
thisdict = dict(name="John", age=36, country="Norway")
# {'name': 'John', 'age': 36, 'country': 'Norway'}
print('dict() constructor -', thisdict)

# Dictionaries cannot have two items with the same key. Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print('Duplicate -', thisdict)

# Dictionary Length. To determine how many items a dictionary has, use the len() function:
print('len() function -', len(thisdict))  # 3


# ***Access Dictionary Items***

# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print('referring to its key name -', x)  # Mustang

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print('get() method -', x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print('keys() method -', x)  # dict_keys(['brand', 'model', 'year'])

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print('before the change -', x)  # dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
# dict_keys(['brand', 'model', 'year', 'color'])
print('after the change the keys list gets updated -', x)

# Get Values
# The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print('values() method -', x)  # dict_values(['Ford', 'Mustang', 1964])

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print('before the change -', x)  # dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
# dict_values(['Ford', 'Mustang', 2020])
print('after the change the values list gets updated -', x)

# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print('before the change -', x)  # dict_values(['Ford', 'Mustang', 1964])
car["color"] = "red"
# dict_values(['Ford', 'Mustang', 1964, 'red'])
print('Add a new item the values list gets updated -', x)

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# Get a list of the key:value pairs
x = thisdict.items()
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print('items() method -', x)

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print('before the change -', x)
car["year"] = 2020
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
print('Make a change in the original dictionary -', x)

# Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
print('before the change -', x)
car["color"] = "red"
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])
print('Add a new item to the original dictionary -', x)

"""
Method          Description
clear()         Removes all the elements from the dictionary
copy()          Returns a copy of the dictionary
fromkeys()      Returns a dictionary with the specified keys and value
get()           Returns the value of the specified key
items()         Returns a list containing a tuple for each key value pair
keys()          Returns a list containing the dictionary's keys
pop()           Removes the element with the specified key
popitem()       Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()        Updates the dictionary with the specified key-value pairs
values()        Returns a list of all the values in the dictionary
"""

# Check if Key Exists.
# To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# ***Change Dictionary Items***

# Change Values. You can change the value of a specific item by referring to its key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
print('change the value by referring to key name -', thisdict)

# Update Dictionary. The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
# {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print('update() method -', thisdict)


# ***Add Dictionary Items***

# Adding Items. Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
print('using a new index key and assigning a value -', thisdict)

# Update Dictionary. The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
print('update() method -', thisdict)


# ***Remove Dictionary Items***

# The pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print('pop() method -', thisdict)  # {'brand': 'Ford', 'year': 1964}

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print('popitem() method -', thisdict)  # {'brand': 'Ford', 'model': 'Mustang'}

# The del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
# {'brand': 'Ford', 'year': 1964}
print('del keyword removes the item -', thisdict)

# The del keyword can also delete the dictionary completely:
del thisdict
# print(thisdict)  # this will cause an error because "thisdict" no longer exists. NameError: name 'thisdict' is not defined

# The clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print('clear() method -', thisdict)  # {}


# ***Loop Dictionaries***

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
# Print all key names in the dictionary, one by one:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print('for loop keys -', x)  # brand model year

# Print all values in the dictionary, one by one:
for x in thisdict:
    print('for loop values -', thisdict[x])  # Ford Mustang 1964

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print('values() method -', x)  # Ford Mustang 1964

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print('keys() method -', x)  # brand model year

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    # brand Ford model Mustang year 1964
    print('Loop through keys and values -', x, y)


# ***Copy Dictionaries***

# Copy a Dictionary. You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# Make a copy of a dictionary with the copy() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print('copy() method -', mydict)

# Make a copy of a dictionary with the dict() function:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print('dict() function -', mydict)

# ***Nested Dictionaries***

# A dictionary can contain dictionaries, this is called nested dictionaries.
# Create a dictionary that contain three dictionaries:
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

# Or, if you want to add three dictionaries into a new dictionary:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Print the name of child 2:
print(myfamily["child2"]["name"])  # Tobias
