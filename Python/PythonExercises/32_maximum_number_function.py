num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def max_two_numbers(number1, number2):
    if number1 == number2:
        print(f"The numbers are equal")
    elif number1 > number2:
        print(f"First number {number1} is bigger then second {number2}")
    else:
        print(f"Second number {number2} is bigger then first {number1}")


def min_two_numbers(number1, number2):
    if number1 == number2:
        print("The numbers are equal")
    elif number1 < number2:
        print(f"First number {number1} is smaller then second {number2}")
    else:
        print(f"Second number {number2} is smaller then first {number1}")


max_two_numbers(num1, num2)
min_two_numbers(num1, num2)
