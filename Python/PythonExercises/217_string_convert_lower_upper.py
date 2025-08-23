user_string = input("Enter any word: ")

if any(s.islower() for s in user_string) and any(s.isupper() for s in user_string):
    print(user_string.swapcase())
else:
    print("Your word doesn't have both uppercase and lowercase letters.")
