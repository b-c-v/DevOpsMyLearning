import tkinter as tk

# messagebox is a separate submodule, so you must import it explicitly:
from tkinter import messagebox


def on_button_click():
    # Show a message box when the 'Click Me' button is clicked.
    messagebox.showinfo("Information", "Thank you for clicking!")


def close():
    root.destroy()


# Create the main application window
root = tk.Tk()

# Set window title
root.title("My Application")

# Set window icon (Windows: .ico file)
icon = tk.PhotoImage(file="favicon.png")
root.iconphoto(True, icon)

# Add a label widget with text "Hello World!"
label = tk.Label(root, text="Hello World!", font=("Arial", 16), fg="blue", bg="yellow")
label.pack(pady=20)  # pack() places the widget in the window

# Set window size (width x height)
root.geometry("600x400")
root.configure(bg="orange")

# Disable user resizing (horizontal, vertical)
root.resizable(False, False)

# Add buttons
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)
button = tk.Button(root, text="Close", command=close)
button.pack(pady=40)


# Start the event loop (keeps window open)
root.mainloop()
