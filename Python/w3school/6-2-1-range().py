# The range() Function.
# To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)  # 0 1 2 3 4 5
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# Если переменная цикла не используется в теле цикла, то указывайте вместо нее символ нижнего подчеркивания _.
for _ in range(3):
    print('Hello')  # Hello Hello Hello
"""
Функция range() может принимать от одного до трех параметров: range(n), range(n, m), range(n, m, k)
- первый параметр – это старт последовательности (включительно);
- второй параметр – это стоп последовательности (не включительно);
- третий параметр – это величина шага.
"""

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6)
# Если первый параметр больше второго, то функция range() генерирует пустую последовательность. Например, range(10, 1) приводит к генерации пустой последовательности.
# Using the start parameter:
for x in range(2, 6):
    print('range start parameter', x)  # 2 3 4 5

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print('range increment the sequence -', x)  # 2 5 8 11 14 17 20 23 26 29

# Можно указать отрицательный шаг генерации (третий параметр), что приведет к генерированию убывающей последовательности.
# Старт последовательности (первый параметр) должен быть больше чем конец последовательности (второй параметр).
for i in range(5, 0, -1):
    print(i, end=' ')  # 5 4 3 2 1
# Если величина шага отрицательна и первый параметр меньше второго, то функция range() генерирует пустую последовательность.
# Например, вызов функции range(1, 10, -1) приводит к генерации пустой последовательности.

# Величина шага не может равняться нулю. Следующий код:
# range(1, 10, 0) приведет к ошибке ValueError: range() arg 3 must not be zero.

"""
Вызов функции       Последовательность чисел   
range(10)           0, 1, 2, 3, 4, 5, 6, 7, 8, 9
range(1, 10)        1, 2, 3, 4, 5, 6, 7, 8, 9
range(3, 7)         3, 4, 5, 6
range(7, 3)         пустая последовательность
range(2, 15, 3)     2, 5, 8, 11, 14
range(9, 2, -1)     9, 8, 7, 6, 5, 4, 3
range(3, 10, -2)    пустая последовательность
"""
