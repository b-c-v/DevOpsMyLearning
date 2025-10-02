import tkinter as tk

BACKGROUND_COLOR = "orange"

# Initialize main window
root = tk.Tk()
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)
root.title("My Application")
root.option_add("*Font", "Arial 14")

# Set window icon
icon = tk.PhotoImage(file="favicon.png")
root.iconphoto(True, icon)

# Add a text label
label = tk.Label(root, text="Hello World!")
label.pack(pady=20)  # pack() places the widget in the window


# Load background image
image_background = tk.PhotoImage(file="tmp.png")

# Create a label to hold the background
background_label = tk.Label(root)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  # Cover entire window


# Function to change background
def change_background():
    background_label.config(image=image_background)
    background_label.image = image_background  # Keep a reference


# Add button
button_background = tk.Button(root, text="Close", command=change_background)
button_background.pack(pady=5)

# Start the event loop (keeps window open)
root.mainloop()
