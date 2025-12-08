import tkinter as tk

BACKGROUND_COLOR = "orange"
NUMBER_OF_ITEMS = 6


def calculate_total():
    sum_numbers = 0
    # Get user input
    for entry in number_entries:
        try:
            # Convert the entry text to an integer
            user_number = int(entry.get())
            if 10 > user_number > 5:
                sum_numbers += user_number
        except ValueError:
            print("Please enter only whole numbers in all fields.")
            return

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry()

    # Display total score
    tk.Label(
        result_window,
        text=f"Total of numbers bigger than 5 and less then 10 is - {sum_numbers}",
    ).pack(pady=5, padx=20)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text="Enter six numbers below: ").pack(pady=5, padx=20)

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
tk.Button(root, text="Calculate", command=calculate_total).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
