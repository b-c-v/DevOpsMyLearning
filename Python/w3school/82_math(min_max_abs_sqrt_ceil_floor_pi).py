# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.
import math

# The min() and max() functions can be used to find the lowest or highest value in an iterable:
x = min(5, 10, 25)
y = max(5, 10, 25)

print('min() functions -', x)  # 5
print('max() functions -', y)  # 25

# The abs() function returns the absolute (positive) value of the specified number:
x = abs(-7.25)
print('abs() function -', x)  # 7.25

# The pow(x, y) function returns the value of x to the power of y (xy).
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
x = pow(4, 3)
print('pow(x, y) function -', x)  # 64

# The Math Module which extends the list of mathematical functions.
# To use it, you must import the math module: import math
# When you have imported the math module, you can start using methods and constants of the module.

# The math.sqrt() method for example, returns the square root of a number:
x = math.sqrt(64)
print('math.sqrt() method -', x)

# The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:
x = math.ceil(1.4)
y = math.floor(1.4)

print('math.ceil() method -', x)  # 2
print('math.ceil() method -', y)  # 1

# The math.pi constant, returns the value of PI (3.14...):
x = math.pi
print('math.pi constant -', x)  # 3.141592653589793


"""
math.acos(X)                            арккосинус X. В радианах
math.acosh(X)                           вычисляет обратный гиперболический косинус
math.asin(X)                            арксинус X. В радианах
math.asinh(X)                           вычисляет обратный гиперболический синус
math.atan(X)                            арктангенс X. В радианах
math.atan2(Y, X)                        арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка(X, Y)
math.atanh(X)                           вычисляет обратный гиперболический тангенс
math.ceil(x)                            округляет число x вверх («потолок»)
math.comb(n, k)                         сколькими способами можно выбрать k элементов из n, если порядок не важен и элементы не повторяются
math.copysign(X, Y)                     возвращает число, имеющее модуль такой же, как и у числа X, а знак как у числа Y
math.cos(X)                             косинус X(X указывается в радианах)
math.cosh(X)                            вычисляет гиперболический косинус
math.degrees(X)                         конвертирует радианы в градусы
math.dist()                             returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
math.erf(X)                             функция ошибок
math.erfc(X)                            дополнительная функция ошибок(1 - math.erf(X))
math.exp(X)                             e в степени X
math.expm1(X)                           e в степени X-1. При X → 0 точнее, чем math.exp(X)-1
math.fabs(X)                            модуль X
math.factorial(X)                       факториал числа X (факториал 4 = 4 * 3 * 2 * 1)
math.floor(x)                           округляет число x вниз («пол»)
math.fmod(X, Y)                         остаток от деления X на Y
math.frexp(X)                           возвращает мантиссу и экспоненту числа
math.fsum(последовательность)           сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой
math.gamma(X)                           гамма-функция X
math.gcd()                              returns the greatest common divisor of two integers
math.hypot(X, Y)                        вычисляет гипотенузу треугольника с катетами X и Y(math.sqrt(x * x + y * y))
math.isclose()                          checks whether two values are close to each other, or not
math.isfinite(X)                        является ли X числом
math.isinf(X)                           является ли X бесконечностью
math.isnan(X)                           является ли X NaN(Not a Number           не число)
math.isqrt()                            rounds a square root number downwards to the nearest integer
math.ldexp(X, I)                        X * 2i. Функция, обратная функции math.frexp()
math.lgamma(X)                          натуральный логарифм гамма-функции X
math.log(X, b)                          логарифм X по основанию b. Если base не указан, вычисляется натуральный логарифм
math.log10(X)                           логарифм X по основанию 10
math.log1p(X)                           натуральный логарифм(1 + X). При X → 0 точнее, чем math.log(1+X)
math.log2(X)                            логарифм X по основанию 2
math.perm()                             returns the number of ways to choose k items from n items with order and without repetition
math.pow(X, Y)                          возведение числа X в степень Y (можно заменить использованием оператора возведения в степень: x**n)
math.prod()                             returns the product of all the elements in an iterable
math.radians(X)                         конвертирует градусы в радианы
math.remainder()                        returns the closest value that can make numerator completely divisible by the denominator
math.sin(X)                             синус X(X указывается в радианах)
math.sinh(X)                            вычисляет гиперболический синус
math.sqrt(X)                            квадратный корень из X (извлечения квадратного корня можно заменить кодом: n**0.5)
math.tan(X)                             тангенс X(X указывается в радианах)
math.tanh(X)                            вычисляет гиперболический тангенс
math.trunc()                            returns the truncated integer parts of a number



Список констант модуля math
math.pi           Число π = 3.141592653589793π = 3.141592653589793
math.e            Число e = 2.718281828459045e = 2.718281828459045
math.inf          Returns a floating-point positive infinity
math.nan          Returns a floating-point NaN (Not a Number) value
math.tau          Returns tau (6.2831...)
"""

# Лотерея: сколько вариантов выбрать 5 чисел из 36?
print(math.comb(36, 5))  # 376992