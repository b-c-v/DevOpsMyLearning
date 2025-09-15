amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]
print(f"Your list is: {user_list}")

list_5_20 = [i for i in user_list if 20 > i > 5]
print(f"List with numbers from 5 to 20: {list_5_20}")

user_dict = {key + 1: value for key, value in enumerate(user_list)}
print(f"Dictionary from the list: {user_dict}")

list_from_dictionary_5_20 = [i for i in user_dict.values() if 20 > i > 5]
print(f"Values from the dictionary between 5 and 20: {list_from_dictionary_5_20}")
