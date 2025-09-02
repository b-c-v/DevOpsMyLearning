user_dict = {}

amount_values = int(input("How many values do you want to enter in this dictionary: "))

for i in range(amount_values):
    key = int(input(f"Enter your {i+1} key: "))
    value = int(input(f"Enter your {i+1} value: "))
    user_dict[key] = value

print(f"Your dictionary data: {user_dict}")
print(f"The sum of all keys is: {sum(user_dict.keys())}")


def multiply_elements(any_list):
    total_product = 1
    for i in any_list:
        total_product *= i
    return total_product


print(
    f"The product of all the values from a dictionary is: {multiply_elements(user_dict.values())}"
)
