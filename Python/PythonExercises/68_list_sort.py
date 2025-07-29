number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

number_list.sort(reverse=True)
print("List in descending order", number_list)
