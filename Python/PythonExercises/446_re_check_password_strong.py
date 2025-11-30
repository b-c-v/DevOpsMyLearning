import re


def check_password_strength(password):
    if len(password) < 8:
        print("Password must be at least 8 characters long")

    if not re.search(r"[A-Z]", password):
        print("Password must contain at least one uppercase letter")

    if not re.search(r"[a-z]", password):
        print("Password must contain at least one lowercase letter")

    if not re.search(r"\d", password):
        print("Password must contain at least one digit")

    if not re.search(r"[!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~]", password):
        print(
            "Password must contain at least one special character (!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~)"
        )
        return

    print("Your password is strong.")


user_password = input("Enter a password: ")

check_password_strength(user_password)
