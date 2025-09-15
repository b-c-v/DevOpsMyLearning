amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [input(f"Enter your word number {i+1}: ") for i in range(amount_numbers)]
print(f"Your list: {user_list}")

list_uppercase = [word.upper() for word in user_list]
print(f"List with uppercase words: {list_uppercase}")

list_lowercase = [word.lower() for word in user_list]
print(f"List with lowercase words: {list_lowercase}")