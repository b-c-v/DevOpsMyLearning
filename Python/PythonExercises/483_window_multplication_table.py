import tkinter as tk
from tkinter import messagebox  # For showing error pop-up messages

BACKGROUND_COLOR = "orange"


def multiplication_table():
    # Get user input
    try:
        user_number = int(entry_user_number.get())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter only whole numbers in the field."
        )
        return

    # Create a new pop-up window to display the result
    new_window = tk.Toplevel(root)
    new_window.title(f"Multiplication table of number {user_number}")
    new_window.geometry("400x400")

    # Display the results to the user
    for i in range(1, 11):
        tk.Label(new_window, text=f"{user_number} * {i} = {user_number * i}").pack(
            pady=5
        )


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("Multiplication table generator")
root.option_add("*Font", "Arial 14")

# User String
tk.Label(root, text="Enter any number:").pack(pady=5)
entry_user_number = tk.Entry(root)
entry_user_number.pack(pady=5)

# Submit button
tk.Button(root, text="Show multiplication table", command=multiplication_table).pack(
    pady=10
)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
