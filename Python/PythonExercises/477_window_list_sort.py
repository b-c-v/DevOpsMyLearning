import tkinter as tk

BACKGROUND_COLOR = "orange"
AMOUNT_OF_NAMES = 6


def sort_usernames():
    user_names = []
    # Get user input
    for entry in name_entries:
        name = entry.get()
        if len(name) > 5:
            user_names.append(name)

    user_names.sort()
    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry()

    tk.Label(result_window, text=f"Username: {user_names}").pack(pady=5, padx=20)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Usernames sorting")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

tk.Label(root, text="Enter six names of users below: ").pack(pady=5, padx=20)

name_entries = []

# Create input fields dynamically based on AMOUNT_OF_NAMES
for i in range(1, AMOUNT_OF_NAMES + 1):
    frame = tk.Entry(root)
    frame.pack(pady=5, padx=10)
    # Label for each score input
    tk.Label(frame, text=f"Name {i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR).pack(
        side="left"
    )

    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    name_entries.append(entry)

# Button to sort user_names
tk.Button(root, text="Show names", command=sort_usernames).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
