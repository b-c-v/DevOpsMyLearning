# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# Модуль random предоставляет функции для генерации случайных чисел, букв и случайного выбора элементов последовательности (списка, строки и т.д.).
# Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:
import random

# Подключение модуля следующим образом позволяет в дальнейшем не писать название модуля и символ точки при вызове функций модуля.
from random import *

# Числа, генерируемые функциями модуля random, не являются подлинно случайными.
# Несмотря на то, что обычно их называют случайными числами, это псевдослучайные числа, вычисляемые на основе формулы.
# Формула, генерирующая случайные числа, должна быть инициализирована начальным значением.
# Оно используется в вычислении, возвращающем следующее случайное число в ряду.
# Когда модуль random импортируется, он получает системное время из внутреннего генератора тактовых импульсов компьютера и использует его как начальное значение.
# Системное время - целое число, представляющее текущую дату и время вплоть до одной сотой секунды. Если бы всегда использовалось одно и то же начальное значение,
# функции генерации случайных чисел всегда  возвращали бы один и тот же ряд псевдослучайных чисел.
# Поскольку системное время меняется каждую сотую долю секунды, можно без опасений утверждать, что всякий раз, когда импортируется модуль random, будет сгенерирована
# отличающаяся от предыдущих последовательность случайных чисел.

# Функции модуля random на самом деле являются методами одноименного класса random.
                      
"""
random.uniform(a, b)           Возвращает псевдослучайное число с плавающей   запятой в      диапазоне от a до b.               
random.randint(a, b)           Возвращает псевдослучайное целое число в диапазоне от a до b.
random.choice(a)               Возвращает псевдослучайный элемент из любой последовательности.
random.randrange(a, b, c)      Возвращает псевдослучайное число из диапазона от a до b с шагом c.
random.shuffle(a)              Перемешивает последовательность.
random.sample(population, k)   Возвращает список длиной k из уникальных элементов, выбранных из последовательности или множества.
"""

# ***функция random()***
#  возвращает случайное число с плавающей точкой (вещественное число).
# В функцию random() никаких аргументов не передается. Функция random() возвращает случайное число с плавающей точкой в диапазоне от 0.0 до 1.0 (исключая 1.0).
import random

num = random.random()


# Функции randint() и randrange() возвращают случайное целое число.

# ***randrange()***
# возвращает случайно выбранное число из последовательности чисел.
import random
# Аргумент 10 задает конечный предел последовательности значений. Функция возвратит случайно выбранное число из последовательности чисел от 00 до конечного предела, исключая сам предел.
num = random.randrange(10)

# задает начальное значение и конечный предел последовательности
# в переменной num будет храниться случайное число в диапазоне от 5 до 9
num = random.randrange(5, 10)

# задает начальное значение, конечный предел и величину шага:
# в переменной num будет храниться случайное число из последовательности чисел: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
num = random.randrange(0, 101, 10)


# ***randint()***
# принимает два обязательных аргумента a и b и возвращает случайное целое число из отрезка [a; b]
# левая и правая граница a и b включаются в диапазон генерируемых случайных чисел
import random

print(random.randint(0, 17))
print(random.randint(-5, 5))

# Функция randint() реализована на основе функции randrange() следующим образом:
# Return random integer in range [a, b], including both end points.
def randint(self, a, b):
    return self.randrange(a, b + 1)

# Функция uniform()
# возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон для отбора значений.
# выводит случайное число с плавающей точкой из диапазона [1.5; 17.3]:
import random
num = random.uniform(1.5, 17.3)
print(num)

# ***seed()***
# генерировать одну и ту же последовательность случайных чисел. При необходимости для этого можно вызвать функцию , задав начальное значение.
# генерирует 10 случайных чисел, и при этом содержит инструкцию, явно устанавливающую начальное значение для генератора случайных чисел:
import random
random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
for _ in range(10):
    print(random.randint(1, 100))
# Если выполнить такой код еще раз, то получим ту же самую последовательность псевдослучайных чисел.

# ***choice()***
# позволяет случайно выбрать элемент списка
from random import *
words_array = ['набор','совершенно','случайных','слов', 'или', 'значений']
print(choice(words_array))