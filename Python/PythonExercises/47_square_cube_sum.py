square_sum = 0
cube_sum = 0
for i in range(2):
    number = int(input("Enter any number: "))
    square_sum += number**2
    cube_sum += number**3
    print(f"The square of the number {number} is {number**2}")
    print(f"The cube of the number {number} is {number**3}")

print(f"The summary of square numbers is {square_sum}")
print(f"The summary of cube numbers is {cube_sum}")
