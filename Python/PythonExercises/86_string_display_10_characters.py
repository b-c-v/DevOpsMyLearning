user_string = input("Enter any sentence: ")


if len(user_string) <= 10:
    print("Sorry, this sentence can't be shortened!")
else:
    print(f"The first 10 characters  are: {user_string[0:10]}")
    print(f"The first characters except last 10 are: {user_string[:-10]}")
