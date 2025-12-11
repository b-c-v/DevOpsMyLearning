import tkinter as tk

BACKGROUND_COLOR = "orange"
NUMBER_OF_ITEMS = 3


def show_min_max_number():
    numbers_list = []
    # Loop through each Entry widget to get user input
    for entry in word_entries:
        user_number = int(entry.get())
        numbers_list.append(user_number)

    min_number = min(numbers_list)
    max_number = max(numbers_list)

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")

    if min_number == max_number:
        tk.Label(
            result_window,
            text=f"The biggest and the smallest numbers are equal",
        ).pack(pady=5, padx=20)
    else:
        tk.Label(
            result_window,
            text=f"The biggest number is: {max_number}",
        ).pack(pady=5, padx=20)
        tk.Label(
            result_window,
            text=f"The smallest number is: {min_number}",
        ).pack(pady=5, padx=20)
    if min_number < 0:
        tk.Label(
            result_window,
            text=f"Your minimum number is negative: {min_number}",
        ).pack(pady=5, padx=20)
    if max_number < 0:
        tk.Label(
            result_window,
            text=f"Your maximum number is negative: {max_number}",
        ).pack(pady=5, padx=20)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Number comparison tool")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text=f"Enter {NUMBER_OF_ITEMS} numbers below: ").pack(pady=5, padx=20)

word_entries = []

# Create input fields dynamically based on NUMBER_OF_ITEMS
for i in range(1, NUMBER_OF_ITEMS + 1):
    frame = tk.Entry(root)
    frame.pack(pady=5, padx=10)
    # Label for each numbered input
    tk.Label(
        frame, text=f"Number #{i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR
    ).pack(side="left")

    # Entry widget for user input
    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    word_entries.append(entry)

# Button that triggers minimum/maximum comparison
tk.Button(root, text="Show result of comparison", command=show_min_max_number).pack(
    pady=10
)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
