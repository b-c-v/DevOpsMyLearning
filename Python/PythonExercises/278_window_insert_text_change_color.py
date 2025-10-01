import tkinter as tk

# Create the main application window
root = tk.Tk()

# Set window title
root.title("My Application")

# Add a label widget with text "Hello World!"
label = tk.Label(root, text="Hello World!", font=("Arial", 16), fg="blue", bg="yellow")
label.pack(pady=20)  # pack() places the widget in the window

# Set window size (width x height)
root.geometry("600x400")
root.configure(bg="orange")

# Start the event loop (keeps window open)
root.mainloop()
