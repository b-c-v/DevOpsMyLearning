my_dict = {}


def print_data():
    print(f"Name:\t\t{my_dict['name']}")
    print(f"Father Name:\t{my_dict['father_name']}")
    print(f"CNIC:\t\t{my_dict['cnic']}")
    print(f"Age:\t\t{my_dict['age']}")
    print(f"Contact:\t{my_dict['contact']}")


def add_user_info():
    my_dict["name"] = input("Enter your name: ")
    my_dict["father_name"] = input("Enter your father name: ")
    my_dict["cnic"] = input("Enter your CNIC: ")
    my_dict["age"] = input("Enter your age: ")
    my_dict["contact"] = input("Enter your contact: ")


def change_user_info():
    my_dict["cnic"] = input("Enter your CNIC: ")
    my_dict["age"] = input("Enter your age: ")
    my_dict["contact"] = input("Enter your contact: ")
    print("Your current data: ", my_dict)


add_user_info()
print_data()
answer = input("Do you want to change your data Y/n? ")

while answer == "Y" or answer == "y":
    change_user_info()
    print_data()
    answer = input("Do you want to change your data Y/n? ")
else:
    print("Your data saved. Thank you!")
