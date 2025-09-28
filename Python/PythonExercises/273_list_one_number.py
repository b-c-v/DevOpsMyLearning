amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]
print(f"Your list is: {user_list}")

join_number = "".join(str(num) for num in user_list)
print(f"Joined number string: {join_number}")
