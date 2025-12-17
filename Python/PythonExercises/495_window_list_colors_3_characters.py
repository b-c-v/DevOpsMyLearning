import tkinter as tk

BACKGROUND_COLOR = "orange"
NUMBER_OF_ITEMS = 5

VALID_COLORS = ["red", "orange", "yellow", "green", "blue", "violet"]


def get_valid_three_letter_colors(entries):
    valid_three_letter_colors = []
    invalid_inputs = []

    # Take only the the range from FIRST till LAST Entry widgets
    selected_entries = entries[1:-1]

    for entry in selected_entries:
        color = entry.get().strip().lower()

        if color not in VALID_COLORS:
            invalid_inputs.append(color)
        elif len(color) == 3:
            valid_three_letter_colors.append(color)

    return valid_three_letter_colors, invalid_inputs


def show_results():
    valid_colors, invalid_colors = get_valid_three_letter_colors(color_entries)
    message = []
    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")

    if invalid_colors:
        message.append(f"Invalid colors: {invalid_colors}")

    if valid_colors:
        message.append(f"Colors with 3 letters: {valid_colors}")

    if not message:
        message.append("No valid 3-letter colors were entered.")

    # Display results
    tk.Label(result_window, text="\n".join(message)).pack(pady=10, padx=20)


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
    # Label describing the color number
    tk.Label(
        frame, text=f"Color #{i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR
    ).pack(side="left")

    # Entry widget for user input
    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    color_entries.append(entry)

# Button that triggers validation and result display
tk.Button(root, text="Check colors", command=show_results).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
