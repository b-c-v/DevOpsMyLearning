# print("Hello world")
# print('*', '**', '***', '****', '*****', '******', '*******', sep='\n')

# print('Mercury', 'Venus', sep='*', end='!')
# print('Mars', 'Jupiter', sep='**', end='?')

# sep = input()
# # var1 = input()
# # var2 = input()
# # var3 = input()
# print(input(), input(), input(), sep=sep)

# var1 = "hello"
# var2 = var1
# var1 = "world"
# print(var2)

# num = int(input())
# i = 1
# while i < 3:
# print(num+1)
# num = num+1
# if i == 3:
# break
# i += 1

# a, b = int(input()), int(input())
# print(3*(a+b)**3 + 275*b**2 - 127*a - 41)

# print(82 // 3 ** 2 % 7)
# print(3**2 % 7)

# вывод единиц, десятков, сотен в отдельные числа
"""
abcd = 1234
a = (abcd % 10000) // 1000
b = (abcd % 1000) // 100
c = (abcd % 100) // 10
d = abcd % 10
print(a, b, c, d, sep='\n')
"""

"""
a = 'Москва'
b = 'Санкт-Петербург'
c = 'Екатеринбург'
if len(a) < len(b):
    b, a = a, b
if len(b) < len(c):
    c, b = b, c
if len(a) < len(b):
    b, a = a, b
print(c, a, sep='\n')
"""

"""
s = 'abcabc'
if s in 'abc123abc':
    print('YES')
else:
    print('NO')

"""

# Число Фибоначчи
"""
n = int(input())
a, b = 1, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
"""

"""
i = input()
while (i != "КОНЕЦ") and (i != "конец"):
    print(i)
    i = input()
"""

"""
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')
"""

"""
n = 0
while n < 10:
    n += 2
    print(n)
else:
    print('Цикл завершен.')
"""

# печать треугольника из звездочек
"""
n = 7

for i in range(n):
    print('n // 2 + 1 =', n // 2 + 1)
    print('n // 2 - i =', n // 2 - i)

    cur_cnt = (n // 2 + 1) - abs(n // 2 - i)
    for j in range(cur_cnt):
        print("*", end="")
    print()
"""

# Гипотеза Эйлера о сумме степеней
"""
for a in range(1, 150):
    for b in range(a, 150):
        for c in range(b, 150):
            for d in range(c, 150):
                for e in range(d, 150):
                    if pow(a, 5) + pow(b,5) + pow(c, 5) + pow(d, 5) == pow(e,5):
                        print(a, b, c, d, e)
"""

# печать простых чисел в диапазоне от a до b
"""
a, b = int(input()), int(input())

for cur_num in range(a, b + 1):
    if cur_num == 1:
        continue

    for i in range(2, int(cur_num ** 0.5 + 1)):
        if cur_num % i == 0:
            break
    else:
        print(cur_num)
"""

"""
s = 'hello'
print(len(s))
for i in range(len(s) - 1, 0, -1):
    print(s[i])
"""
"""
# печать букв в диапазоне n 
n = int(input())

s = ""
for i in range(n):
    s += chr(ord("a") + i)
    
print(list(s))
"""
"""
# среднее арифметическое массива
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens)/len(evens)
print(sum(evens), len(evens), average)
"""

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]

# print(numbers1 * 2 + numbers2 * 9 + numbers3 )


# numbers = [1, 2, 3]
# sum = 0
# for n in numbers:
#     sum += pow(n,2)
# print(sum)


# numbers = [8, 9, 10, 11]
# numbers.insert(2, 17)
# y = [4, 5 ,6]
# numbers.extend(y)
# numbers.pop(0)
# numbers.extend(numbers)
# numbers.insert(3, 25)
# print(numbers)


"""
# объединить и отсортировать 2 списка
numbers1 = [1, 2, 3, 5, 6, 7, 8]
numbers2 = [5, 6, 13, 20]

def merge(list1, list2):
    tmp = (list1 + list2)
    tmp.sort() # если написать (list1 + list2).sort сортирует исходный список на месте, изменяет индексы списка и возвращает None
    return tmp
print(merge(numbers1, numbers2))

def merge_sorted(list1, list2):
    return sorted(list1 + list2) # sorted() возвращает новый отсортированный список, оставляя исходный список без изменений
print(merge_sorted(numbers1, numbers2))
"""
"""
# слияние двух отсортированных списков в один
def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2
    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1
    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]    
    return result
list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)
"""
"""
def draw_triangle():
    l = 1
    c = 7
    while l <= 15:
        print(' ' * c + '*' * l)
        l += 2
        c -= 1
draw_triangle()  # вызов функции
"""
"""
# объявление функции
def is_pangram(text):
    if len(set(text.replace(' ', '').lower())) == 26:
        return True
    else:
        return False

print(is_pangram('Jackdaws love my big sphinx of quartz'))

"""
"""
# первое простое число большее числа n
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# объявление функции
def get_next_prime(num):
    tmp = num + 1
    while not is_prime(tmp):
        tmp += 1
    return(tmp)


# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
"""
"""
# check is password good
# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    dig = False
    let = False
    blet = False
    for i in txt:
        if i.isupper():
             dig = True
        if i.islower():
             let = True
        if i.isdigit():
             blet = True
    if dig and let and blet:
        return True
    else:
        return False
# считываем данные
txt = 'aa13AN'
# вызываем функцию
print(is_password_good(txt))
"""

"""
# слова имеют одинаковую длину и отличаются ровно в 1 символе
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        counter = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                counter += 1
        return counter == 1
    return False

# вызываем функцию
print(is_one_away('water', 'wafer'))
"""
"""
# принимает в качестве аргумента радиус окружности и возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью
import math
def get_circle(radius):
    c = 2 * math.pi * radius
    s = math.pi * pow(radius, 2)
    return c, s

length, square = get_circle(1)
print(length, square)
"""
"""
import math
# объявление функции
def solve(a, b, c):
    D = math.pow(b, 2) - 4 * a * c
    print(D)
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        return min(x1, x2), max(x1, x2)
    elif D == 0:
        return -b / (2 * a), -b / (2 * a)
    else:
        return 'Нет корней'

x1, x2 = solve(1, 2, 1)
print(x1, x2)
"""

print(int('1000', 16))