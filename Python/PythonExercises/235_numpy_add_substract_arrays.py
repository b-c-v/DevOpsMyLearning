import numpy as np


def create_array(size, name_array):
    numbers = []
    for i in range(size):
        number = int(input(f"Enter your {i+1} number for {name_array}: "))
        numbers.append(number)
    # transform list to numpy array. This is faster that np.append(user_array, number)
    return np.array(numbers, dtype=int)


size_array = int(input("How many numbers do you want to enter in the arrays: "))
print("First array")
user_array_1 = create_array(size_array, "first array")


print("Second array")
user_array_2 = create_array(size_array, "second array")

print(f"Your first array is {user_array_1}")
print(f"Your second array is {user_array_2}")

add_array = user_array_1 + user_array_2
print(f"The sum of two arrays is: {add_array}")

subtract_array = user_array_1 - user_array_2
print(f"The subtraction of the second array from the first is: {subtract_array}")
