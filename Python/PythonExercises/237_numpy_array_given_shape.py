import numpy as np

width = int(input("Enter the width of the array (columns): "))
height = int(input("Enter the height of the array (rows): "))
print("Array filled with zeroes")
user_array_0 = np.zeros((height, width))
print(user_array_0)

print("Array filled with ones")
user_array_1 = np.ones((height, width))
print(user_array_1)
