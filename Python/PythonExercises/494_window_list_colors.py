import tkinter as tk

BACKGROUND_COLOR = "orange"
NUMBER_OF_ITEMS = 3

COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]


def show_total_characters():
    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry()

    # Display total score
    for entry in color_entries:
        user_color = entry.get().strip().lower()
        if user_color in COLORS:
            message = f"The color {user_color} has {len(user_color)} characters"
        else:
            message = f"The value {user_color} in NOT a valid color."

        tk.Label(
            result_window,
            text=message,
        ).pack(pady=5, padx=20)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Color checker")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text=f"Enter {NUMBER_OF_ITEMS} colors below: ").pack(pady=5, padx=20)

color_entries = []

# Create input fields dynamically based on NUMBER_OF_ITEMS
for i in range(1, NUMBER_OF_ITEMS + 1):
    frame = tk.Entry(root)
    frame.pack(pady=5, padx=10)
    # Label describing the word number
    tk.Label(
        frame, text=f"Color #{i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR
    ).pack(side="left")

    # Entry widget for user input
    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    color_entries.append(entry)

# Button that triggers validation and result display
tk.Button(root, text="Check colors", command=show_total_characters).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
