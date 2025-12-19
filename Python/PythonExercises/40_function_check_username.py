username = input("Enter your username: ")


def check_username(any_username):
    if any_username.isalnum() and len(any_username) >= 8:
        print(f"Your username '{any_username}' is correct")
    else:
        print(
            "Your username must contain only letters and digits and must be longer than 7 characters."
        )


check_username(username)
