user_string = input("Enter any phrase: ")

lower_count = 0
upper_count = 0
digit_count = 0

for char in user_string:
    if char.isdigit():
        digit_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isupper():
        upper_count += 1

if digit_count > 0:
    print(f"In your phrase, there are {digit_count} digits")

if lower_count > 0:
    print(f"In your phrase, there are {lower_count} lowercase letters")

if upper_count > 0:
    print(f"In your phrase, there are {upper_count} uppercase letters")
