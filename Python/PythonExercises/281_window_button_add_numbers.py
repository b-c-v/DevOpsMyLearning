import tkinter as tk


def on_button_click():
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(f"The sum of two numbers: {number_1 + number_2}")


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

# Add button
button = tk.Button(root, text="Calculate sum", command=on_button_click)
button.pack(pady=20)


# Start the event loop (keeps window open)
root.mainloop()
