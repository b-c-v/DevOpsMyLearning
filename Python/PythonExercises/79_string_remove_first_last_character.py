user_string = input("Enter any sentence: ")

print(f"The first character is: {user_string[0]}")
print(f"The last character is: {user_string[-1]}")

if len(user_string) <= 2:
    print("Sorry, this sentence can't be shortened!")
else:
    print(f"The string with the first and last characters removed: {user_string[1:-1]}")
