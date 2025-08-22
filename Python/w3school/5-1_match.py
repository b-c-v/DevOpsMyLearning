# The match statement is used to perform different actions based on different conditions.
# Instead of writing many if..else statements, you can use the match statement.
# The match statement selects one of many code blocks to be executed.

"""
- The match expression is evaluated once.
- The value of the expression is compared with the values of each case.
- If there is a match, the associated block of code is executed.
"""
day = 4  # Thursday
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

# Default Value.
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
# The value _ will always match, so it is important to place it as the last case to make it beahave as a default case.
day = 4  # Looking forward to the Weekend
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

# Combine Values.
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
day = 4  # Today is a weekday
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

# If Statements as Guards.
# You can add if statements in the case evaluation as an extra condition-check:
month = 5  # A weekday in May
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
