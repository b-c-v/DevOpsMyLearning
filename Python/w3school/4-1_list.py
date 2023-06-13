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
"""
Списки в Python аналогичны массивам в других языках программирования. Однако разница между списками и массивами все же существует. Элементы массива всегда имеют одинаковый тип данных и располагаются в памяти компьютера непрерывным блоком, а элементы списка могут быть разбросаны по памяти как угодно и могут иметь разный тип данных.
При выводе содержимого списка с помощью функции print() слова выводятся в кавычках, цифры без кавычек, но всё будет в  квадратных скобках.
"""
# From Python's perspective, lists are defined as objects with the data type 'list': <class 'list'>
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(type(thislist))  # <class 'list'>

# It is also possible to use the list() constructor when creating a new list.
# note the double round-brackets
mylist = list(("apple", "banana", "cherry"))
print('use the list()', mylist)  # ['apple', 'banana', 'cherry']

"""
Создать пустой список можно двумя способами:
- Использовать пустые квадратные скобки [];
- Использовать встроенную функцию, которая называется list.
"""
mylist = []       # пустой список
mylist = list()   # пустой список

# List items can be of any data type:
# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

# Преобразование строки в список:
s = 'abcde'
chars = list(s)  # список содержит символы 'a', 'b', 'c', 'd', 'e'

# To determine how many items a list has, use the len() function:
print('len() is ', len(thislist))   # 7


# ***Access List Items***
# List items are indexed and you can access them by referring to the index number:
print('referring to the index -', thislist[1])       # banana

# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
print('negative indexing -', thislist[-1])           # mango

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# The search will start at index 2 (included) and end at index 5 (not included).
# ['cherry', 'orange', 'kiwi']
print('range of indexes -', thislist[2:5])

# By leaving out the start value, the range will start at the first item:
# This example returns the items from the beginning to, but NOT including, "kiwi":

# ['apple', 'banana', 'cherry', 'orange']
print('leaving out the start value -', thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:
# ["cherry", "orange", "kiwi", "melon", "mango"]
print('leaving out the end value -', thislist[2:])

# Изменение целого диапазона элементов списка.
fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2:5] = ['банан', 'вишня', 'киви']
print(fruits)  # ['apple', 'apricot', 'банан', 'вишня', 'киви', 'lemon', 'mango']

# Specify negative indexes if you want to start the search from the end of the list:
# ['orange', 'kiwi', 'melon']
print('Range of Negative Indexes -', thislist[-4:-1])

# To determine if a specified item is present in a list use the in keyword:
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# ***Change List Items***
# To change the value of a specific item, refer to the index number:
thislist[1] = "blackcurrant"
# ['apple', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'melon', 'mango']
print('Change Item Value -', thislist)

# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist[5:7] = ["blackcurrant", "watermelon"]
# ['apple', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'blackcurrant', 'watermelon']
print('Change a Range of Item Values -', thislist)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# The length of the list will change when the number of items inserted does not match the number of items replaced.
# Change the first value by replacing it with two new values:
thislist[0:1] = ["blackcurrant", "watermelon"]
# ['blackcurrant', 'watermelon', 'blackcurrant', 'cherry', 'orange', 'kiwi', 'blackcurrant', 'watermelon']
print('insert more items than you replace -', thislist)

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
# Change the second and 8 value by replacing it with one value:
thislist[1:8] = ["watermelon"]
print('insert less items than you replace -', thislist)  # ['blackcurrant', 'watermelon']

"""
List Methods
Python has a set of built-in methods that you can use on lists.
Method         Description
append()       Adds an element at the end of the list
clear()        Removes all the elements from the list
copy()         Returns a copy of the list
count()        Returns the number of elements with the specified value
extend()       Add the elements of a list (or any iterable), to the end of the current list
index()        Returns the index of the first element with the specified value
insert()       Adds an element at the specified position
pop()          Removes the element at the specified position
remove()       Removes the item with the specified value
reverse()      Reverses the order of the list
sort()         Sorts the list
"""


# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
# The insert() method inserts an item at the specified index:
# Insert "watermelon" as the third item:
thislist.insert(2, "watermelon")
# ['blackcurrant', 'watermelon', 'watermelon'] Note: As a result, the list will now contain 3 items.
print('Insert Items insert() method -', thislist)


# ***Add List Items***
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print('append() method -', thislist)  # ['apple', 'banana', 'cherry', 'orange']

"""
Нельзя использовать индексаторы для установки значений элементов списка, если список пустой. 
numbers = []  # создаем пустой список
numbers[0] = 1
numbers[1] = 2
numbers[2] = 3
print(numbers) # IndexError: list assignment index out of range
"""

# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist. The elements will be added to the end of the list:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print('extend() method -', thislist) # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object(tuples, sets, dictionaries etc.).
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
# ['apple', 'banana', 'cherry', 'kiwi', 'orange']
print('extend() method add any iterable object -', thislist)


# Отличие между методами append() и extend() проявляется при добавлении строки к списку.
# Метод append() добавляет строку 'python' целиком к списку, а метод extend() разбивает строку 'python' на  символы 'p', 'y', 't', 'h', 'o', 'n' и их добавляет в качестве элементов списка. 
words1 = ['be', 'happy', 'learn']
words2 = ['be', 'happy', 'learn']
words1.append('python')
words2.extend('python')
print(words1)   # ['be', 'happy', 'learn', 'python']
print(words2)   # ['be', 'happy', 'learn', 'p', 'y', 't', 'h', 'o', 'n']


