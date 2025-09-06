import numpy as np

size_array = int(input("Enter the size of the array: "))
numbers = np.zeros(size_array)
print(numbers)

for i in range(size_array):
    number = int(input(f"Enter your {i+1} number: "))
    numbers[i] = number
print(f"(for) Your array: {numbers}")

counter = 0
while counter < size_array:
    number = int(input(f"Enter your {counter+1} number: "))
    numbers[counter] = number
    counter += 1
print(f"(while) your array {numbers}")
