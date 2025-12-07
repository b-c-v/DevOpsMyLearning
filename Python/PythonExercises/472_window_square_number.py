import tkinter as tk

BACKGROUND_COLOR = "orange"


def calculate_cube():
    try:
        # Convert the entry text to an integer
        user_number_1 = int(first_number.get())
        user_number_2 = int(second_number.get())
    except ValueError:
        print("Please enter only whole numbers in all fields.")
        return

    # Calculate the result
    # 1. Cube each number
    # 2. Add the cubes
    # 3. Cube the final sum
    result = (user_number_1 ** 3 + user_number_2 ** 3) ** 3

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry("400x200")

    # Display total score
    tk.Label(result_window, text=f"Result: {result}").pack(pady=5)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# First number
tk.Label(root, text="Enter the first number: ").pack(pady=5)
first_number = tk.Entry(root)
first_number.pack(pady=5, padx=5)

# Second number
tk.Label(root, text="Enter the second number: ").pack(pady=5)
second_number = tk.Entry(root)
second_number.pack(pady=5, padx=5)


# Button to calculate total and average scores
tk.Button(root, text="Calculate", command=calculate_cube).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
