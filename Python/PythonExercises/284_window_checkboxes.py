import tkinter as tk

BACKGROUND_COLOR = "orange"


def close():
    root.destroy()


def update_bg():
    # Background toggle
    if bg_red.get():
        label.config(bg="red")
    elif bg_blue.get():
        label.config(bg="blue")
    else:
        label.config(bg="white")


def update_fg():
    # Foreground (text color) toggle
    if fg_red.get():
        label.config(fg="red")
    elif fg_blue.get():
        label.config(fg="blue")
    else:
        label.config(fg="white")


def update_font_size():
    # Font size toggle
    if font_size_10.get():
        label.config(font=("Arial", 10))
    elif font_size_20.get():
        label.config(font=("Arial", 20))
    else:
        label.config(font=("Arial", 12))

    # Cursor toggle
    if cursor_var.get():
        label.config(cursor="hand2")
    else:
        label.config(cursor="arrow")


# Create the main application window
root = tk.Tk()

# Set window title
root.title("My Application")
# Set global size of the font in the window
root.option_add("*Font", "Arial 14")

# Set window icon
icon = tk.PhotoImage(file="favicon.png")
root.iconphoto(True, icon)

# Add a label widget with text "Hello World!"
label = tk.Label(root, text="Hello World!")
label.pack(pady=20)  # pack() places the widget in the window

# Set window size (width x height)
root.geometry("600x400")
root.configure(bg=BACKGROUND_COLOR)

# Variables for checkboxes
bg_red = tk.BooleanVar()
bg_blue = tk.BooleanVar()
fg_red = tk.BooleanVar()
fg_blue = tk.BooleanVar()
font_size_10 = tk.BooleanVar()
font_size_20 = tk.BooleanVar()


# Add checkboxes
tk.Checkbutton(
    root, text="Background red", variable=bg_red, command=update_bg, bg=BACKGROUND_COLOR
).pack(anchor="w")
tk.Checkbutton(
    root,
    text="Background blue",
    variable=bg_blue,
    command=update_bg,
    bg=BACKGROUND_COLOR,
).pack(anchor="w")
tk.Checkbutton(
    root, text="Foreground red", variable=fg_red, command=update_fg, bg=BACKGROUND_COLOR
).pack(anchor="w")
tk.Checkbutton(
    root,
    text="Foreground blue",
    variable=fg_blue,
    command=update_fg,
    bg=BACKGROUND_COLOR,
).pack(anchor="w")
tk.Checkbutton(
    root,
    text="Font Size 10 px",
    variable=font_size_10,
    command=update_font_size,
    bg=BACKGROUND_COLOR,
).pack(anchor="w")
tk.Checkbutton(
    root,
    text="Font Size 20 px",
    variable=font_size_20,
    command=update_font_size,
    bg=BACKGROUND_COLOR,
).pack(anchor="w")


# Add button
button_close = tk.Button(root, text="Close", command=close)
button_close.pack(pady=40)

# Start the event loop (keeps window open)
root.mainloop()
