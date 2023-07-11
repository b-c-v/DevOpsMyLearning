# https://www.w3schools.com/python/default.asp
# Comments start with #
# Comments can be placed at the end of a line, and Python will ignore the rest of the line

"""
Python does not really have a syntax for multiline comments.
You can use a multiline string.
Add a multiline string (triple quotes) in your code, and place your comment inside it
"""

# Python uses indentation to indicate a block of code. Python will give you an error if you skip the indentation
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5 > 2:
    print("Five is greater than two!")

# Python has no command for declaring a variable.
# Variable names are case-sensitive.
# A variable is created the moment you first assign a value to it.
y = "Hello, World!"
X = "Case-sensitive variable"
x = 5  # x will not overwrite X
print(x)
print(y)
print(X)

"""
    Rules for Python variables:
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords: and, as, assert, def, del, False etc.
"""
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# There are several techniques you can use to make them more readable:
# Camel Case - Each word, except the first, starts with a capital letter:
myVariableName = "John"
# Pascal Case - Each word starts with a capital letter:
MyVariableName = "John"
# Snake Case - Each word is separated by an underscore character:
my_variable_name = "John"

# Можно за одну инструкцию присваивания изменять значение сразу нескольких переменных:
name, surname = 'Vasya', 'Pythonist'
print('Сразу несколько переменных - Имя:', name, 'Фамилия:', surname)


# Поменять значения переменных x и y местами.
x, y = y, x
# Поменять значения переменных x и y местами используя временную переменную temp:
temp = x
x = y
y = temp


"""
    Python has the following data types built-in by default, in these categories:
    Text Type:         str
    Numeric Types:     int, float, complex
    Sequence Types:    list, tuple, range
    Mapping Type:      dict
    Set Types:         set, frozenset
    Boolean Type:      bool
    Binary Types:      bytes, bytearray, memoryview
    None Type:         NoneType
"""
# You can convert from one type to another with the int(), float(), and complex() methods
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# convert from int to float:
a = float(x)        # 1.0
# convert from float to int:
b = int(y)          # 2
# convert from int to complex:
c = complex(x)      # (1+0j)

# Float can also be scientific numbers with an "e" to indicate the power of 10
x = 35e3
y = 12E4
z = -87.7e100

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = "Hello World"                                # x is of type str
x = 20                                           # x is of type int
x = 20.5                                         # x is of type float
x = 1j                                           # x is of type complex
x = ["apple", "banana", "cherry"]                # x is of type list
x = ("apple", "banana", "cherry")                # x is of type tuple
x = range(6)                                     # x is of type range
x = {"name": "John", "age": 36}                  # x is of type dict
x = {"apple", "banana", "cherry"}                # x is of type set
x = frozenset({"apple", "banana", "cherry"})     # x is of type frozenset
x = True                                         # x is of type bool
x = b"Hello"                                     # x is of type bytes
x = bytearray(5)                                 # x is of type bytearray
x = memoryview(bytes(5))                         # x is of type memoryview
x = None                                         # x is of type NoneType


# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")                           # x is of type str
# x is of type int Для удобного чтения чисел можно использовать символ подчеркивания x = 25_000_000
x = int(20)
x = float(20.5)                                  # x is of type float
x = complex(1j)                                  # x is of type complex
x = list(("apple", "banana", "cherry"))          # x is of type list
x = tuple(("apple", "banana", "cherry"))         # x is of type tuple
x = range(6)                                     # x is of type range
x = dict(name="John", age=36)                    # x is of type dict
x = set(("apple", "banana", "cherry"))           # x is of type set
x = frozenset(("apple", "banana", "cherry"))     # x is of type frozenset
x = bool(5)                                      # x is of type boola
x = bytes(5)                                     # x is of type bytes
x = bytearray(5)                                 # x is of type bytearray
x = memoryview(bytes(5))                         # x is of type memoryview


# Casting If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3


# Get the Type. You can get the data type of a variable with the type() function.
print(type(x))
print(type(y))


# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)  # apple
print(y)  # banana
print(z)  # cherry


# ***Global and local variables***
# Global Variables - variables that are created outside of a function. Global variables can be used by everyone, both inside of functions and outside.
# The global variable with the same name will remain as it was, global and with the original value.

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function.
# Память для локальных переменных выделяется на время исполнения данной функции в специальной области, называемой стеком.
# При завершении работы функции память освобождается, внутренние результаты работы функции не сохраняются от одного обращения к другому.
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()  # Python is fantastic
print("Python is " + x)  # Python is awesome

# Разные функции могут иметь локальные переменные с одинаковыми именами, потому что они не видят локальных переменных друг друга.


def print_texas():
    birds = 5000
    print('В Техасе обитает', birds, 'птиц.')

# Функция print_california() обращается к локальной переменной birds функции print_texas().
# Вызов функции print_california(), приводит к ошибке: NameError: name 'birds' is not defined


def print_california():
    print('В Калифорнии обитает', birds, 'птиц.')
# print_california()

# К локальной переменной не может обращаться программный код, который появляется внутри функции до того, как переменная была создана.
# если в функции print_texas() поменять местами строки кода, то при вызове получим ошибку: UnboundLocalError: cannot access local variable 'birds' where it is not associated with a value


def print_texas():
    print('В Техасе обитает', birds, 'птиц.')
    birds = 5000
# print_texas()


# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
"""
следует ограничить использование глобальных переменных либо не использовать их вообще:
- Глобальные переменные затрудняют отладку программы. Значение глобальной переменной может быть изменено любой инструкцией в программном файле. Если обнаружится,
что в глобальной переменной хранится неверное значение, то придется отыскать все инструкции, которые к ней обращаются, чтобы определить,
откуда поступает плохое значение.
- Функции, использующие глобальные переменные, обычно зависят от этих переменных. Если возникнет необходимость применить такую функцию в другой программе,
скорее всего придется эту функцию перепроектировать, чтобы она не опиралась на глобальную переменную.
- Глобальные переменные затрудняют понимание программы. Глобальная переменная может быть модифицирована любой инструкцией в программе. При необходимости
разобраться в какой-то части программы, использующей глобальную переменную, придется узнать обо всех других частях программы, обращающихся к этой глобальной переменной.
"""
# ***global***
# Глобальная константа – глобальное имя, ссылающееся на неизменное значение.
# Поскольку значение глобальной константы не может быть изменено во время исполнения программы, можно не беспокоиться о потенциальных опасностях, обычно связанных с использованием глобальных переменных.
# global используется для создания глобальной переменной и изменения ее в локальной области видимости.


def myfunc():
    global x
    x = "fantastic"


myfunc()  # Python is fantastic
print("Python is " + x)  # Python is fantastic

# Когда мы создаем переменную внутри функции, она по умолчанию является локальной.
# Когда мы определяем переменную вне функции, она по умолчанию является глобальной. В этом случае не нужно использовать ключевое слово global.
# Ключевое слово global нужно для получения доступа к глобальной переменной и изменения ее внутри функции, то есть внутри локальной области видимости.
# Использовать ключевое слово global вне функции бессмысленно.



