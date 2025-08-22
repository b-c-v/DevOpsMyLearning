password = input("Enter your password: ")
if password.isalnum() and len(password) >= 8:
    print("Your password is correct")
else:
    print(
        "Your password must contain only letters and digits and be longer than 7 characters."
    )
