import numpy as np
import pandas as pd


def create_array(size):
    numbers = []
    for i in range(size):
        number = int(input(f"Enter your {i+1} number: "))
        numbers.append(number)
    # transform list to numpy array. This is faster that np.append(user_numpy_array, number)
    return np.array(numbers, dtype=int)


size_array = int(input("How many numbers do you want to enter in the array: "))
user_numpy_array = create_array(size_array)
print(f"Array of type {type(user_numpy_array)} contains: {user_numpy_array}")

user_panda_series = pd.Series(user_numpy_array)
print(f"Panda series of type {type(user_panda_series)} contains:\n{user_panda_series}")

back_to_np = user_panda_series.to_numpy()
print(f"Array of type {type(back_to_np)} contains: {back_to_np}")
