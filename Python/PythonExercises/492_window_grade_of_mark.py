import tkinter as tk
from tkinter import messagebox  # For showing error pop-up messages

BACKGROUND_COLOR = "orange"


def show_grade():
    # Get user input
    try:
        user_mark = int(entry_user_mark.get())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter only whole numbers in the field."
        )
        return

    # Create a new pop-up window to display the result
    result_window = tk.Toplevel(root)
    result_window.title(f"Your grade")
    result_window.geometry("300x200")

    if user_mark >= 95:
        grade = "A+"
    elif user_mark >= 80:
        grade = "A"
    elif user_mark >= 70:
        grade = "B"
    elif user_mark >= 60:
        grade = "C"
    else:
        message = "You FAIL!"

    if user_mark >= 60:
        tk.Label(
            result_window,
            text=f"Your grade is {grade}",
        ).pack(padx=10, pady=10)
    else:
        tk.Label(
            result_window,
            text=f"{message}",
        ).pack(padx=10, pady=10)


def close():
    root.destroy()


# Main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("Grade calculator")
root.option_add("*Font", "Arial 14")

# User String
tk.Label(root, text="Enter your mark:").pack(pady=5)
entry_user_mark = tk.Entry(root)
entry_user_mark.pack(pady=5)

# Submit button
tk.Button(root, text="Show your grade", command=show_grade).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close).pack(pady=10)

# Run the application
root.mainloop()
