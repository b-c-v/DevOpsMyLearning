number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)


numbers_sum = sum(number_list)
numbers_average = numbers_sum / amount_numbers

print("Summary of your numbers is: ", numbers_sum)
print("Average of your numbers is: ", numbers_average)
