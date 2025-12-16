import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox


def calculate_cube():
    user_number = simpledialog.askinteger("Input", "Enter any number", parent=root)

    if user_number is None:
        return

    # Calculate the result
    result_square = user_number**3
    result_cube = user_number**3

    # Show the result in a message box
    messagebox.showinfo(
        "Result",
        f"{user_number}\u00b2 = {result_square}\n{user_number}\u00b3 = {result_cube}",
    )


# Create the MAIN WINDOW
root = tk.Tk()

# Hide the main window so no buttons or empty window are shown
root.withdraw()

# Run the calculation immediately
calculate_cube()

# Properly close the Tkinter application
root.destroy()
