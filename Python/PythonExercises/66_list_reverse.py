amount_numbers = int(input("How many numbers do you want to enter: "))
my_list = []


for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    my_list.append(number)


my_list.reverse()
print(f"List of the numbers in reverse mode: {my_list}")
