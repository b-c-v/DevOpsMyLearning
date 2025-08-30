user_dict = {}
counter = int(input("How many users do you want to add: "))


def add_user_info():
    name = input("Enter your name: ").lower()
    """
    user_dict[input("Enter your name: ")] = { 
    Will not work because Python first evaluates the right side of the assignment.
    It processes all the input() calls inside the dictionary: email, phone, birth.
    Then it asks for the name to use as the key
    """
    user_dict[name] = {
        "email": input("Enter your email: "),
        "contact": input("Enter your phone: "),
        "birth": input("Enter year of birth: "),
    }
    print("Your current data: ", user_dict)


for i in range(counter):
    add_user_info()

select_user = input("Enter the name of the user to show his data: ").lower()
if select_user in user_dict:
    print(f"The user data is: {user_dict[select_user]}")
else:
    print(f"The user {select_user} doesn't exist in the dictionary")
