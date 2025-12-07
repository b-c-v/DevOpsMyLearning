import tkinter as tk

BACKGROUND_COLOR = "orange"


def calculate_acceleration():
    try:
        # Convert the entry text to an integer
        user_velocity = int(velocity_number.get())
        user_time = int(time_number.get())
    except ValueError:
        print("Please enter only whole numbers in all fields.")
        return

    # Calculate the acceleration
    acceleration = user_velocity / user_time

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Acceleration result")
    result_window.geometry("400x200")

    # Display acceleration
    tk.Label(result_window, text=f"Acceleration: {acceleration:.2f} m/s²").pack(pady=5)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Acceleration calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

tk.Label(root, text="Enter change in velocity in m/s: ").pack(pady=5)
velocity_number = tk.Entry(root)
velocity_number.pack(pady=5, padx=20)
tk.Label(root, text="Enter time in s: ").pack(pady=5)
time_number = tk.Entry(root)
time_number.pack(pady=5, padx=20)


# Button to calculate total and average scores
tk.Button(root, text="Calculate acceleration", command=calculate_acceleration).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
