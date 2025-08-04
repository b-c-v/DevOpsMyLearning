number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

my_tuple = tuple(number_list)

first_number = my_tuple[0]
last_number = my_tuple[-1]
if my_tuple[0] == my_tuple[-1]:
    print(
        f"The first {first_number} and the last {last_number} numbers of the tuple are the same"
    )
else:
    print(
        f"The first {first_number} and the last {last_number} numbers of the tuple are NOT the same"
    )
