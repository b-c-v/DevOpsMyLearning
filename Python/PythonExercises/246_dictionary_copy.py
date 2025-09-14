user_dict = {}


def add_user_info():
    user_dict["name"] = input("Enter your name: ")
    user_dict["address"] = input("Enter your email: ")
    user_dict["contact"] = input("Enter your phone: ")
    user_dict["birth"] = input("Enter year of birth: ")
    print("Your current data: ", user_dict)
    return user_dict


add_user_info()

new_dict_key = {}
for k, v in user_dict.items():
    new_dict_key[k] = len(k)
print(f"Length of keys: {new_dict_key}")

new_dict_value = {k: len(v) for (k, v) in user_dict.items()}
print(f"Length of values: {new_dict_value}")
