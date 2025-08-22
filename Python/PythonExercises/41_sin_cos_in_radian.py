import math

angle_degrees = float(input("Enter any angle: "))
angle_radians = math.radians(angle_degrees)

cos_radians = math.cos(angle_radians)
sin_radians = math.sin(angle_radians)

# Convert sin and cos values to degree units
sin_degrees = math.degrees(sin_radians)
cos_degrees = math.degrees(cos_radians)

print(f"Cos of {angle_degrees} degrees is {cos_radians} rad")
print(f"Sin of {angle_degrees} degrees is {sin_radians} rad")
print(f"Cos of {angle_degrees} degrees is {cos_degrees}")
print(f"Sin of {angle_degrees} degrees is {sin_degrees}")
