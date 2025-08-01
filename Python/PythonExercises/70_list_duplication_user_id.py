number_list = []

amount_numbers = int(input("How many numbers do you want to enter: "))

i = 0

while i < amount_numbers:
    number = int(input(f"Enter your {i+1} number: "))
    if number_list.count(number) > 0:
        print("You're trying to insert a duplicate value. Try again!")
    else:
        number_list.append(number)
        i += 1

print(number_list)
