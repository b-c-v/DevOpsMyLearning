import math

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))


def solve(a, b, c):
    D = math.pow(b, 2) - 4 * a * c
    if D > 0:
        x1 = (-b - math.sqrt(D)) / (2 * a)
        x2 = (-b + math.sqrt(D)) / (2 * a)
        print("There're two roots:")
        return min(x1, x2), max(x1, x2)
    elif D == 0:
        print("There is one root:")
        return -b / (2 * a), -b / (2 * a)
    else:
        return "No roots"


print(solve(a, b, c))
