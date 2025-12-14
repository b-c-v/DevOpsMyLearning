import tkinter as tk
from tkinter import messagebox


def show_selection(event):
    selected_index = lst.curselection()
    if selected_index:
        selected_language = lst.get(selected_index[0])
        print("Выбран язык:", selected_language)
        # Show the result in a message box
        messagebox.showinfo("Result", f"You selected {selected_language}!")


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Programming Language Selector")  # Set a window title

lst = tk.Listbox(root, bd=10, fg="yellow", bg="black", cursor="cross")
lst.insert(0, "Python")
lst.insert(1, "C++")
lst.insert(2, "TypeScript")
lst.pack(padx=10, pady=10)
lst.bind("<<ListboxSelect>>", show_selection)
root.mainloop()
