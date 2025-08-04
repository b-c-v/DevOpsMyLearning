number_list = []

divisible_3 = []
divisible_5 = []

amount_numbers = int(input("How many numbers do you want to enter: "))

for i in range(amount_numbers):
    number = int(input(f"Enter your {i+1} number: "))
    number_list.append(number)

for i in number_list:
    if i % 3 == 0:
        divisible_3.append(i)
    if i % 5 == 0:
        divisible_5.append(i)

print(f"Numbers divisible by 3: {divisible_3}")
print(f"Numbers divisible by 5: {divisible_5}")
