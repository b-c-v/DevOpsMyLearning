import tkinter as tk
from tkinter import messagebox  # Import messagebox module for pop-up dialogs

root = tk.Tk()
root.geometry("600x350")
messagebox.askokcancel("Title ask or cancel pop up", "Do you want to cancel?")
messagebox.askquestion("Title ask a question", "Ask any question?")
messagebox.askretrycancel("Title RETRY/CANCEL pop up", "Do you want to try again?")
messagebox.askyesno("Title YES/NO question", "Do you want to do this?")
messagebox.askyesnocancel("Title YES/NO/CANCEl pop up", "Do you want to install app?")
root.mainloop()
