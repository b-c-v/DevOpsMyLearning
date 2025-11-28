import re


def check_string(match_result):
    if match_result:
        print("You entered the correct string.")
    else:
        print("You entered the wrong string.")


user_string = input(
    "Enter a string that starts with the letter 'f' and ends with the letter 'z': "
)
match_result_reg = re.search("^f\w*z$", user_string)
check_string(match_result_reg)
