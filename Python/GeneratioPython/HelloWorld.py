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


numbers = [1, 2, 3]
sum = 0
for n in numbers:
    sum += pow(n,2)
print(sum)