import tkinter as tk
from tkinter import messagebox  # Import messagebox module for pop-up dialogs

root = tk.Tk()
root.geometry("600x350")
messagebox.showinfo("Title info pop up", "Any info message")
messagebox.showwarning("Title warning message", "Any warning message")
messagebox.showerror("Title error pop up", "Any error message")
root.mainloop()
