import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def show_age_name():
    user_name = simpledialog.askstring("Input", "Enter your name", parent=root)
    if not user_name:
        return

    user_age = simpledialog.askinteger("Input", "Enter your age", parent=root)

    if user_age is None:
        return

    # Show the result in a message box
    messagebox.showinfo("Result", f"Hi {user_name}! Your age is {user_age}!")


# Create the MAIN WINDOW
root = tk.Tk()

# Hide the main window so no buttons or empty window are shown
root.withdraw()

# Run the calculation immediately
show_age_name()

# Properly close the Tkinter application
root.destroy()
