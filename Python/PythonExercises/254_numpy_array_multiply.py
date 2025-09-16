import numpy as np


def create_array(size):
    numbers = []
    for i in range(size):
        number = int(input(f"Enter your {i+1} number: "))
        numbers.append(number)
    # transform list to numpy array. This is faster that np.append(user_numpy_array, number)
    return np.array(numbers, dtype=int)


size_array = int(
    input("How many numbers do you want to enter in the first and second array: ")
)
user_numpy_array_1 = create_array(size_array)
user_numpy_array_2 = create_array(size_array)

print(f"Your first array: {user_numpy_array_1}")
print(f"Your first array: {user_numpy_array_2}")


sum_array = np.add(user_numpy_array_1, user_numpy_array_2)
multiplication_array = np.multiply(user_numpy_array_1, user_numpy_array_2)
division_array = np.divide(user_numpy_array_1, user_numpy_array_2)
print(f"Addition: {sum_array}")
print(f"Multiplication: {multiplication_array}")
print(f"Division: {division_array}")
