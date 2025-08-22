m = float(input(f"Please enter the mass of the object in kg: ").replace(",", "."))
a = float(
    input(f"Please enter a value of the acceleration in m/s\u00b2: ").replace(",", ".")
)

F = m * a

print(f"The force of the man is {F} newtons")


# find mass of the object
a2 = float(
    input(f"Please enter a value of the acceleration in m/s\u00b2: ").replace(",", ".")
)
F2 = float(input(f"Please enter the value of the force in N: ").replace(",", "."))

m2 = F2 / a2
print(f"The mass of the object is {m2} kg")
