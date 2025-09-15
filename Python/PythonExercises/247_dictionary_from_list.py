amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]
print(f"Your list is: {user_list}")


user_dict_value = {i: i**2 for i in user_list}
print(f"Dictionary where the value is the square of the key: {user_dict_value}")

user_dict_key = {i**2: i for i in user_list}
print(f"Dictionary where the key is the square of the value: {user_dict_key}")
