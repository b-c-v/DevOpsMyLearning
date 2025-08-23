import math

number = int(input("Enter any number: "))
previous_number = number - 1
next_number = number + 1

def square_cos_sin(number):
   print(f"The square is {number**2}")
   print(f"The cos is {math.cos(number)}")
   print(f"The sin is {math.sin(number)}")

print(f"Next number is {next_number}")
square_cos_sin(next_number)


print(f"Previous number is {previous_number}")
square_cos_sin(previous_number)
