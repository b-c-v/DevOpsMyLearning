import math

number = int(input("Please enter any number: "))

print(f"Factorial of the number {number} is {math.factorial(number)}")

# calculate factorial using loop
factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of the number {number} using a for loop is {math.factorial(number)}")
