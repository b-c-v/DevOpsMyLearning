import re


def check_string(x):
    if x:
        print("You entered the correct string.")
    else:
        print("You entered the wrong string.")


user_string_digit = input("Enter a string that starts and ends with a digit: ")

digit_is = re.search("^[0-9]+[A-za-z].+[0-9]$", user_string_digit)
check_string(digit_is)

user_string = input("Enter a string that starts and ends with a letter: ")
letter_is = re.search("^[A-Za-z].+[A-Za-z]$", user_string)
check_string(letter_is)
