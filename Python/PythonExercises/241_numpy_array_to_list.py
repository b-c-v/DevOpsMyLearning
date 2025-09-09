import numpy as np


def create_array(size):
    numbers = []
    for i in range(size):
        number = int(input(f"Enter your {i+1} number: "))
        numbers.append(number)
    # transform list to numpy array. This is faster that np.append(user_numpy_array, number)
    return np.array(numbers, dtype=int)


size_array = int(input("How many numbers do you want to enter in the array: "))
user_numpy_array = create_array(size_array)
print(f"Array of type{type(user_numpy_array)} contains: {user_numpy_array}")

user_list = user_numpy_array.tolist()
print(
    f"After converting the array to list, the type is {type(user_list)} and it contains: {user_list}"
)

user_numpy_array_converted = np.array(user_list)
print(
    f"After converting the list back to numpy array, the type is {type(user_numpy_array_converted)} and it contains: {user_numpy_array_converted}"
)
