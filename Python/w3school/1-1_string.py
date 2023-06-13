# В Python строки хранятся в виде последовательности юникод символов.
# UTF-8 — это кодировка, которая используются для перевода двоичных данных в числа.
# Unicode — это набор символов, который используется для преобразования чисел в символы.

# String variables can be declared either by using single or double quotes
x = "John"
# is the same as
x = 'John'
# You can assign a multiline string to a variable by using three quotes """   """ Or three single quotes ''' ...  ''':
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):
b = "Hello, World!"
print(b[1])      # e

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# первое число – это то место, где начинается срез (включительно), а второе – это место, где заканчивается срез (невключительно).
# Get the characters from position 2 to position 5 (not included):
print('===b[2:5]===')
print(b[2:5])    # llo

# Get the characters from the start to position 5 (not included):
print('===b[:5]===')
print(b[:5])     # Hello

# Get the characters from position 2, and all the way to the end:
print('===b[2:]===')
print(b[2:])     # llo, World!

#  Срез b[:] возвращает исходную строку.
print('===b[:]===')
print(b[:])      # Hello, World!

# Use negative indexes to start the slice from the end of the string
"""
Положительные индексы    0    1    2    3    4    5
Строка                   P    y    t    h    o    n
Отрицательные индексы   -6   -5   -4   -3   -2   -1
"""
# если длина строки s равна len(s), то при положительной нумерации слева направо, последний элемент имеет индекс равный len(s) - 1,
# при отрицательной индексации справа налево, первый элемент имеет индекс равный -len(s)
# Get the characters From: "o" in "World!" (position - 5) To, but not included: "d" in "World!" (position - 2):cl
print('===b[-5:-2]===')
print(b[-5:-2])  # orl

# Удалить из строки последний символ b[:-1]
print('===b[:-1]===')
print(b[:-1])    # Hello, World

# Можно передать в срез третий необязательный параметр, который отвечает за шаг среза.
# К примеру, срез s[1:7:2] создаст строку bdf состоящую из каждого второго символа (индексы 1, 3, 5, правая граница не включена в срез).
print('===n[1:7:2]===')
n = "01234567890"
print(n[1:7:2])  # 135

# Если в качестве шага среза указать отрицательное число, то символы будут идти в обратном порядке.
print('===n[::-1]===')
print(n[::-1])   # 09876543210

# Если первый параметр среза больше второго, то срез создает пустую строку.
# the first is greater than the second:
print('when the first is greater than the second:', n[7:2])

# Другое пояснение обратного индекса: сначала считываем строку в обратном порядке - gfedcba, индекс начинается с 0 и с шагом 3 выбираем буквки.
s = 'abcdefg'
print(s[::-3])  # gda

# we can loop through the characters in a string, with a for loop.
s = 'abcdef'
for i in range(len(s)):
    print(s[i])

# Если не нужен индекс самого символа, то можно использовать более короткий способ итерации:
for c in s:
    print(c)

# Метод — специализированная функция, тесно связанная с объектом. Как и функция, метод вызывается для выполнения отдельной задачи, но он вызывается для определенного объекта и "знает" о своем целевом объекте во время выполнения.
# Метод — функция, применяемая к объекту. Метод вызывается в виде имя_объекта.имя_метода(параметры).
# s.find('e') — это применение к строке s метода find с одним параметром 'e'
s.find('e')
"""
Методы строкового типа данных можно разделить на три группы:
- Конвертация регистра;
- Поиск и замена;
- Классификация символов.
"""


# To get the length of a string, use the len() function.
# При подсчете длины строки считаются все символы, включая пробелы.
print(len(b))  # 13


