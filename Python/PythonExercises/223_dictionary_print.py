user_dict = {}

user_dict["name"] = input("Enter your name: ")
user_dict["email"] = input("Enter your email: ")
user_dict["contact"] = input("Enter your phone: ")
user_dict["birth"] = input("Enter year of birth: ")

print("Print items line by line with one tab distance between key and value")
for k, v in user_dict.items():
    print(f"{k}\t{v}")

print("Print items in uppercase")
for k, v in user_dict.items():
    print(f"{k.upper()}\t{v.upper()}")
