import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Scrollbar

BACKGROUND_COLOR = "orange"


def close_app():
    root.destroy()


def calculate_square():
    try:
        start = int(first_number.get())
        end = int(second_number.get())
    except ValueError:
        messagebox.showerror(
            "Invalid input", "Please enter only whole numbers in all fields."
        )
        return

    # Ensure correct order
    if start > end:
        start, end = end, start

    # Clear previous results
    text_widget.delete("1.0", "end")

    # Insert new results
    for number in range(start, end + 1):
        text_widget.insert("end", f"{number}² = {number ** 2}\n")


# Main window
root = tk.Tk()
root.title("Square calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")
root.geometry("400x600")

# First number
tk.Label(root, text=f"Enter the first number: ", bg=BACKGROUND_COLOR).pack(
    padx=5, pady=5
)
first_number = tk.Entry(root)
first_number.pack(padx=5, pady=5)

# Second number
tk.Label(root, text=f"Enter the second number: ", bg=BACKGROUND_COLOR).pack(
    padx=5, pady=5
)
second_number = tk.Entry(root)
second_number.pack(padx=5, pady=5)


# Submit button
tk.Button(root, text="Calculate square", command=calculate_square).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Result area with scrollbar
result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a vertical scrollbar
scrollbar = Scrollbar(result_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create a Text widget (scrollable content)
text_widget = tk.Text(result_frame, wrap="word", yscrollcommand=scrollbar.set)
text_widget.pack(side="left", fill="both", expand=True)

# Connect scrollbar to the Text widget
scrollbar.config(command=text_widget.yview)

# Run the application
root.mainloop()
