temperature_F = float(input("Enter a temperature in Fahrenheit: "))
temperature_C = (temperature_F - 32) * 5/9
temperature_K = (temperature_F + 459.67) * 5/9
print(f"Temperature in Celsius: {temperature_C:.3f}")
print(f"Temperature in Kelvin: {temperature_K:.3f}")