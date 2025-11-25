import random
import string

while input("Do you want to generate a random string? (Y/n): ").strip().lower() in ("y", "yes"):
    string_length = int(input("How many characters should the random string have? "))
    result = "".join(random.choices(string.digits + string.ascii_uppercase, k=string_length))
    print(result)
else:
    print("Thank you!")