my_dict = {}


for i in range(3):
    author_name = input("Enter a name of the author: ")
    book_name = input("Enter a name of the book: ")
    my_dict[author_name] = book_name

last_key = list(my_dict.keys())[-1]
print(f"Last author is: {last_key}: {my_dict[last_key]}")

first_key = list(my_dict.keys())[0]
print(f"First author is: {first_key}: {my_dict[first_key]}")
