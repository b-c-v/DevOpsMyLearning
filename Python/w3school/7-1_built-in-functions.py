"""
abs()              Returns the absolute value of a number
all()              Returns True if all items in an iterable object are true
any()              Returns True if any item in an iterable object is true
ascii()            Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()              Returns the binary version of a number
bool()             Returns the boolean value of the specified object
bytearray()        Returns an array of bytes
bytes()            Returns a bytes object
callable()         Returns True if the specified object is callable, otherwise False
chr()              Returns a character from the specified Unicode code.
classmethod()      Converts a method into a class method
compile()          Returns the specified source as an object, ready to be executed
complex()          Returns a complex number
delattr()          Deletes the specified attribute (property or method) from the specified object
dict()             Returns a dictionary (Array)
dir()              Returns a list of the specified object's properties and methods
divmod()           Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()        Takes a collection (e.g. a tuple) and returns it as an enumerate object. Добавляет к каждому элементу последовательности его индекс (порядковый номер), начиная с 0
eval()             Evaluates and executes an expression
exec()             Executes the specified code (or object)
filter()           Use a filter function to exclude items in an iterable object
float()            Returns a floating point number
format()           Formats a specified value
frozenset()        Returns a frozenset object
getattr()          Returns the value of the specified attribute (property or method)
globals()          Returns the current global symbol table as a dictionary
hasattr()          Returns True if the specified object has the specified attribute (property/method)
hash()             Returns the hash value of a specified object
help()             Executes the built-in help system
hex()              Converts a number into a hexadecimal value
id()               Returns the id of an object
input()            Allowing user input
int()              Returns an integer (decimal) number
isinstance()       Returns True if a specified object is an instance of a specified object
issubclass()       Returns True if a specified class is a subclass of a specified object
iter()             Returns an iterator object
len()              Returns the length of an object
list()             Returns a list
locals()           Returns an updated dictionary of the current local symbol table
map()              Returns the specified iterator with the specified function applied to each item
max()              Returns the largest item in an iterable
memoryview()       Returns a memory view object
min()              Returns the smallest item in an iterable
next()             Returns the next item in an iterable
object()           Returns a new object
oct()              Converts a number into an octal
open()             Opens a file and returns a file object
ord()              Convert an integer representing the Unicode of the specified character
pow()              Returns the value of x to the power of y
print()            Prints to the standard output device
property()         Gets, sets, deletes a property
range()            Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()             Returns a readable version of an object
reversed()         Returns a reversed iterator
round()            Rounds a numbers
set()              Returns a new set object
setattr()          Sets an attribute (property/method) of an object
slice()            Returns a slice object
sorted()           Returns a sorted list
staticmethod()     Converts a method into a static method
str()              Returns a string object
sum()              Sums the items of an iterator
super()            Returns an object that represents the parent class
tuple()            Returns a tuple
type()             Returns the type of an object
vars()             Returns the __dict__ property of an object
zip()              Returns an iterator, from two or more iterators
"""

# ***sorted()***
# function returns a sorted list of the specified iterable object.
# sorted() не меняет оригинальный список, а просто делает отсортированную копию  в отличии от sort()
# You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.
# Note: You cannot sort a list that contains BOTH string values AND numeric values.
"""
sorted(iterable, key=key, reverse=reverse)
iterable - Required. The sequence to sort, list, dictionary, tuple etc.
key - Optional. A Function to execute to decide the order. Default is None.
 key задаёт функцию, которая будет применена к каждому элементу перед попарным сравнением (большинство видов сортировок,
 включая timsort, основано на попарном сравнении элементов), например, key=str задаёт в качестве ключа функцию str которая
 будет переводить числа в строки перед сравнением. Это может быть не только встроенная функция, но и функция объявленная пользователем, включая лямбда-функции. Важно только, чтобы это была функция одного параметра, соответствующего типу элемента, например, key=len выдаст ошибку для спика чисел, но сработает для списка строк и вернёт новый список строк, отсортированных по их длине!
reverse - Optional. A Boolean. False will sort ascending, True will sort descending. Default is False
"""

a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Sort numeric:
a = (1, 11, 2)
x = sorted(a)
print(x)  # [1, 2, 11]

# Sort descending:
a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)  # ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']


# Функция ord() позволяет определить код некоторого символа в таблице символов Unicode. Аргументом данной функции является одиночный символ.
# Если попытаться передать строку, содержащую более одного символа, получим ошибку времени выполнения: TypeError: ord() expected a character, but string of length 3 found
# Название функции ord происходит от английского слова order — порядок.
print("===ord()===")
num1 = ord("A")
num2 = ord("B")
num3 = ord("a")
print(num1, num2, num3)  # 65 66 97


# Функция chr() позволяет определить по коду символа сам символ. Аргументом данной функции является численный код.
# Название функции chr происходит от английского слова char — символ.
chr1 = chr(65)
chr2 = chr(66)
chr3 = chr(97)
print(chr1, chr2, chr3)  # A B a

# Функции ord() и chr() часто работают в паре.
# Вывод всех заглавных букв английского алфавита.
# Вызов функции ord('A') возвращает код символа «A», который равен 65. Далее на каждой итерации цикла, к данному коду прибавляется значение переменной i = 0, 1, 2, ..., 25, а затем полученный код преобразуется в символ с помощью вызова функции chr.
for i in range(26):
    print(chr(ord("A") + i), end="")  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Функции ord и chr являются взаимнообратными. Для них выполнены равенства:
# chr(ord('A')) = 'A', ord(chr(65)) = 65.


# enumerate() возвращает кортежи вида (индекс, элемент).
# x - это индекс (начинается с 0)
# y - это значение из range(2) (т.е. 0, 1)
for x, y in enumerate(range(2)):
    print(f"x - {x}; y - {y}")
    print(f"{chr(ord('A') + x)}")

# Что будет, если оставить только x, то x будет не индексом, а кортежем (индекс, значение).
for i in enumerate(range(2)):
    print(f"enumerate(): {i}")  # (0, 0) (1, 1)

# min() нахождения минимального значения в последовательности или среди аргументов.
# min(iterable, /, *, key=None)
# Принимает один итерируемый объект (например, список, строку, множество).
# Аргумент key позволяет указать функцию для вычисления значения сравнения.
numbers = [5, 2, 9, 1]
print(min(numbers))  # 1

# min(iterable, /, *, default, key=None)
# default используется, если итерируемый объект может оказаться пустым.
# В таком случае вместо ошибки возвращается значение default.
empty_list = []
print(min(empty_list, default="Нет данных"))  # Нет данных

# min(arg1, arg2, /, *args, key=None)
# - Принимает несколько аргументов и возвращает наименьший из них.
# - Можно передать key для сравнения по определённому критерию.
print(min(3, 7, -2, 5))  # -2
print(min("apple", "banana", key=len))  # apple
