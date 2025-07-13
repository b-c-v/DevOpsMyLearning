my_dict = {}


def add_user_info():
    my_dict["name"] = input("Enter your name: ")
    my_dict["address"] = input("Enter your email: ")
    my_dict["contact"] = input("Enter your phone: ")
    print("Your current data: ", my_dict)


add_user_info()
answer = input("Do you want to change your data Y/n? ")

while answer == "Y" or answer == "y":
    add_user_info()
    answer = input("Do you want to change your data Y/n? ")
else:
    print("Your data saved. Thank you!")
