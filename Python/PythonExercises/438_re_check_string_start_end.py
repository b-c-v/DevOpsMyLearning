import re


def check_string(match_result):
    if match_result:
        print("You entered the correct string.")
    else:
        print("You entered the wrong string.")


user_string = input(
    "Enter a string that starts with the letter 'm' or 'M' and ends with the digit '0' or '1': "
)
match_result_reg = re.search("^[mM]\w*[01]$", user_string)
check_string(match_result_reg)
