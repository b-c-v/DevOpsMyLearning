import math

number = float(input(f"Please enter any number that needs to be rounded up: ").replace(",", "."))

print(f"Round up of the number {number} is {round(number)}")
print(f"Ceil  of the number {number} is {math.ceil(number)}")
print(f"Floor of the number {number} is {math.floor(number)}")
