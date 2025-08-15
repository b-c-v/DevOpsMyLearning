my_dict = {}


def add_user_info():
    my_dict["name"] = input("Enter your name: ")
    my_dict["address"] = input("Enter your email: ")
    my_dict["contact"] = input("Enter your phone: ")
    my_dict["contact"] = input("Enter year of birth: ")
    print("Your current data: ", my_dict)


def change_key():
    old_key = input("Please enter the old key name: ")
    new_key = input("Please enter the new key name: ")
    if old_key in my_dict:
        my_dict[new_key] = my_dict.pop(old_key)
    else:
        print(f"Key '{old_key}' not found.")


add_user_info()

while input("Do you want to change your data Y/n? ").lower() == "y":
    change_key()
    print("Your current data: ", my_dict)
else:
    print("Your data saved. Thank you!")


# length of all keys and values
total_length = 0


def length_key_values(values_list):
    global total_length
    for i in values_list:
        total_length += len(i)
    return total_length


length_key_values(my_dict.keys())
length_key_values(my_dict.values())
print(f"The total length of all keys and values is: {total_length}")
