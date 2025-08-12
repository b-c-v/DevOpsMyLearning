import math

radius = float(input("Enter a radius in mm: "))
area = math.pi * radius**2
circumference = 2 * math.pi * radius
print(f"Area of the circle with the radius {radius} is {area:.2f} mm\u00b2")
print(f"Circumference of the circle with the radius {radius} is {circumference:.2f} mm")

total = (circumference + area) / 2
print(f"Sum of their half is {total:.2f}")
