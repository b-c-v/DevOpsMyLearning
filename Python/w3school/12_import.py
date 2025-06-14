# Для того чтобы использовать возможности модулей в Python, необходимо их сначала подключить. Это делается с помощью команды import, которая позволяет импортировать весь модуль в программу:
import random
# Это позволяет использовать все функции и переменные, определённые в модуле, но с обязательным указанием имени модуля при каждом обращении. 
print(random.randint(1, 10))

# (не рекомендуется) Если требуется использовать функции модуля без указания имени модуля, можно импортировать отдельные элементы модуля с помощью конструкции from ... import. Это позволяет обращаться к функциям напрямую, не используя имя модуля.
from random import *
print(randint(1,10))

# Для упрощения обращения к модулям можно создавать псевдонимы (алиасы):
import random as rnd
print(rnd.randint(1, 10))

# Можно импортировать лишь необходимые части модуля, чтобы уменьшить объём используемой памяти и повысить читаемость кода.
from random import randint
# Теперь можно использовать только функцию randint из модуля random, без необходимости обращаться к полному имени модуля:
print(randint(1, 10))

# (не рекомендуется) Можно импортировать несколько модулей в одной строке, перечисляя их через запятую.
import subprocess, datetime, time
# Рекомендуется импортировать каждый модуль на отдельной строке для лучшей читаемости.
