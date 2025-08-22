import random

number_list = []

amount_numbers = int(input("How many color codes do you want to enter: "))

for i in range(amount_numbers):
    color = input(f"Enter any color code: ")
    number_list.append(color)


number_list.sort(reverse=True)
print("List of colors in descending order", number_list)

number_list.sort(reverse=False)
print("List of colors in ascending order", number_list)

random.shuffle(number_list)
print("List of colors in shuffle order", number_list)