# Insert Items
# To insert a list item at a specified index, use the insert() method.
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print('insert() method -', thislist)  # ['apple', 'orange', 'banana', 'cherry']
# Note: As a result of the examples above, the lists will now contain 4 items.

# ***Remove List Items***
# Remove Specified Item. The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print('remove() method -', thislist)  # ['apple', 'cherry']

# Remove Specified Index. The pop() method removes the specified index.
# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print('pop() method removes -', thislist)  # ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print('do not specify the index, the pop() -', thislist)  # ['apple', 'banana']

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]  # Remove the first item:
print('del keyword -', thislist)  # ['banana', 'cherry']

# Оператор del работает и со срезами: мы можем удалить целый диапазон элементов списка.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7]    # удаляем элементы с 2 по 6 включительно
print('del -', numbers) # del - [1, 2, 8, 9]

# удалить все элементы на четных позициях (0, 2, 4, ...) исходного списка.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]
print('del -', numbers)   # del - [2, 4, 6, 8]

# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist  # Delete the entire list:

# Clear the List
# The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print('clear() method -', thislist)

# ***Loop Lists***
# Loop Through a List. You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:  # Print all items in the list, one by one:
    print('Loop Through a List -', x)

# Loop Through the Index Numbers. You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print('Loop Through the Index Numbers -', thislist[i])

# Using a While Loop. You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print('using a while loop -', thislist[i])
    i = i + 1  # Remember to increase the index by 1 after each iteration.

# ***List Comprehension***
# Looping Using List Comprehension. List Comprehension offers the shortest syntax for looping through lists:
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print('List Comprehension -', x) for x in thislist]

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print('Without list comprehension', newlist)

# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print('With list comprehension', newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.

# Condition. The condition is like a filter that only accepts the items that valuate to True.
# Only accept items that are not "apple". The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".:
newlist = [x for x in fruits if x != "apple"]


# The condition is optional and can be omitted:
# With no if statement:
newlist = [x for x in fruits]

# Iterable. The iterable can be any iterable object, like a list, tuple, set etc.
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# Same example, but with a condition:
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]

# Expression. The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

# You can set the outcome to whatever you like:
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Return "orange" instead of "banana". "Return the item if it is not banana, if it is banana return orange":
newlist = [x if x != "banana" else "orange" for x in fruits]

# ***Sort Lists***
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
# ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
print('Sort the list alphabetically', thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print('Sort the list numerically -', thislist)  # [23, 50, 65, 82, 100]

# Sort Descending. To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
# ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
print('Sort Descending -', thislist)

# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print('Sort the list descendin -', thislist)  # [100, 82, 65, 50, 23]

# Customize Sort Function. You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):


def myfunc(n):
    return abs(n - 50)  # Sort the list based on how close the number is to 50:


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print('Customize Sort Function -', thislist)  # [50, 65, 23, 82, 100]

# Case Insensitive Sort. By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
# ['Kiwi', 'Orange', 'banana', 'cherry']
print('Case Insensitive Sort -', thislist)

# We can use built-in functions as key functions when sorting a list. If you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print('use str.lower -', thislist)  # ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order. The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print('reverse() method -', thislist)  # ['cherry', 'Kiwi', 'Orange', 'banana']

# ***Copy Lists***
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print('copy() method -', mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print('list() method -', mylist)

# ***Join Lists***
# There are several ways to join, or concatenate, two or more lists.
# by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print('using the + operator -', list3)  # ['a', 'b', 'c', 1, 2, 3]

# Для генерации списков, состоящих строго из повторяющихся элементов, умножение на число — самый короткий и правильный метод.
print([1, 2, 3, 4] + [5, 6, 7, 8]) # [1, 2, 3, 4, 5, 6, 7, 8]
print([7, 8] * 3) # [7, 8, 7, 8, 7, 8]

# Можно использовать расширенные операторы += и *= при работе со списками.
a = [1, 2, 3, 4]
b = [7, 8]
a += b
b *= 5 
print(a)  # [1, 2, 3, 4, 7, 8]
print(b)  # [7, 8, 7, 8, 7, 8, 7, 8, 7, 8]

# by appending all the items from list2 into list1, one by one:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print('appending all the item -', list1)  # ['a', 'b', 'c', 1, 2, 3]

# use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print('the extend() method -', list1)  # ['a', 'b', 'c', 1, 2, 3]

# Встроенная функция sum() принимает в качестве параметра список чисел и вычисляет сумму его элементов.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Сумма всех элементов списка =', sum(numbers)) # Сумма всех элементов списка = 55

# Встроенные функции min() и max() принимают в качестве параметра список и находят минимальный и максимальный элементы соответственно.
numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))   # Минимальный элемент = -7
print('Максимальный элемент =', max(numbers))  # Максимальный элемент = 3333

# Отличие списков от строк: строки — неизменяемые объекты, а списки – изменяемые.
# строка
# s = 'abcdefg'
# s[1] = 'x'    # пытаемся изменить 2 символ (по индексу 1) строки 
# приводит к ошибке: object does not support item assignment

# список
# изменять отдельные символы строк нельзя, однако можно изменять отдельные элементы списков. Для этого используем индексатор и оператор присваивания.
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[1] = 101     # изменяем 2 элемент (по индексу 1) списка
print(numbers) # [1, 101, 3, 4, 5, 6, 7]
