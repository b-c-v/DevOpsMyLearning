import tkinter as tk
from tkinter import messagebox

BACKGROUND_COLOR = "orange"


def save_text_to_file():
    text = user_text.get().strip()
    filename = user_filename.get().strip()

    if not text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return
    try:
        with open(filename, "a") as file:
            print(f'Saving word "{text}" to the file "{filename}"')
            file.write(text + "\n")
        # Inform the user that the text was saved successfully
        messagebox.showinfo("Success", f'Text was saved to "{filename}".')
        # Clear the text entry after saving
        user_text.delete(0, tk.END)
    except OSError as error:
        # Show an error message if file operation fails
        messagebox.showerror("File Error", f"Could not save file:\n{error}")


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Save text to the file")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

tk.Label(root, text="Enter any text: ").pack(pady=5, padx=20)
user_text = tk.Entry(root)
user_text.pack(pady=5, padx=20)

tk.Label(root, text="Enter filename: ").pack(pady=5, padx=20)
user_filename = tk.Entry(root)
user_filename.pack(pady=5, padx=20)

# Button to calculate total and average scores
tk.Button(root, text="Save text", command=save_text_to_file).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
