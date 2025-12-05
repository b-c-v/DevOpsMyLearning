try:
    source_file_path = input("Enter the source file path: ").strip()
    with open(source_file_path, "r", encoding="utf-8") as source_file:
        file_content = source_file.readlines()
    try:
        line_number = int(
            input(f"Enter the line number to read (0 to {len(file_content)-1}): ").strip()
        )
    except ValueError:
        print("Please enter a valid number!")
    try:
        print(f"Line {line_number} content:\n{file_content[line_number]}")
    except IndexError:
        print(f"The maximum line number must be less than {len(file_content)}")
except FileNotFoundError:
    print("File doesn't exist")
