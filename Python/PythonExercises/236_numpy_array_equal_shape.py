import numpy as np


def create_array(size):
    tmp = []
    expected_size = None
    for i in range(size):
        user_input = input(
            f"Enter your {i+1} nested list  (separate numbers by space): "
        )
        number = [int(x) for x in user_input.split()]
        tmp.append(number)
        if expected_size is None:
            expected_size = len(number)  # Для первого списка задаём эталонную длину
        elif (
            len(number) != expected_size
        ):  # Сравниваем длину текущего списка с эталонной
            print("All nested lists must be the same length")
            return None
    return np.array(tmp)


size_array = int(input("How many nested lists do you want to enter in the array: "))
user_array = create_array(size_array)
if user_array is not None:
    print(f"Your array:\n {user_array}")
    print(f"Equal-shaped array with zeros:\n {np.zeros_like(user_array)}")
