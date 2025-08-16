import scipy.constants as const

# python -m venv .scipy
# source .scipy/bin/activate
# pip install scipy

mass_1 = float(input(f"Enter a mass of the first object in kg: ").replace(",", "."))
mass_2 = float(input(f"Enter a mass of the second object in kg: ").replace(",", "."))
distance = float(input(f"Enter a distance between two objects in m: ").replace(",", "."))
print(const.G)

gravity_force = (const.G * (mass_1 * mass_2)) / distance**2

print(f"The force of gravity is {gravity_force:.3f}")
