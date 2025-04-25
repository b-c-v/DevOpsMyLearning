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
