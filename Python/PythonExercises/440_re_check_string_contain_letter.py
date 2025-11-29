import re


def check_string(match_result):
    if match_result:
        print("Correct string.")
    else:
        print("Wrong string.")


user_string = input("Enter a string that contains the letter 'm': ")

lowercase_letter_match = re.search("[m]", user_string)
check_string(lowercase_letter_match)

user_string = input("Enter a string that contains the number '6': ")
uppercase_letter_match = re.search("[6]", user_string)
check_string(uppercase_letter_match)
