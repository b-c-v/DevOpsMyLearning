import re


def check_string(match_result):
    if match_result:
        print("Correct string.")
    else:
        print("Wrong string.")


user_string = input(
    "Enter a string that contains at least 5 digits or 4 uppercase letters: "
).strip()

regex_match = re.search(r"(\d{5,})|([A-Z]{4})", user_string)
check_string(regex_match)
