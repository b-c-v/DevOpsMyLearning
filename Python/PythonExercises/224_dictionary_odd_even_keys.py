user_dict = {}

amount_values = int(input("How many values do you want to enter in this dictionary: "))

for i in range(amount_values):
    user_dict[i] = input(f"Enter your {i+1} value: ")

print(f"Your dictionary is: {user_dict}")

for k, v in user_dict.items():
    if k % 2 == 0:
        print(f"Values for even-numbered keys: {v}")


for k, v in user_dict.items():
    if k % 2 != 0:
        print(f"Value for odd-numbered keys: {v}")