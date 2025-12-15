import tkinter as tk
from tkinter import messagebox  # For showing error pop-up messages
import math

BACKGROUND_COLOR = "orange"


def calculate_factorial():
    # Get user input
    try:
        user_number = int(entry_user_number.get())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter only whole numbers in the field."
        )
        return

    # Check for negative numbers
    if user_number < 0:
        messagebox.showerror(
            "Invalid input", "Factorial is not defined for negative numbers."
        )
        return

    # Create a new pop-up window to display the result
    result_window = tk.Toplevel(root)
    result_window.title(f"Factorial of the number")

    factorial = 1
    for i in range(1, user_number + 1):
        tk.Label(
            result_window,
            text=f"{i} * {factorial} = {i * factorial}",
        ).pack(pady=5)
        factorial *= i

    tk.Label(
        result_window,
        text=f"Factorial of the number {user_number} is {math.factorial(user_number)}",
    ).pack(padx=10, pady=10)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("Factorial of the number")
root.option_add("*Font", "Arial 14")

# User String
tk.Label(root, text="Enter any number:").pack(pady=5)
entry_user_number = tk.Entry(root)
entry_user_number.pack(pady=5)

# Submit button
tk.Button(root, text="Show factorial of the number", command=calculate_factorial).pack(
    pady=10
)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
