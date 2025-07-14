number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operations = input("Enter type of operation +-*/: ")
operations_set = {"+", "-", "*", "/"}
if operations in operations_set:
    if operations == "+":
        print(number1 + number2)
    elif operations == "-":
        print(number1 - number2)
    elif operations == "*":
        print(number1 * number2)
    elif operations == "/":
        print(number1 / number2)
else:
    print("You entered wrong operation!")
