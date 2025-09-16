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

print(
    f"Your array type is {type(user_numpy_array)} and it contains: {user_numpy_array}"
)
repeat = int(input("How many times would you like to repeat the array: "))

repeat_numpy_array = np.tile(user_numpy_array, repeat)
print(repeat_numpy_array)

list_array = repeat_numpy_array.tolist()
print(
    f"After converting the array to list, the type is {type(list_array)} and it contains: {list_array}"
)

# If converted directly from a NumPy array to a tuple, it produces incorrect output (e.g., (np.int64(1), np.int64(2), ...)).
# To avoid this, first convert the array to a list and then to a tuple.
tuple_array = tuple(repeat_numpy_array.tolist())
print(
    f"After converting the array to tuple, the type is {type(tuple_array)} and it contains: {tuple_array}"
)
