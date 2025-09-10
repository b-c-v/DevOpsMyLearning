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
print(f"Array contains: {user_numpy_array}")


with open("tmp.txt", "w+") as file:
    file.write(str(user_numpy_array))
    file.seek(0)
    print(f"Data saved in the file tmp.txt\n {file.read()}")
