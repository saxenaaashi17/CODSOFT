import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning(
                "Password Length",
                "Please enter a length of at least 4."
            )
            return

        characters = string.ascii_letters + string.digits

        if symbols_var.get():
            characters += string.punctuation

        password = [
            secrets.choice(string.ascii_lowercase),
            secrets.choice(string.ascii_uppercase),
            secrets.choice(string.digits)
        ]

        if symbols_var.get():
            password.append(secrets.choice(string.punctuation))

        remaining_length = length - len(password)

        password += [secrets.choice(characters) for _ in range(remaining_length)]
        secrets.SystemRandom().shuffle(password)

        password_text.set("".join(password))

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number for password length."
        )

def copy_password():
    password = password_text.get()

    if password == "":
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(password)
    window.update()

    messagebox.showinfo(
        "Copied",
        "Password copied to clipboard."
    )

window = tk.Tk()
window.title("Password Generator")
window.geometry("500x420")
window.configure(bg="#f4f6fb")

password_text = tk.StringVar()
symbols_var = tk.BooleanVar(value=True)

title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Arial", 22, "bold"),
    bg="#f4f6fb",
    fg="#2d3a8c"
)
title_label.pack(pady=25)

instruction_label = tk.Label(
    window,
    text="Enter password length:",
    font=("Arial", 13),
    bg="#f4f6fb"
)
instruction_label.pack()

length_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=12,
    justify="center",
    bd=2,
    relief="groove"
)
length_entry.pack(pady=8)
length_entry.insert(0, "12")

symbols_checkbutton = tk.Checkbutton(
    window,
    text="Include symbols (!, @, #, etc.)",
    variable=symbols_var,
    font=("Arial", 12),
    bg="#f4f6fb"
)
symbols_checkbutton.pack(pady=5)

generate_button = tk.Button(
    window,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#2d3a8c",
    fg="white",
    width=20,
    command=generate_password
)
generate_button.pack(pady=15)

password_entry = tk.Entry(
    window,
    textvariable=password_text,
    font=("Arial", 15, "bold"),
    width=30,
    justify="center",
    bd=2,
    relief="groove",
    state="readonly",
    readonlybackground="white"
)
password_entry.pack(pady=8)

copy_button = tk.Button(
    window,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#4caf50",
    fg="white",
    width=18,
    command=copy_password
)
copy_button.pack(pady=15)

window.mainloop()