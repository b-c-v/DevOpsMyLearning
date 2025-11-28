import re


def check_string(match_result):
    if match_result:
        print("You entered the correct string.")
    else:
        print("You entered the wrong string.")


user_string = input(
    "Enter a string that starts and ends with any letter, digit or underscore: "
)
match_result_reg = re.search("^\w.*\w$", user_string)
check_string(match_result_reg)
