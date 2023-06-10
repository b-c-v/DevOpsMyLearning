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
Список функций модуля math

Функция       Описание
      Округления
int()         Округляет число в сторону нуля
round(x)      Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа
round(x, n)   Округляет число x до n знаков после точки
floor(x)      Округляет число x вниз («пол»)
ceil(x)       Округляет число x вверх («потолок»)
abs(x)        Модуль числа x (абсолютная величина)
      Корни, логарифмы, степени и факториал
sqrt(x)       Квадратный корень числа x
pow(x, n)     Возведение числа x в степень n
log(x)        Натуральный логарифм числа x. Основание натурального логарифма равно числу e
log10(x)      Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
log(x, b)     Логарифм числа x по основанию b
factorial(n)  Факториал натурального числа n
      Тригонометрия
degrees(x)    Преобразует угол x, заданный в радианах, в градусы
radians(x)    Преобразует угол x, заданный в градусах, в радианы
cos(x)        Косинус угла x, задаваемого в радианах
sin(x)        Синус угла x, задаваемого в радианах
tan(x)        Тангенс угла x, задаваемого в радианах
acos(x)       Возвращает угол в радианах от 00 до ππ, cos которого равен x
asin(x)       Возвращает угол в радианах от −π2−2π​ до π22π​, sin которого равен x
atan(x)       Возвращает угол в радианах от −π2−2π​ до π22π​, tan которого равен x
atan2(y, x)   Полярный угол (в радианах) точки с координатами (x, y)
"""
# sqrt(n) извлечения квадратного корня можно заменить кодом n ** 0.5, вместо .
# pow(x, n) можно заменить использованием оператора возведения в степень: x**n
"""
Список констант модуля math

Константа    Описание
pi           Число π = 3.141592653589793π = 3.141592653589793
e            Число e = 2.718281828459045e = 2.718281828459045
"""
