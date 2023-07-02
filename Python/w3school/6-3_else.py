# Python допускает необязательный блок else в конце циклов while и for.
# Это уникальная особенность Python, не встречающаяся в большинстве других языков программирования.
# Блок else в циклах часто применяется для обработки отсутствия элементов.
# Блок кода else в циклах встречается не так часто на практике.

"""
while условие:
    блок кода1
else:
    блок кода2
"""


"""
for i in range(10):
    блок кода1
else:
    блок кода2
"""

# Блок кода2, указанный в else, будет выполнен, когда штатным образом завершается цикл while или for.
# Под штатным завершением цикла подразумевается его завершение без использования оператора прерывания break.
# Оператор continue не влияет на выполнение блока else в циклах.


# Цикл завершается штатным образом и блок кода в инструкции else будет выполнен.
n = 5
while n > 0:
    n -= 1
    print(n, end='*')  # 4*3*2*1*0*Цикл завершен
else:
    print('Цикл завершен')

# Цикл преждевременно завершается с помощью оператора прерывания break, поэтому блок кода в инструкции else не будет выполнен.
n = 5
while n > 0:
    n -= 1
    print(n, end='*')  # 4*3*2*
    if n == 2:
        break
else:
    print('Цикл завершен.')