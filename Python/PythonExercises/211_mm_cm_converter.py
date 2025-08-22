mm = float(input("Please enter a value in mm: "))
cm = mm / 10
m = mm / 1000
km = mm / 1000000

print(f"{mm} mm is {cm:.3f} cm")
print(f"{mm} mm is {m:.3f} m")
print(f"{mm} mm is {km:.3f} km")

cm_2 = float(input("Please enter a value in cm: "))
m_2 = cm_2 / 100
km_2 = cm_2 / 100000
print(f"{cm_2} cm is {m_2:.3f} m")
print(f"{cm_2} cm is {km_2:.3f} km")