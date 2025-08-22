number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

max_number = number_list[0]
min_number = number_list[0]

for i in number_list:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i

print(f"The biggest number is {max_number}")
print(f"The smallest number is {min_number}")

# using min() max() methods
print(f"Using method: The biggest number is {max(number_list)}")
print(f"Using method: The smallest number is {min(number_list)}")
