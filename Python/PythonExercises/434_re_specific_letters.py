import re


def check_string(match_result):
    if match_result:
        print("Correct string.")
    else:
        print("Wrong string.")


user_string = input("Enter a string that contains specific letters from a to f: ")

lowercase_letter_match = re.search("[a-f]", user_string)
check_string(lowercase_letter_match)

user_string = input("Enter a string that contains specific letters from A to F: ")
uppercase_letter_match = re.search("[A-F]", user_string)
check_string(uppercase_letter_match)
