import tkinter as tk

BACKGROUND_COLOR = "orange"


def count_words():
    # Get user input
    user_string = entry_user_string.get()
    word_count = len(user_string.split())
    spaces_count = user_string.count(" ")

    # Create a new pop-up window to display the result
    new_window = tk.Toplevel(root)
    new_window.title("Counted words")
    new_window.geometry("400x400")

    # Display the results to the user
    tk.Label(new_window, text=f"In your sentence:\n{word_count} words").pack(pady=5)
    tk.Label(new_window, text=f"{spaces_count} spaces").pack(pady=5)
    tk.Label(new_window, text=f"{len(user_string)} characters").pack(pady=5)
    tk.Label(
        new_window, text=f"{len(user_string) - spaces_count} characters without spaces"
    ).pack(pady=5)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("Count total number of words")
root.option_add("*Font", "Arial 14")

# User String
tk.Label(root, text="Enter any string:").pack(pady=5)
entry_user_string = tk.Entry(root)
entry_user_string.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=count_words).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
