import tkinter as tk

BACKGROUND_COLOR = "orange"


def show_data():
    # Get user input
    first_name = entry_name.get()
    surname = entry_surname.get()
    number = int(entry_number.get())

    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("User Information")
    new_window.geometry("400x400")

    # Display the collected information
    tk.Label(new_window, text=f"First Name: {first_name}").pack(pady=5)
    tk.Label(new_window, text=f"Surname: {surname}").pack(pady=5)
    tk.Label(new_window, text=f"Cube of the number {number}: {number**3}").pack(pady=5)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("My Application")
root.option_add("*Font", "Arial 14")

# First Name
tk.Label(root, text="Enter First Name:").pack(pady=5)
entry_name = tk.Entry(root)  # Create the widget
entry_name.pack(pady=5)  # Place it on the window

# Surname
tk.Label(root, text="Enter Surname:").pack(pady=5)
entry_surname = tk.Entry(root)
entry_surname.pack(pady=5)

# Name
tk.Label(root, text="Enter Number:").pack(pady=5)
entry_number = tk.Entry(root)
entry_number.pack(pady=5)

# Submit button
tk.Button(root, text="Submit", command=show_data).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
