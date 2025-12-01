import sys


# Define a few example objects whose memory usage we want to inspect
number = 42  # An integer object
text = "Hello, world!"  # A string object
numbers_list = [1, 2, 3, 4, 5]  # A list containing integers
numbers_dict = {"a": 1, "b": 2}  # A dictionary with string keys and integer values


# Print the type and memory size of each object
# sys.getsizeof() returns the size of the object in bytes
print("Memory usage of objects (in bytes):")

print(f"Integer (number): {sys.getsizeof(number)} bytes")
print(f"String (text): {sys.getsizeof(text)} bytes")
print(f"List (numbers_list): {sys.getsizeof(numbers_list)} bytes")
print(f"Dictionary (numbers_dict): {sys.getsizeof(numbers_dict)} bytes")


# Demonstrate that containers do not include the size of the objects they reference
# Here, we sum the sizes of individual elements in the list manually
total_list_size = sys.getsizeof(numbers_list)  # Size of the list object itself

for item in numbers_list:
    total_list_size += sys.getsizeof(item)  # Add the size of each element

print(
    f"\nApproximate total size of numbers_list including elements: {total_list_size} bytes"
)
