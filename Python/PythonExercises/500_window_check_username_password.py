import tkinter as tk
import re

BACKGROUND_COLOR = "orange"


def check_password_strength(any_password):
    message = []
    if not any_password:
        return ["Password cannot be empty!"]
    if len(any_password) < 8:
        message.append("Password must be at least 8 characters long")
    if not re.search(r"[A-Z]", any_password):
        message.append("Password must contain at least one uppercase letter")
    if not re.search(r"[a-z]", any_password):
        message.append("Password must contain at least one lowercase letter")
    if not re.search(r"\d", any_password):
        message.append("Password must contain at least one digit")
    if not re.search(r"[!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~]", any_password):
        message.append(
            "Password must contain at least one special character (!\"#$%&'()*+,\-./:;<=>?@\[\]^_`{|}~)"
        )
    if not message:
        message.append("Your password is strong!")
    return message


def check_username(any_username):
    if not any_username:
        return "Username cannot be empty"
    if any_username.isalnum():
        return f"Your username '{any_username}' is valid"
    else:
        return "Your username must contain only letters and digits"


def show_result_of_check():
    user_name = username.get().strip()
    user_password = password.get().strip()
    password_check = "\n".join(check_password_strength(user_password))

    # Create a new window to display results
    result_window = tk.Toplevel(root)
    result_window.title("Result")
    result_window.geometry("800x200")

    # Display result
    tk.Label(result_window, text=f"{check_username(user_name)}\n{password_check}").pack(
        pady=5
    )


def close_app():
    root.destroy()


# Create the MAIN WINDOW
root = tk.Tk()
root.title("Check username and password")
root.configure(bg=BACKGROUND_COLOR)
root.option_add("*Font", "Arial 14")

tk.Label(root, text="Enter a username: ").pack(pady=5, padx=20)
username = tk.Entry(root)
username.pack(pady=5, padx=20)
tk.Label(root, text="Enter a password: ").pack(pady=5, padx=20)
password = tk.Entry(root)
password.pack(pady=5, padx=20)


# Button to calculate total and average scores
tk.Button(root, text="Check", command=show_result_of_check).pack(pady=10)

# Close button
tk.Button(root, text="Close", command=close_app).pack(pady=10)

# Run the application
root.mainloop()
