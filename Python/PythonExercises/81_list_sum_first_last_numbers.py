number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

print(
    f"The sum of the firs {number_list[0]} and the last {number_list[-1]} numbers in the list is: {number_list[0] + number_list[-1]}"
)
print(
    f"The sum of the second {number_list[1]} and the before last {number_list[-2]} numbers in the list is: {number_list[0] + number_list[-1]}"
)
