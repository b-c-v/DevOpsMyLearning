import numpy as np


def create_array(size):
    numbers = []
    for i in range(size):
        number = int(input(f"Enter your {i+1} number: "))
        numbers.append(number)
    # transform list to numpy array. This is faster that np.append(user_numpy_array, number)
    return np.array(numbers, dtype=int)


size_array = 12
user_numpy_array = create_array(size_array)

print(f"Your array contains: {user_numpy_array}")

replace_number = int(input("Which number would you like to replace: "))
replaced_number = int(input("What number would you like to replace it with: "))
user_numpy_array[user_numpy_array == replace_number] = replaced_number
print(f"Your array after replacement: {user_numpy_array}")

# reshape array
# Изменим форму массива на матрицу 3x4
reshaped_arr = user_numpy_array.reshape(
    3, 4
)  # reshape(3, 4) преобразует массив в таблицу 3 строки × 4 столбца

print("Reshaped array :\n", reshaped_arr)  # Выводим результат
