# Use os.name when you need a simple check ('nt' for Windows, 'posix' for Unix-like systems).
import os
import platform

# OS name (e.g., 'posix' for Linux/Mac, 'nt' for Windows)
print("OS Name:", os.name)


print("System:", platform.system())  # e.g., 'Windows', 'Linux'
print("Release:", platform.release())  # e.g., '10', '5.15.0-72-generic'
print("Version:", platform.version())  # Detailed OS version
print("Machine:", platform.machine())  # e.g., 'x86_64'
print("Processor:", platform.processor())  # CPU details
