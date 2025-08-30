amount_numbers = int(input("How many numbers do you want to enter: "))

user_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]
print(f"Your list is: {user_list}")

power_3 = [x**3 for x in user_list]
print(f"Power of 3 of all numbers in the list: {power_3}")

total = sum([num for num in user_list])
print(f"Sum of all numbers in the list is: {total}")
