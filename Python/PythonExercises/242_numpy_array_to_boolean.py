import numpy as np


def create_array(size):
    numbers = []
    i = 0
    while i < size:
        number = int(input(f"Enter your {i+1} number: "))
        if number in [0, 1]:
            numbers.append(number)
            i += 1
        else:
            print("You should enter only 0 or 1")
    # transform list to numpy array. This is faster that np.append(user_numpy_array, number)
    return np.array(numbers, dtype=int)


size_array = int(input("How many numbers do you want to enter in the array: "))
user_numpy_array = create_array(size_array)
print(f"Array contains: {user_numpy_array}")

print(
    f"After converting the array elements to boolean: {np.array(user_numpy_array, dtype=bool)}"
)
print(f"After converting the array elements to bytes: {user_numpy_array.tobytes()}")
