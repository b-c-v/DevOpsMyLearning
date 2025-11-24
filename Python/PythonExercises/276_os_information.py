# Use os.name when you need a simple check ('nt' for Windows, 'posix' for Unix-like systems).
import os
import platform

# OS name (e.g., 'posix' for Linux/Mac, 'nt' for Windows)
print("OS Name:", os.name)

# psutil library provides system monitoring functions
import psutil

# Get CPU usage as a percentage
cpu_usage = psutil.cpu_percent(interval=1)  # Measures CPU load over 1 second

# Get memory (RAM) statistics
memory_info = psutil.virtual_memory()  # Returns an object with RAM details
ram_total = memory_info.total  # Total RAM in bytes
ram_used = memory_info.used  # Used RAM in bytes
ram_percent = memory_info.percent  # Percentage of RAM used

# Print everything
print(f"CPU Usage: {cpu_usage}%")
print(f"RAM Total: {ram_total / (1024**3):.2f} GB")
print(f"RAM Used: {ram_used / (1024**3):.2f} GB")
print(f"RAM Usage: {ram_percent}%")
