user_marks = int(input("Please enter your marks: "))


def check_scholarship(marks):

    if marks == 1100:
        print("You have free education")
    elif marks >= 1000:
        print("You have 80% monthly fees deduction")
    elif marks >= 900:
        print("You have 60% monthly fees deduction")
    elif marks >= 800:
        print("You have 40% monthly fees deduction")
    elif marks >= 700:
        print("You have 30% monthly fees deduction")
    elif marks >= 600:
        print("There is not scholarship")


if user_marks < 600 or user_marks > 1100:
    print("Enter valid number!")
else:
    check_scholarship(user_marks)
