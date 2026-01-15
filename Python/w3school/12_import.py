# Для того чтобы использовать возможности модулей в Python, необходимо их сначала подключить. Это делается с помощью команды import, которая позволяет импортировать весь модуль в программу:
import random
# - Python loads and executes random.py from the standard library
# - module object named random is created
# - all public objects (functions, classes, variables) defined in random module become accessible only through the module name
# Это позволяет использовать все функции и переменные, определённые в модуле, но с обязательным указанием имени модуля при каждом обращении.
print(random.randint(1, 10))

# Для упрощения обращения к модулям можно создавать псевдонимы (алиасы):
import random as rnd

print(rnd.randint(1, 10))

# (не рекомендуется) Импорт * (звёздочка) загружает ВСЕ публичные имена модуля в текущее пространство имён.
# Это может привести к:
# - конфликтам имён (перезаписи функций/переменных)
# - снижению читаемости кода (неясно, откуда взялась функция)
# - усложнению отладки
# Используется только в исключительных случаях (например, в интерактивной среде).
from random import *

print(randint(1, 10))  # вызов функции без указания имени модуля

# Если требуется использовать функции модуля без указания имени модуля, можно импортировать отдельные элементы модуля.
from random import randint
# - Python loads and execute random.py from the standard library
# - imports a single named object (randint) directly into the current namespace
# - the name randint can be used without the random. prefix
# - randint may be a variable, function, class, or any other object defined in the random module
# Теперь можно использовать только функцию randint из модуля random, без необходимости обращаться к полному имени модуля:
print(randint(1, 10))

# Можно импортировать сразу несколько функций из одного модуля.
from random import randint, randrange

print(f"Multiple functions from one module: {randrange(10)} {randint(1,10)}")

# (не рекомендуется) Можно импортировать несколько модулей в одной строке, перечисляя их через запятую.
import subprocess, datetime, time

# Рекомендуется импортировать каждый модуль на отдельной строке для лучшей читаемости.

# Из модуля os в текущее пространство имён импортируется объект path
from os import path  # Теперь name path напрямую доступно, без префикса os

path.exists("file.txt")  # имя os не создано, используется только path


# Импортируется подмодуль path через модуль os. Не имеет особого смысла потому что, это то же самое что import os
import os.path  # Загружается модуль os, а также его подмодуль path

# Проверяем существование файла через полное имя os.path
os.path.exists("file.txt")  # Здесь используется доступ через модуль os
# Сравниваем, являются ли os.path и path одним и тем же объектом
print(os.path is path)  # True - оба имени указывают на один и тот же модуль
# При таком подходе будут доступны все подмодули, хотя они явно не импортированы
print(os.name)  # доступно


# через import X.Y можно импортировать ТОЛЬКО модуль или подмодуль
# randint — это функция, а не модуль, поэтому такой импорт вызовет ошибку

# import random.randint

# Через точку нельзя импортировать функции, классы и переменные,
# если они не являются отдельными модулями
