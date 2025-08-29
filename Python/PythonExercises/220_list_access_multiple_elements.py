user_list = []

amount_numbers = int(input("How many values do you want to enter in the list: "))

for i in range(amount_numbers):
    user_element = input(f"Enter your {i+1} element: ")
    user_list.append(user_element)

print(f"Your list is {user_list}")


def check_index(index, user_list):
    if not 0 <= index < len(user_list):
        print("You select wrong index")
        return False
    else:
        return True


start_index = int(input(f"Start index: "))


if check_index(start_index, user_list):
    end_index = int(input("End index: "))

    if check_index(end_index, user_list):
        if end_index > start_index:
            print(f"You selected from the list: {user_list[start_index:end_index]}")
        else:
            print(
                f"You selected from the list (reversed): {user_list[end_index:start_index]}"
            )
