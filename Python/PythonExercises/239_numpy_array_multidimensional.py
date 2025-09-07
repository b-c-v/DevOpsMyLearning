import numpy as np


def create_array(size):
    tmp = []
    expected_size = None
    for i in range(size):
        user_input = input(
            f"Enter your {i+1} nested list  (separate numbers by space): "
        )
        number = [int(x) for x in user_input.split()]
        tmp.append(number)
        if expected_size is None:
            expected_size = len(number)  # Для первого списка задаём эталонную длину
        elif (
            len(number) != expected_size
        ):  # Сравниваем длину текущего списка с эталонной
            print("All nested lists must be the same length")
            return None
    return np.array(tmp)


size_array = int(input("How many nested lists do you want to enter in the array: "))
user_array = create_array(size_array)
if user_array is not None:
    print(f"Your array:\n {user_array}")
    multiply_number = int(input("Please enter any multiplier for the array: "))
    multiply_array = user_array * multiply_number
    print(f"Array after multiplication:\n{multiply_array}")

# display only even numbers
even_array = []
for i in multiply_array:
    for j in i:
        if j % 2 == 0:
            even_array.append(int(j))
print(f"Even numbers from array after multiplication: {np.array(even_array)}")

# Use list comprehension
comprehension_even_array = [int(j) for i in multiply_array for j in i if j % 2 == 0]
"""
comprehension_even_array = [
    int(j)                    # Что добавляем
    for i in multiply_array   # Внешний цикл
    for j in i                # Внутренний цикл
    if j % 2 == 0             # Условие фильтрации
]
"""
print(f"Comprehension: {comprehension_even_array}")
