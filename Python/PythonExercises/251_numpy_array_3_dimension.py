import numpy as np

layers = int(input("Please enter the number of layers in the array: "))
rows = int(input("Please enter the number of rows in each layer: "))
columns = int(input("Please enter the number of columns in each row: "))

range_number = layers * rows * columns

user_array = np.arange(range_number).reshape((layers, rows, columns))
print(f"Your array is\n {user_array}")
