import re


def check_string(match_result):
    if match_result:
        print("Correct string.")
    else:
        print("Wrong string.")


user_string = input(
    "Enter a string: "
)

regex_match = re.search("^.+?\d+_[A-Z]+$", user_string)
check_string(regex_match)
