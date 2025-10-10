import tkinter as tk

BACKGROUND_COLOR = "orange"


def show_data():
    # Get user input
    first_number = int(entry_first_number.get())
    second_number = int(entry_second_number.get())
    user_string = entry_user_string.get()

    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("User Information")
    new_window.geometry("400x400")

    # Display the collected information
    tk.Label(new_window, text=f"First number: {first_number}").pack(pady=5)
    tk.Label(new_window, text=f"Second number: {second_number}").pack(pady=5)
    tk.Label(
        new_window, text=f"Remainder of division: {first_number % second_number}"
    ).pack(pady=5)
    tk.Label(new_window, text=f"String in uppercase: {user_string.upper()}").pack(
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

# First Number
tk.Label(root, text="Enter First Number:").pack(pady=5)
entry_first_number = tk.Entry(root)  # Create the widget
entry_first_number.pack(pady=5)  # Place it on the window

# Second Number
tk.Label(root, text="Enter Second Number:").pack(pady=5)
entry_second_number = tk.Entry(root)
entry_second_number.pack(pady=5)

# User String
tk.Label(root, text="Enter any string:").pack(pady=5)
entry_user_string = tk.Entry(root)
entry_user_string.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=show_data).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
