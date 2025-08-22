name_list = []


def hello_message():
    print("What do you want to do: ")
    print("1. Add user")
    print("2. View users")
    print("3. Remove user")
    print("4. Update username")
    selection = int(input("Please enter what do you want to do: "))
    return selection


def add_user():
    username = input("Please enter the name of the user to add: ")
    name_list.append(username)


def view_users(user_list):
    print("Users:")
    for i, username in enumerate(user_list):
        print(f"{i+1}\t{username}")


def delete_user():
    view_users(name_list)
    user = input("Please enter the name of the user that you want to delete: ")
    if user in name_list:
        name_list.pop(user)
    else:
        print("You select wrong name!")


def update_user():
    view_users(name_list)
    user = input("Please enter the name of the user to update: ")
    if user in name_list:
        index = name_list.index(user)
        name_list[index] = input("Enter the new name: ")
    else:
        print("You select wrong name!")


answer = "y"

while answer.lower() == "y":
    choice = hello_message()
    if choice == 1:
        add_user()
    elif choice == 2:
        view_users(name_list)
    elif choice == 3:
        delete_user()
    elif choice == 4:
        update_user()
    else:
        print("You made wrong choice!")
    answer = input("Do you want to change your data Y/n? ")
else:
    print("Your data saved. Thank you!")


print(name_list)
