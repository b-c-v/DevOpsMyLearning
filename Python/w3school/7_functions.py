# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


# In Python a function is defined using the def keyword:
"""
def имя_функции():
    блок кода
"""


def my_function():
    print("Hello from a function")


# Первая строка объявления функции называется заголовком функции.
# Со следующей строки идет блок кода – тело функции. Это набор инструкций, составляющих одно целое и выполняющихся каждый раз, когда вызывается функция.
# каждая строка в теле функции выделена отступом.

# При объявлении функции следует убедиться, что каждая строка тела функции начинается с одинакового количества пробелов, иначе произойдет ошибка: IndentationError: unexpected indent
"""
def print_greeting():
    рrint('Доброе утро!')

рrint('Сегодня мы будем изучать функции.')
    рrint('Это очень важная тема!')
"""


# Calling a Function. To call a function, use the function name followed by parenthesis:
def my_function():
    print("Hello from a function")


my_function()
# Объявление функции должно предшествовать ее вызову.

# правила именования функций:
# в имени функции используются только латинские буквы a-z, A-Z, цифры и символ нижнего подчеркивания (_);
# имя функции не может начинаться с цифры;
# имя функции по возможности должно отражать ее назначение;
# символы верхнего и нижнего регистра различаются.
# Для именования переменных и функций принято использовать стиль lower_case_with_underscores (слова из маленьких букв с подчеркиваниями).
# Поскольку функции выполняют действия, большинство программистов предпочитает в именах функций использовать глаголы.

# ***Arguments***
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# Arguments are often shortened to args in Python documentations.


# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
def draw_box(height, width):
    for i in range(height):
        print("*" * width)


# параметрами являются переменные height и width.
# В момент вызова функции draw_box(height, width) аргументами являются height и 9.
height = 1
draw_box(height, 9)  # *********


# Когда аргумент передается в функцию, параметрическая переменная функции будет ссылаться на значение этого аргумента.
# Однако любые изменения, которые вносятся в параметрическую переменную, не будут влиять на аргумент. (также см. 1_variables.py)
def draw_box(height, width):
    height = 1
    width = 5
    for i in range(height):
        print("!" * width)


n = 5
m = 7
draw_box(n, m)  # !!!!!
print(n, m)  # 5 7

# В теле функции вносятся изменения в значения параметрических переменных height и width, однако это никак не повлияло на значение переменных n и m из основной программы, которые передавались в качестве аргументов в функцию draw_box().


# ***Number of Arguments***
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# If you try to call the function with 1 or 3 arguments, you will get an error:
# This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
    print(fname + " " + lname)


# my_function("Emil") # TypeError: my_function() missing 1 required positional argument: 'lname'


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# Arbitrary Arguments are often shortened to *args in Python documentations.
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")  # The youngest child is Linus


# Keyword Arguments. You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
    print("key = value syntax - " + child3)


# key = value syntax - Linus
my_function(child1="Emil", child2="Tobias", child3="Linus")


# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
    print("His last name is " + kid["lname"])  # His last name is Refsnes


my_function(fname="Tobias", lname="Refsnes")


# Default Parameter Value.
# If we call the function without argument, it uses the default value:
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function()
my_function("Brazil")


# / ограничивает использование первых аргументов только позиционно (нельзя передать их как a=..., b=...)
# * означает, что следующие аргументы должны указываться только по имени (c - именованный аргумент, d - именованный аргумент со значением по умолчанию 'default value')
def myfunc(a, b, /, *, c, d="default value"):
    if d == "default value":
        return (a + b + c) / 2
    elif d == "sum":
        return a + b + c
    else:
        return "Invalid metric"


# d берёт значение по умолчанию 'default value'
print(myfunc(10, 20, c=30))  # 30
print(myfunc(10, 20, c=30, d="sum"))  # 60
print(myfunc(10, 20, c=30, d="any value"))  # Invalid metric
# print(myfunc(a=10, b=20, c=30)) # попытка передать a и b по имени вызовет ошибку
print(
    myfunc(10, 20, 30)
)  # вызовет ошибку, третий аргумент должен быть передан как именованный (c=30)


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)  # apple banana cherry


# ***Return Values***
# To let a function return a value, use the return statement
# Once return is executed, the function terminates immediately, and the returned value becomes the result of the function call
# A function can return any Python object (e.g., numbers, strings, lists, dictionaries).
def my_function(x):
    return 5 * x


print(f"return statement: {my_function(3)}")  # 15
print(f"return statement: {my_function(5)}")  # 25


# If a function does not explicitly use return, it returns None by default.
def my_function(x):
    x += 1
    print(x)


x = my_function(3)
print(x)  # None


# The returned value can be assigned to a variable for later use.
def multiply_by_five(number):
    return 5 * number


result = multiply_by_five(20)
print(f"return value assigned to a variable: {result}")  # 100


# В одной функции может быть сколько угодно инструкций return. Рассмотрим функцию convert_grade(), которая переводит стобалльную оценку в пятибалльную:
def convert_grade_many(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1


# Функцию convert_grade() можно переписать с помощью одной инструкции return:
def convert_grade_one(grade):
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70:
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1

    return result


print("many returns -", convert_grade_many(86))  # many returns - 4
print("one return -", convert_grade_one(11))  # one return - 1


# ***Return boolean***
# Python позволяет писать булевы функции, возвращающие либо истину (True), либо ложь (False). Булеву функцию можно применять для проверки условия, тогда значения True и False будут сигнализировать о его выполнении.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# ***Return few results
# функции не ограничены возвратом всего одного значения. После инструкции return можно определить много выражений, разделенных запятыми: return выражение 1, выражение 2, выражение 3 ...
def solve(a, b, c, d, e, f):
    x = (d * e - b * f) / (a * d - b * c)
    y = (a * f - c * e) / (a * d - b * c)
    return x, y


xsol, ysol = solve(2, 3, 4, 1, 2, 5)
print(
    "Решением системы являются числа", "x =", xsol, "y =", ysol
)  # Решением системы являются числа x = 1.3 y = -0.2


# ***The pass Statement***
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# Пока нет кода, но планируется,
def myfunction():
    pass


# ***Recursion***
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)  # Recursion Example Results 1 3 6 10 15 21
