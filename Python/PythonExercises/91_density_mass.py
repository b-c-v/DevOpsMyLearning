mass = float(input(f"Enter mass of the object: ").replace(",", "."))
volume = float(input(f"Enter volume of the object: ").replace(",", "."))

density = mass / volume

print(f"Density of the object is {density}")

mass = density * volume
print(f"Mass of the object is {mass}")
