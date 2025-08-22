import math
side = int(input("Please enter the size of the square's side: "))

area = side**2
perimeter = side*4

print(f"Area of the square is {area}")
print(f"Perimeter of the square is {perimeter}")

sum = math.sqrt(area) + math.sqrt(perimeter)
print(f"The sum of the square root of the area and the perimeter is: {sum:.2f}")