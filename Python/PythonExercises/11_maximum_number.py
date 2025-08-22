number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 == number2:
    print(f"The numbers are equal")
elif number1 > number2:
    print(f"First number {number1} is bigger then second {number2}")
else:
    print(f"Second number {number2} is bigger then first {number1}")

# difference between 3 numbers
maximum = max(number1, number2, number3)

if number1 == number2 and number1 == number3:
    print(f"The numbers are equal")
elif maximum == number1:
    print(f"First number {number1} is the biggest")
elif maximum == number2:
    print(f"Second number {number2} is the biggest")
else:
    print(f"Third number {number3} is the biggest")
