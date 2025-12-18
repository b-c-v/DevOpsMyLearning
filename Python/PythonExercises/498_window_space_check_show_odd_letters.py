import tkinter as tk

BACKGROUND_COLOR = "orange"


def space_check():

    # Get user input
    user_string = entry_user_string.get()
    odd_index_chars = []

    if " " in user_string:
        message = "The string contains spaces"
    else:
        message = "There are no spaces in this string"

    for index, char in enumerate(user_string):
        if index % 2 != 0:
            odd_index_chars.append(char)

    # Create a new pop-up window to display the result
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry("400x200")

    # Display the results to the user
    tk.Label(
        result_window,
        text=f'{message}\nLetters aat odd position: {"".join(odd_index_chars)}',
    ).pack(pady=5)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("Space checker and odd letters display")
root.option_add("*Font", "Arial 14")

# User String
tk.Label(root, text="Enter any string:").pack(pady=5)
entry_user_string = tk.Entry(root)
entry_user_string.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=space_check).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
