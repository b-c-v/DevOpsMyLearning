user_dict = {}

amount_values = int(input("How many values do you want to enter in this dictionary: "))

for i in range(amount_values):
    key = input(f"Enter your {i+1} key: ")
    value = input(f"Enter your {i+1} value: ")
    user_dict[key] = value

print(f"Your dictionary data: {user_dict}")

vowels = ["a", "e", "i", "o", "u"]

for value in user_dict.values():
    for vowel in vowels:
        if type(value) == str and vowel in value.lower():
            print(f"Word '{value}' has vowel character")
            break
