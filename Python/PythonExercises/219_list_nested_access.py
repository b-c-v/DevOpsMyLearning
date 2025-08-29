nested_list = [[9, 7, 6, 5], [5, 4, 3], [2, 1, 0], [-1, -2, -3]]
print("Nested list:", nested_list)

outer_index = int(input("Enter nested list index: "))


def check_index(index, user_list):
    if not 0 <= index < len(user_list):
        print("You select wrong index")
        return False
    else:
        return True


if check_index(outer_index, nested_list):
    print(f"Selected nested list is: {nested_list[outer_index]}")
    inner_index = int(input("Enter list index: "))

    if check_index(inner_index, nested_list[outer_index]):
        print(f"Selected element is: {nested_list[outer_index][inner_index]}")
