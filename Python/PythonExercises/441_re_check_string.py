import re


def check_string(match_result):
    if match_result:
        print("Correct string.")
    else:
        print("Wrong string.")


user_string = input(
    "Enter a string that starts with an uppercase letters, contains lowercase letters, and ends with digits, an underscore, and a space: "
)

regex_match = re.search("[A-Z]+[a-z]+[0-9]+[_]+[ ]+", user_string)
check_string(regex_match)
