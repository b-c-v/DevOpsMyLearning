user_dict = {}

amount_values = int(input("How many values do you want to enter in this dictionary: "))

if amount_values > 0:
    for i in range(amount_values):
        key = int(input(f"Enter your {i+1} key: "))
        value = int(input(f"Enter your {i+1} value: "))
        user_dict[key] = value
    print(f"Your dictionary is: {user_dict}")
    max_key = max(user_dict.keys())
    max_value = max(user_dict.values())
    print(f"The maximum key is: {max_key}")
    print(f"The maximum value is: {max_value}")
else:
    print("The size of the dictionary should be greater than 0")
