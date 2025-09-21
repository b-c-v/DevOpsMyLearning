import numpy as np

def create_array(size):
    numbers = []
    for i in range(size):
        number = float(input(f"Enter your {i+1} number: "))
        numbers.append(number)
    # transform list to numpy array. This is faster that np.append(user_array, number)
    return np.array(numbers, dtype=float)


size_array = int(input("How many numbers do you want to enter in the array: "))
user_float_array = create_array(size_array)

print(f"Your array with floating-point numbers: {user_float_array}")

user_int_array = np.array(user_float_array, dtype=int)
print(f"Your array after converting to integers: {user_int_array}")



