v_initial = float(
    input(f"Please enter a value of the initial speed in m/s: ").replace(",", ".")
)
v_final = float(
    input(f"Please enter a value of the final speed in m/s: ").replace(",", ".")
)
time = float(input(f"Please enter the time in seconds: ").replace(",", "."))

a = (v_final - v_initial) / time

print(f"The acceleration of the object is { a } m/s\u00B2")

# find time taken by the object
v_initial2 = float(
    input(f"Please enter a value of the initial speed in m/s: ").replace(",", ".")
)
v_final2 = float(
    input(f"Please enter a value of the final speed in m/s: ").replace(",", ".")
)
a2 = float(input(f"Please enter a value of the acceleration in m/s\u00B2: ").replace(",", "."))
time = (v_final2 - v_initial2) / a2
print(f"The time taken by the object is {time} seconds")
