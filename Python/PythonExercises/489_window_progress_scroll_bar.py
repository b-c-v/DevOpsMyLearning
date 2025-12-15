import tkinter as tk
from tkinter.ttk import Progressbar, Scrollbar, Button


# Function is called when the button is clicked. It increases the progress bar's value by 10 units.
def increase_progress():
    if progress["value"] < progress["maximum"]:
        progress["value"] += 10


# Create the main application window
root = tk.Tk()
root.geometry("400x300")
root.title("Progress Bar with Scrollbar")

# Create a horizontal progress bar widget
progress = Progressbar(root, orient="horizontal", mode="determinate", length="300", maximum="100")
progress.pack(pady=20)  # Place the progress bar in the window

# Create a button to control the progress bar
btn = Button(root, text="Increase progress", command=increase_progress)
btn.pack()


# *** Scroll bar ***

# Create a frame to hold Text and Scrollbar together
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Create a vertical scrollbar
scrollbar = Scrollbar(text_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

# Create a Text widget (scrollable content)
text_widget = tk.Text(
    text_frame,
    wrap="word",
    yscrollcommand=scrollbar.set
)
text_widget.pack(side="left", fill="both", expand=True)

# Connect scrollbar to the Text widget
scrollbar.config(command=text_widget.yview)

# Insert sample text so scrolling is visible
for i in range(1, 51):
    text_widget.insert("end", f"Line {i}\n")

# Start the Tkinter event loop
root.mainloop()