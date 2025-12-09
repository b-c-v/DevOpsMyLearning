import tkinter as tk

BACKGROUND_COLOR = "orange"
AMOUNT_OF_NAMES = 3


def close_app():
    root.destroy()


def show_last_book():
    last_key = list(author_book_entries.keys())[-1]
    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")

    # Get the text entered by the user from the Entry widgets
    last_author_name = last_key.get()
    last_book_name = author_book_entries[last_key].get()

    # Display last author and book
    tk.Label(
        result_window,
        text=f"Last author is: {last_author_name}, Book: {last_book_name}",
    ).pack(pady=5, padx=20)


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Author and book names")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

tk.Label(root, text=f"Enter {AMOUNT_OF_NAMES} names and their book titles below: ").pack(
    pady=5, padx=20
)


author_book_entries = {}

# Create input fields
for i in range(1, AMOUNT_OF_NAMES + 1):
    row_frame = tk.Entry(root)
    row_frame.pack(pady=5, padx=10)
    # Label for each score input
    tk.Label(
        row_frame,
        text=f"Author {i}: ",
        width=10,
        anchor="w",
        bg=BACKGROUND_COLOR,
    ).pack(side="left", padx=5)

    # Entry widget where the user types the author's name
    author_name_entry = tk.Entry(row_frame)
    author_name_entry.pack(side="left", expand=True, fill="x")
    # Save entry widget for later access

    # Label for book
    tk.Label(
        row_frame,
        text=f"Book: ",
        width=10,
        anchor="w",
        bg=BACKGROUND_COLOR,
    ).pack(side="left", padx=5)

    book_name_entry = tk.Entry(row_frame)
    book_name_entry.pack(side="left")

    # Store both Entry widgets in the dictionary for later use
    author_book_entries[author_name_entry] = book_name_entry

# Button to show last entry
tk.Button(root, text="Show last book", command=show_last_book).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Start the Tkinter event loop (keeps the window open)
root.mainloop()


# first_key = list(author_book_entries.keys())[0]
# print(f"First author is: {first_key}: {author_book_entries[first_key]}")
