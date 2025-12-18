import tkinter as tk

BACKGROUND_COLOR = "orange"


def convert_lowercase():
    # Get user input
    user_string = entry_user_string.get()

    if not user_string:
        message = "Please enter a string."
    elif user_string.islower():
        message = "String is already in lowercase"
    else:
        message = user_string.lower()

    # Create a new pop-up window to display the result
    result_window = tk.Toplevel(root)
    result_window.title("Result of converting")
    result_window.geometry("400x200")

    # Display the results to the user
    tk.Label(result_window, text=f"{message}").pack(pady=5)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("Lowercase converter")
root.option_add("*Font", "Arial 14")

# User String
tk.Label(root, text="Enter any string:").pack(pady=5)
entry_user_string = tk.Entry(root)
entry_user_string.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=convert_lowercase).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
