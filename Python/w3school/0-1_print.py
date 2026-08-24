# https://www.w3schools.com/python/default.asp
# Comments start with #
# Comments can be placed at the end of a line, and Python will ignore the rest of the line

"""
Python does not really have a syntax for multiline comments.
You can use a multiline string.
Add a multiline string (triple quotes) in your code, and place your comment inside it
"""

# То, что мы пишем в круглых скобках у команды print(), называется аргументами или параметрами команды.
# Команда print() позволяет указывать несколько аргументов, в таком случае их надо отделять запятыми.
print('Скоро я', 'буду программировать', 'на языке', 'Python!')


# если в тексте нужны одинарные кавычки, то для обрамления такого текста используем двойные кавычки;
print("В тексте есть 'одинарные' кавычки")
# если в тексте нужны двойные кавычки, то обрамляем его одинарными.
print('В тексте есть "двойные" кавычки')

# По умолчанию команда print() принимает несколько аргументов (параметров), выводит их через один пробел, после чего ставит перевод строки.
# Это поведение можно изменить, используя необязательные именованные параметры sep (separator, разделитель) и end (окончание).
print('sep', 'b', 'c', sep='*')  # sep*b*c
print('end', 'b', 'c', end='*')  # end b c*
print()

# У параметров sep и end следующие значения по умолчанию:
# sep=' '   # пробел
# end='\n'  # перевод строки

# In the print() function, you output multiple variables, separated by a comma:
x = 'apple'
y = 'banana'
z = 'cherry'
print(z, y, x)  # cherry banana apple


# You can also use the + operator to output multiple variables. For numbers, the + character works as a mathematical operator
print(x + y + z)  # applebananacherry


# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error: print(int1 + string1)
# To output multiple variables in the print() function is to separate them with commas, which even support different data types
int1 = 4
string1 = "What is your experience?"
print(string1, int1)

# * это оператор распаковки (unpacking operator) в Python. Он распаковывает элементы и передаёт их как отдельные аргументы в print()
print(*['a', 'b', 'c']) # a b c
print(['a', 'b', 'c'])  # ['a', 'b', 'c']

# F-String (f"...") — это форматированная строка позволяет встраивать переменные и выражения прямо в строку
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old")  # My name is Alice and I am 30 years old

# Параметр flush=True заставляет print() немедленно выводить содержимое буфера. Полезен для логирования в реальном времени или индикаторов прогресса
# По умолчанию flush=False, что означает, что вывод может быть буферизирован
print(f"Progress: {50}%", flush=True)
