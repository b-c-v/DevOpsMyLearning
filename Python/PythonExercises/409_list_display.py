string_count = int(input("How many values do you want to enter: "))

user_string = [input(f"Enter your {i+1} value: ") for i in range(string_count)]
print(f"Your list is: {user_string}")

for item in user_string[1:-1]:
    if len(item) != 5:
        print(item)


number_count = int(input("How many numbers do you want to enter: "))

user_numbers = [int(input(f"Enter your {i+1} number: ")) for i in range(number_count)]
print(f"Your list is: {user_numbers}")
for number in user_numbers[1:-1]:
    if number % 5 == 0 and number % 7 == 0:
        print(number)
