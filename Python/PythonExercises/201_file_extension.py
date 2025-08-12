import os

while True:
    full_file_name = input("Enter any file namename with extension: ")
    file_name, file_extension = os.path.splitext(full_file_name)
    if file_extension == ".mp3":
        print("This file is not allowed")
    else:
        print(f"File name is: {file_name}")
        print(f"File extension is: {file_extension}")
        break
