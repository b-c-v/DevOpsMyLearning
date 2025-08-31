user_dict = {}

amount_values = int(
    input("How many key-value pairs do you want to enter in this dictionary: ")
)

for i in range(amount_values):
    key = input(f"Enter your {i+1} key: ")
    value = input(f"Enter your {i+1} value: ")
    user_dict[key] = value
print(f"Your dictionary is: {user_dict}")


# length of all keys and values
def total_length_of_strings(values_list):
    total_length = 0
    for i in values_list:
        total_length += len(i)
    return total_length


print(f"Total length of all keys is: {total_length_of_strings(user_dict.keys())}")
print(f"Total length of all values is: {total_length_of_strings(user_dict.values())}")
