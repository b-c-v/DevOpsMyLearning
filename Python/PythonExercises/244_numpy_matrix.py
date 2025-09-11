import numpy as np


def create_array(size):
    # List comprehension
    numbers = [int(input(f"Enter your {i+1} number: ")) for i in range(size)]
    return np.diag(numbers)


size_array = int(
    input("How many numbers do you want to enter in the diagonal matrix: ")
)
user_numpy_array = create_array(size_array)
print(f"Your diagonal matrix:\n{user_numpy_array}")
