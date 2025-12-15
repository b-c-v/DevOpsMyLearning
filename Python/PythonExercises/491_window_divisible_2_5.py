import tkinter as tk
from tkinter import messagebox  # For showing error pop-up messages

BACKGROUND_COLOR = "orange"
NUMBER_OF_ITEMS = 3


def show_divisible_by_2_and_5():
    divisible_2_5 = []
    # Get user input
    for entry in number_entries:
        try:
            # Convert the entry text to an integer
            user_number = int(entry.get())
            if user_number % 2 == 0 and user_number % 5 == 0:
                divisible_2_5.append(user_number)
        except ValueError:
            messagebox.showerror(
                "Invalid input", "Please enter only whole numbers in all fields."
            )
            return
    divisible_2_5.sort()

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Numbers divisible by 2 and 5 in ascending order")
    result_window.geometry("500x200")

    # Display total score
    tk.Label(
        result_window,
        text=f"{divisible_2_5}",
    ).pack(pady=5, padx=20)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text=f"Enter {NUMBER_OF_ITEMS} numbers below: ").pack(pady=5, padx=20)

number_entries = []

# Create input fields dynamically based on NUMBER_OF_ITEMS
for i in range(1, NUMBER_OF_ITEMS + 1):
    frame = tk.Entry(root)
    frame.pack(pady=5, padx=10)
    # Label for each score input
    tk.Label(
        frame, text=f"Number {i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR
    ).pack(side="left")

    # Entry field for the score
    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    number_entries.append(entry)

# Button to calculate total and average scores
tk.Button(
    root,
    text="Show numbers divisible by 2 and 5 in ascending order",
    command=show_divisible_by_2_and_5,
).pack(pady=10, padx=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