"""
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.
Method             Description
capitalize()       Converts the first character to upper case
casefold()         Converts string into lower case
center()           Returns a centered string
count()            Returns the number of times a specified value occurs in a string
encode()           Returns an encoded version of the string
endswith()         Returns true if the string ends with the specified value
expandtabs()       Sets the tab size of the string
find()             Searches the string for a specified value and returns the position of where it was found
format()           Formats specified values in a string
format_map()       Formats specified values in a string
index()            Searches the string for a specified value and returns the position of where it was found
isalnum()          Returns True if all characters in the string are alphanumeric
isalpha()          Returns True if all characters in the string are in the alphabet
isdecimal()        Returns True if all characters in the string are decimals
isdigit()          Returns True if all characters in the string are digits
isidentifier()     Returns True if the string is an identifier
islower()          Returns True if all characters in the string are lower case
isnumeric()        Returns True if all characters in the string are numeric
isprintable()      Returns True if all characters in the string are printable
isspace()          Returns True if all characters in the string are whitespaces
istitle()          Returns True if the string follows the rules of a title
isupper()          Returns True if all characters in the string are upper case
join()             Joins the elements of an iterable to the end of the string
ljust()            Returns a left justified version of the string
lower()            Converts a string into lower case
lstrip()           Returns a left trim version of the string
maketrans()        Returns a translation table to be used in translations
partition()        Returns a tuple where the string is parted into three parts
replace()          Returns a string where a specified value is replaced with a specified value
rfind()            Searches the string for a specified value and returns the last position of where it was found
rindex()           Searches the string for a specified value and returns the last position of where it was found
rjust()            Returns a right justified version of the string
rpartition()       Returns a tuple where the string is parted into three parts
rsplit()           Splits the string at the specified separator, and returns a list
rstrip()           Returns a right trim version of the string
split()            Splits the string at the specified separator, and returns a list
splitlines()       Splits the string at line breaks and returns a list
startswith()       Returns true if the string starts with the specified value
strip()            Returns a trimmed version of the string
swapcase()         Swaps cases, lower case becomes upper case and vice versa
title()            Converts the first character of each word to upper case
translate()        Returns a translated string
upper()            Converts a string into upper case
zfill()            Fills the string with a specified number of 0 values at the beginning
"""


# The upper() method returns the string in upper case:
print('===b.upper()===')
print(b.upper())  # HELLO, WORLD!


# The lower() method returns the string in lower case:
print('===lower()===')
print(b.lower())  # hello, world!


# The replace() method replaces a string with another string:
print('===replace()===')
print(b.replace("H", "J"))  # Jello, World!


# The split() method returns a list where the text between the specified separator becomes the list items.
print('===split()===')
print(b.split(","))  # ['Hello', ' World!']


# count(<sub>, <start>, <end>) считает количество непересекающихся вхождений подстроки <sub> в исходную строку s.
print('===count()===')
s = 'foo goo moo'
print(s.count('oo'))  # 3
# подсчет с 0 по 7 символ
print(s.count('oo', 0, 8))  # 2


# startswith(<suffix>, <start>, <end>) определяет начинается ли исходная строка s подстрокой <suffix>. Если исходная строка начинается с подстроки <suffix>,метод возвращает значение True, а если нет, то  False.
print('===startswith()===')
print(s.startswith('foo'))  # True
print(s.startswith('baz'))  # False


# ndswith(<suffix>, <start>, <end>) определяет оканчивается ли исходная строка s подстрокой <suffix>. Метод возвращает значение True если исходная строка оканчивается на подстроку <suffix> и False в противном случае.
print('===endswith()===')
print(s.endswith('bar'))  # False
print(s.endswith('moo'))  # True


# find(<sub>, <start>, <end>) находит индекс первого вхождения подстроки <sub> в исходной строке s. Если строка s не содержит подстроки <sub>, то метод возвращает значение -1.
# Можно использовать данный метод наравне с оператором in для проверки: содержит ли заданная строка некоторую подстроку или нет.
print('===find()===')
# s = 'foo bar foo baz foo qux'
print(s.find('moo'))      # 8
print(s.find('foo'))      # 0
print(s.find('python'))   # -1


