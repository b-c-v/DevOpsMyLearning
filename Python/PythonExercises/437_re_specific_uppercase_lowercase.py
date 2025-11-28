import re


def check_string(match_result):
    if match_result:
        return "is"
    else:
        return "isn't"


user_string = input("Enter any phrase: ")
user_chars_start = input(
    "Enter any lowercase character or set of characters that the string should start with: "
).lower()
user_chars_end = input(
    "Enter any uppercase character or set of characters that the string should end with: "
).upper()
chars_match_start = re.search("^" + user_chars_start, user_string)
chars_match_end = re.search(user_chars_end + "$", user_string)
print(
    f"Your string {check_string(chars_match_start)} starting with the given characters."
)
print(f"Your string {check_string(chars_match_end)} ending with the given characters.")
