number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

print(f"Before swap: number1 = {number1}, number2 = {number2}")

number1, number2 = number2, number1
print(f"After swap: number1 = {number1}, number2 = {number2}")


# arithmetic way
print(f"Before arithmetic swap: number1 = {number1}, number2 = {number2}")
number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2
print(f"After arithmetic swap: number1 = {number1}, number2 = {number2}")
