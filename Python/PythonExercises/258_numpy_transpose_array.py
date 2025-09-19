import numpy as np

rows = int(input("Please enter the number of rows in each layer: "))
columns = int(input("Please enter the number of columns in each row: "))

range_number = rows * columns

user_array = np.arange(range_number).reshape((rows, columns))
print(f"Your array is\n {user_array}")

# transposed array — это новый массив, который получается из исходного, если строки поменять местами со столбцами.
transpose_array = user_array.T
print(f"Transposed array is\n{transpose_array}")