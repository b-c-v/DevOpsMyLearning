import tkinter as tk

BACKGROUND_COLOR = "orange"


def show_data():
    vowels = ["a", "e", "i", "o", "u"]
    # Get user input
    user_character = entry_character.get()
    user_string = entry_user_string.get()
    character_type = ""

    if user_character in vowels:
        character_type = "vowel"
    else:
        character_type = "consonant"

    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("User Information")
    new_window.geometry("400x400")

    # Display the collected information
    tk.Label(
        new_window, text=f'Your letter "{user_character}" is a {character_type}'
    ).pack(pady=5)
    tk.Label(new_window, text=f"Your reverse string is: {user_string[::-1]}").pack(
        pady=5
    )


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("My Application")
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text="Enter any character:").pack(pady=5)
entry_character = tk.Entry(root)  # Create the widget
entry_character.pack(pady=5)  # Place it on the window

# User string
tk.Label(root, text="Enter any string:").pack(pady=5)
entry_user_string = tk.Entry(root)
entry_user_string.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=show_data).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
