user_dict = {}


def hello_message():
    print("What do you want to do: ")
    print("1. Add user info")
    print("2. View user info")
    print("3. Update key")
    print("4. Update value")
    selection = int(input("Please enter what do you want to do: "))
    return selection


def add_user_info():
    # global user_dict # если необходимо перезаписать весь словарь заново (стереть старые данные и заменить на новые)
    # update() если необходимо только дополнить или изменить данные.
    # Без update() или global внутри функции создаётся заново словарь user_dict, не затрагивая глобальную переменную.
    user_dict.update(
        {  
            "name": input("Enter your name: "),
            "email": input("Enter your email: "),
            "phone": input("Enter your phone: "),
            "birth": input("Enter year of birth: "),
        }
    )
    print("Your current data: ", user_dict)


def view_users():
    print("Users:")
    for i, key in enumerate(user_dict):
        print(f"{i+1}\t{key}\t{user_dict[key]}")


def update_key():
    view_users()
    key_name = input("Please enter the name of the key to update: ")
    if key_name in user_dict.keys():
        tmp_value = user_dict[key_name]
        del user_dict[key_name]
        new_key = input("Please enter the name of new key: ")
        user_dict[new_key] = tmp_value
        view_users()
    else:
        print("You selected a wrong key name!")


def update_value():
    view_users()
    value_name = input("Please enter the name of the value to update: ")
    for key, value in user_dict.items():
        if value == value_name:
            new_value = input("Please enter the name of new value: ")
            user_dict[key] = new_value
            view_users()
    else:
        print("You selected a wrong value!")


answer = "y"

while answer.lower() == "y":
    choice = hello_message()
    if choice == 1:
        add_user_info()
    elif choice == 2:
        view_users()
    elif choice == 3:
        update_key()
    elif choice == 4:
        update_value()
    else:
        print("You made a invalid choice!")
    answer = input("Do you want to change your data Y/n? ")
else:
    print("Your data has saved. Thank you!")


print(user_dict)
