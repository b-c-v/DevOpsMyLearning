import random
import string

while input("Do you want to generate a password? (Y/n): ").strip().lower() in ("y", "yes"):
    password_length = int(input("How many characters should the password have? "))
    allowed_characters = (
        string.digits +
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.punctuation
    )
    result = "".join(random.choices(allowed_characters, k=password_length))
    print(result)
else:
    print("Thank you!")