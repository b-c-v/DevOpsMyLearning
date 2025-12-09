import tkinter as tk

BACKGROUND_COLOR = "orange"
NUMBER_OF_ITEMS = 3


def show_uppercase_word():
    uppercase_list = []
    # Loop through each Entry widget to get user input
    for entry in word_entries:
        user_word = entry.get()
        if user_word == user_word.upper() and user_word != "":
            uppercase_list.append(user_word)

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry()

    # Display total score
    tk.Label(
        result_window,
        text=f"Only uppercase words:\n{uppercase_list}",
    ).pack(pady=5, padx=20)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Uppercase word checker")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text=f"Enter {NUMBER_OF_ITEMS} words below: ").pack(pady=5, padx=20)

word_entries = []

# Create input fields dynamically based on NUMBER_OF_ITEMS
for i in range(1, NUMBER_OF_ITEMS + 1):
    frame = tk.Entry(root)
    frame.pack(pady=5, padx=10)
    # Label describing the word number
    tk.Label(frame, text=f"Word {i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR).pack(
        side="left"
    )

    # Entry widget for user input
    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    word_entries.append(entry)

# Button to show uppercase words
tk.Button(root, text="Show only uppercase words", command=show_uppercase_word).pack(
    pady=10
)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
