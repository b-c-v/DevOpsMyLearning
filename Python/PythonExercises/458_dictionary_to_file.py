user_dict = {}


def add_user_info():
    user_dict["name"] = input("Enter your name: ")
    user_dict["address"] = input("Enter your email: ")
    user_dict["contact"] = input("Enter your phone: ")
    user_dict["birth"] = input("Enter year of birth: ")
    print("Your current data: ", user_dict)
    return user_dict


add_user_info()

with open("tmp.txt", "a") as file:
    for k, v in user_dict.items():
        file.write(str(k) + "\t" + str(v) + "\n")
