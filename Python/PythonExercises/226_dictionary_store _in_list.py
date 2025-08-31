user_dict = {}

amount_values = int(
    input("How many key-value pairs do you want to enter in this dictionary: ")
)

for i in range(amount_values):
    key = input(f"Enter your {i+1} key: ")
    value = input(f"Enter your {i+1} value: ")
    user_dict[key] = value
print(f"Your dictionary is: {user_dict}")


def to_list_converter(values_list):
    tmp_list = []
    for i in values_list:
        tmp_list.append(i)
    return tmp_list


print(f"(My function) All keys as a list: {to_list_converter(user_dict.keys())}")
print(f"(My function) All values as a list: {to_list_converter(user_dict.values())}")
print(f"(Build-in function) All keys as a list: {list(user_dict.keys())}")
print(f"(Build-in function) All values as a list: {list(user_dict.values())}")


def to_tuple_converter(values_list):
    tmp_list = []
    for i in values_list:
        tmp_list.append(i)
    return tuple(tmp_list)


print(f"All keys as a tuple: {to_tuple_converter(user_dict.keys())}")
print(f"All values as a tuple: {to_tuple_converter(user_dict.values())}")
print(f"(Built-in function) All keys as a tuple: {tuple(user_dict.keys())}")
print(f"(Built-in function) All values as a tuple: {tuple(user_dict.values())}")
