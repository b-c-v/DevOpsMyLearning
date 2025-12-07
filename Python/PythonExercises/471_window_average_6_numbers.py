import tkinter as tk

BACKGROUND_COLOR = "orange"
NUMBER_OF_SCORES = 6


def calculate_total_and_average():
    scores = []
    # Get user input
    for entry in score_entries:
        try:
            # Convert the entry text to an integer
            score = int(entry.get())
            scores.append(score)
        except ValueError:
            print("Please enter only whole numbers in all fields.")
            return

    # Calculate total and average scores
    total_marks = sum(scores)
    average_marks = total_marks / NUMBER_OF_SCORES

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry("400x200")

    # Display total score
    tk.Label(result_window, text=f"Total of all scores: {total_marks}").pack(pady=5)

    # Display average score
    tk.Label(result_window, text=f"Average score: {average_marks:.2f}").pack(pady=5)


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Score calculator")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

# User character
tk.Label(root, text="Enter six scores below: ").pack(pady=5, padx=20)

score_entries = []

# Create input fields dynamically based on NUMBER_OF_SCORES
for i in range(1, NUMBER_OF_SCORES + 1):
    frame = tk.Entry(root)
    frame.pack(pady=5, padx=10)
    # Label for each score input
    tk.Label(
        frame, text=f"Score {i}: ", width=10, anchor="w", bg=BACKGROUND_COLOR
    ).pack(side="left")

    # Entry field for the score
    entry = tk.Entry(frame)
    entry.pack(side="left")
    # Save entry widget for later access
    score_entries.append(entry)

# Button to calculate total and average scores
tk.Button(root, text="Calculate", command=calculate_total_and_average).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
