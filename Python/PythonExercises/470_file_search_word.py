try:
    source_file_path = input("Enter the source file path: ").strip()
    with open(source_file_path, "r", encoding="utf-8") as source_file:
        search_word = input("Enter a word to search in the file: ").strip()
        file_content = source_file.readlines()
        for line in file_content:
            if search_word.lower() in line.lower():
                print(f"Word {search_word} is found in: {line}")
except FileNotFoundError:
    print("File doesn't exist")
