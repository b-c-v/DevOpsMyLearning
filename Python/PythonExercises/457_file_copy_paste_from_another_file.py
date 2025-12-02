try:
    source_file_path = input("Enter the source file path: ")
    # Open and read content of the source file in read mode
    with open(source_file_path, "r", encoding="utf-8") as source_file:
        file_content = source_file.read()
    string_to_exclude = input("Enter the string to remove from the file content: ")
    # Remove all occurrences of the user-specified string
    # str.replace() replaces the string with an empty string
    filtered_content = file_content.replace(string_to_exclude, "")
    # Open and write the modified content to the destination file
    destination_file_path = input("Enter the destination file path: ")
    with open(destination_file_path, "w", encoding="utf-8") as destination_file:
        # Write the modified content to the destination file
        destination_file.write(filtered_content)
    print("File content copied successfully, excluding the specified string.")
except FileNotFoundError:
    print("File doesn't exist")
