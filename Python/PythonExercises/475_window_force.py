import tkinter as tk

BACKGROUND_COLOR = "orange"


def calculate_force():
    try:
        # Convert the entry text to an integer
        user_mass = int(mass_number.get().replace(",", "."))
        user_acceleration = int(time_number.get().replace(",", "."))
    except ValueError:
        print("Please enter only whole numbers in all fields.")
        return

    # Calculate the Force
    force = user_mass * user_acceleration

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Calculated force")
    result_window.geometry("400x200")

    # Display force
    tk.Label(result_window, text=f"Force: {force:.2f} N").pack(pady=5)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Force calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

tk.Label(root, text="Enter a mass of the object in kg: ").pack(pady=5, padx=20)
mass_number = tk.Entry(root)
mass_number.pack(pady=5, padx=20)
tk.Label(root, text="Enter a value of the acceleration in m/s\u00b2: ").pack(
    pady=5, padx=20
)
time_number = tk.Entry(root)
time_number.pack(pady=5, padx=20)


# Button to calculate total and average scores
tk.Button(root, text="Calculate force", command=calculate_force).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