# rfind(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки s.
print('===rfind()===')
print(s.rfind('moo'))      # 8
print(s.rfind('foo'))      # 0
print(s.rfind('python'))   # -1


# index(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он вызывает ошибку  ValueError: substring not found во время выполнения программы, если подстрока <sub> не найдена.
# rindex(<sub>, <start>, <end>) идентичен методу index(<sub>, <start>, <end>), за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки s.
# Методы find() и rfind() являются более безопасными чем index() и rindex(), так как не приводят к возникновению ошибки во время выполнения программы.


# strip() возвращает копию строки s у которой удалены все пробелы стоящие в начале и конце строки.
print('===strip()===')
l = '     foo bar foo baz foo qux      '
print(l.strip())
# lstrip() возвращает копию строки s у которой удалены все пробелы стоящие в начале строки.
print('===lstrip()===')
print(l.lstrip())

# Метод rstrip() возвращает копию строки s у которой удалены все пробелы стоящие в конце строки.
print('===rstrip()===')
print(l.rstrip())
# Методы strip(), lstrip(), rstrip() могут принимать на вход опциональный аргумент<chars>. Необязательный аргумент <chars> – это строка, которая определяет набор символов для удаления.


# Метод replace(<old>, <new>) возвращает копию s со всеми вхождениями подстроки <old>, замененными на <new>.
print('===replace()===')
print(l.replace('foo', 'grault'))     # grault bar grault baz grault qux
# Метод replace() может принимать опциональный третий аргумент <count>,  который определяет количество замен.
print(l.replace('foo', 'grault', 2))  # grault bar grault baz foo qux


# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Check if "free" is present in the following text
print('===in===')
txt = "The best things in life are free!"
print("free" in txt)  # True

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
# Check if "expensive" is NOT present in the following text:
print('===not in===')
txt = "The best things in life are free!"
print("expensive" not in txt)  # True

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
print('===concatenate===')
a = "Hello"
b = "World"
c = a + b
print(c)  # HelloWorld

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World

# Можно умножать строку на число. Такой оператор повторяет строку указанное количество раз.
print('===умножать строку на число===')
s = 'Hi' * 4
print(s)  # HiHiHiHi
# Строку можно умножать на число, но нельзя умножать на строку.
# s = 'Hi' * 'Hi' #TypeError: can't multiply sequence by non-int of type 'str'

# Тройные кавычки используются для многострочного (multiline) текста.
text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design 
philosophy emphasizes code readability with its notable use of significant whitespace.'''


# Можно использовать как одинарные, так и двойные кавычки:
s1 = 'В одиночных кавычках двойные кавычки "Двойные"'
s2 = "В двойных кавычках одиночные кавычки 'Одиночные'"
print(s1)  # В одиночных кавычках двойные кавычки "Двойные"
print(s2)  # В двойных кавычках одиночные кавычки 'Одиночные'

# To insert characters that are illegal in a string, use an escape character - is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)  # We are the so-called "Vikings" from the north.

#     Other escape characters used in Python:
#     \'      Single Quote
#     \\      Backslash
#     \n      New Line
#     \r      Carriage Return
#     \t      Tab
#     \b      Backspace
#     \f      Form Feed
#     \ooo    Octal value
#     \xhh    Hex value


# Функция ord() позволяет определить код некоторого символа в таблице символов Unicode. Аргументом данной функции является одиночный символ.
# Если попытаться передать строку, содержащую более одного символа, получим ошибку времени выполнения: TypeError: ord() expected a character, but string of length 3 found
# Название функции ord происходит от английского слова order — порядок.
print('===ord()===')
num1 = ord('A')
num2 = ord('B')
num3 = ord('a')
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
    print(chr(ord('A') + i), end='')  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Функции ord и chr являются взаимнообратными. Для них выполнены равенства:
# chr(ord('A')) = 'A', ord(chr(65)) = 65.
