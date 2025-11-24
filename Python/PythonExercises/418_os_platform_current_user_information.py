# os module to interact with the operating system
import os

# platform module to retrieve system and hardware information
import platform

# Print the username of the person currently logged into the system
print(os.getlogin())


print("System:", platform.system())  # e.g., 'Windows', 'Linux'
print("Release:", platform.release())  # e.g., '10', '5.15.0-72-generic'
print("Version:", platform.version())  # Detailed OS version
print("Machine:", platform.machine())  # e.g., 'x86_64'
print("Processor:", platform.processor())  # CPU details
