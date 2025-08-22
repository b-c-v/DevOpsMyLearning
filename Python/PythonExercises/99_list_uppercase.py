uppercase_list = []
lowercase_list = []


def check_case(word, case_type):
    if case_type == "uppercase":
        return word == word.upper()
    else:
        return word == word.lower()


def add_to_list(target_list, case_type):
    while True:
        user_string = input(f"Enter any word in {case_type}: ")
        if check_case(user_string, case_type):
            target_list.append(user_string)
        else:
            print(f"The word should be written in {case_type}. Please try again!")
        answer = input("Do you want to add another word Y/n? ")
        if answer.lower() != "y":
            break


add_to_list(lowercase_list, "lowercase")
print(f"Your lowercase list: {lowercase_list}")

add_to_list(uppercase_list, "uppercase")
print(f"Your uppercase list: {uppercase_list}")
