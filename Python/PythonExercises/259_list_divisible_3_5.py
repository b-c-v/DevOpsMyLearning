amount_numbers = int(input("How many numbers do you want to enter: "))

number_list = [int(input(f"Enter your {i+1} number: ")) for i in range(amount_numbers)]

divisible_3_5 = [i for i in number_list if i % 3 == 0 or i % 5 == 0]

print(f"Numbers divisible by 3 or 5 from your list: {divisible_3_5}")
