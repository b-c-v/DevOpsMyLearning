import re


def check_string(match_result):
    if match_result:
        print("Correct string.")
    else:
        print("Wrong string.")


user_string = input("Enter a string that ends with a number: ")
user_number = int(input("Enter the number that should end the string: "))

pattern = str(user_number) + "$"
regex_match = re.search(pattern, user_string)
check_string(regex_match)
