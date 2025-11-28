import re


def check_string(match_result):
    if match_result:
        return "is"
    else:
        return "isn't"


user_string = input("Enter any phrase: ")
user_chars = input(
    "Enter any character or set of characters that the string should start or end with: "
)
chars_match_start = re.search("^" + user_chars, user_string)
chars_match_end = re.search(user_chars + "$", user_string)
print(
    f"Your string {check_string(chars_match_start)} starting with the given characters."
)
print(f"Your string {check_string(chars_match_end)} ending with the given characters.")
