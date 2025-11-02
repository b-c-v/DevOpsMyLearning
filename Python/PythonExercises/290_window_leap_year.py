import tkinter as tk

BACKGROUND_COLOR = "orange"


def check_year():
    # Get user input
    user_year = int(entry_user_year.get())

    if (user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0:
        year_type = "leap"
    else:
        year_type = "not leap"

    # Create a new window
    new_window = tk.Toplevel(root)
    new_window.title("User Information")
    new_window.geometry("400x400")

    # Display the collected information
    tk.Label(new_window, text=f"This is {year_type} year").pack(pady=5)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("My Application")
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text="Enter any year: ").pack(pady=5)
entry_user_year = tk.Entry(root)  # Create the widget
entry_user_year.pack(pady=5)  # Place it on the window

# Submit button
tk.Button(root, text="Submit", command=check_year).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
