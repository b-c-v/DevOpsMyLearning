amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]
print(f"Your list is: {user_list}")


positive_numbers = [x for x in user_list if x > 0]

if len(positive_numbers) > 0:
    print(f"Positive numbers from your list: {positive_numbers}")

negative_numbers = [x for x in user_list if x < 0]

if len(negative_numbers) > 0:
    print(f"Negative numbers from your list: {negative_numbers}")

if 0 in user_list:
    print("The list also contains 0.")
