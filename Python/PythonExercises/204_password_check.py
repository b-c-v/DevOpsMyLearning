import re

user_password = input("Enter your password: ")


def check_password(password):
    if len(password) < 8 or len(password) > 20:
        print("The length of the password should be between 8-20 characters.")
    # anything that's not lowercase or digit is special char
    if not re.search(r"[^a-z0-9]", password):
        print("The password must contain at least one special character.")
    if re.search(r"[A-Z]", password):
        print("The password shouldn't contain uppercase letters.")
    if " " in password:
        print("The password shouldn't contain spaces.")


check_password(user_password)
