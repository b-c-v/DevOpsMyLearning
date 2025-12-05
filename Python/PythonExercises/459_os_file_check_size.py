import os.path

print(os.name)

file_name = "tmp.mp3"
file_size = int(os.path.getsize(file_name))
print(file_size)
# 1 MB = 1,048,576 Bytes
if 3 * 1048576 < file_size < 5 * 1048576:
    print(f"The size of the file {file_name} is {(file_size / 1048576):.2f} MB")
else:
    print(f"Size of the file {file_name} is {file_size} bytes")
