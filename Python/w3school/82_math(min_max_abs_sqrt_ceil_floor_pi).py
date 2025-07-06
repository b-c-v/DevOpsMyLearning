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
Округления
math.round(x)          Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа
math.round(x, n)       Округляет число x до n знаков после точки
math.floor(x)          Округляет число x вниз(«пол»)
math.ceil(x)           Округляет число x вверх(«потолок»)
math.abs(x)            Модуль числа x(абсолютная величина)
math.trunc(X)     усекает значение X до целого.


Список констант модуля math
math.pi           Число π = 3.141592653589793π = 3.141592653589793
math.e            Число e = 2.718281828459045e = 2.718281828459045


math.pow(X, Y)                          Возведение числа X в степень Y
math.sqrt(X)                            квадратный корень из X.
math.log(X, b)                          логарифм X по основанию b. Если base не указан, вычисляется натуральный логарифм.
math.log1p(X)                           натуральный логарифм(1 + X). При X → 0 точнее, чем math.log(1+X).
math.log10(X)                           логарифм X по основанию 10.
math.log2(X)                            логарифм X по основанию 2.
math.factorial(X)                       факториал числа X.
# sqrt(n) извлечения квадратного корня можно заменить кодом n ** 0.5, вместо .
# pow(x, n) можно заменить использованием оператора возведения в степень: x**n


math.copysign(X, Y)                     возвращает число, имеющее модуль такой же, как и у числа X, а знак как у числа Y.
math.fabs(X)                            модуль X.
math.fmod(X, Y)                         остаток от деления X на Y.
math.frexp(X)                           возвращает мантиссу и экспоненту числа.
math.ldexp(X, I)                        X * 2i. Функция, обратная функции math.frexp().
math.fsum(последовательность)           сумма всех членов последовательности. Эквивалент встроенной функции sum(), но math.fsum() более точна для чисел с плавающей точкой.
math.isfinite(X)                        является ли X числом.
math.isinf(X)                           является ли X бесконечностью.
math.isnan(X)                           является ли X NaN(Not a Number           не число).
math.modf(X)                            возвращает дробную и целую часть числа X. Оба числа имеют тот же знак, что и X.
math.exp(X)                             e в степени X
math.expm1(X)                           e в степени X-1. При X → 0 точнее, чем math.exp(X)-1.

math.acos(X)                            арккосинус X. В радианах.
math.asin(X)                            арксинус X. В радианах.
math.atan(X)                            арктангенс X. В радианах.
math.atan2(Y, X)                        арктангенс Y/X. В радианах. С учетом четверти, в которой находится точка(X, Y).
math.cos(X)                             косинус X(X указывается в радианах).
math.sin(X)                             синус X(X указывается в радианах).
math.tan(X)                             тангенс X(X указывается в радианах).
math.hypot(X, Y)                        вычисляет гипотенузу треугольника с катетами X и Y(math.sqrt(x * x + y * y)).
math.degrees(X)                         конвертирует радианы в градусы.
math.radians(X)                         конвертирует градусы в радианы.
math.cosh(X)                            вычисляет гиперболический косинус.
math.sinh(X)                            вычисляет гиперболический синус.
math.tanh(X)                            вычисляет гиперболический тангенс.
math.acosh(X)                           вычисляет обратный гиперболический косинус.
math.asinh(X)                           вычисляет обратный гиперболический синус.
math.atanh(X)                           вычисляет обратный гиперболический тангенс.
math.erf(X)                             функция ошибок.
math.erfc(X)                            дополнительная функция ошибок(1 - math.erf(X)).
math.gamma(X)                           гамма-функция X.
math.lgamma(X)                          натуральный логарифм гамма-функции X.
"""
