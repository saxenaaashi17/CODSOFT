import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Empty Task", "Please enter a task first.")
        return

    tasks.append({"name": task, "completed": False})
    task_entry.delete(0, tk.END)
    update_task_list()

def update_task_list():
    task_listbox.delete(0, tk.END)

    for index, task in enumerate(tasks):
        status = "✓" if task["completed"] else "○"
        task_listbox.insert(tk.END, f"{status}  {task['name']}")

def mark_completed():
    selected_task = task_listbox.curselection()

    if not selected_task:
        messagebox.showwarning("No Selection", "Please select a task first.")
        return

    index = selected_task[0]
    tasks[index]["completed"] = not tasks[index]["completed"]
    update_task_list()

def delete_task():
    selected_task = task_listbox.curselection()

    if not selected_task:
        messagebox.showwarning("No Selection", "Please select a task first.")
        return

    index = selected_task[0]
    del tasks[index]
    update_task_list()

def clear_all_tasks():
    if not tasks:
        messagebox.showinfo("To-Do List", "There are no tasks to clear.")
        return

    confirm = messagebox.askyesno(
        "Clear All Tasks",
        "Are you sure you want to delete all tasks?"
    )

    if confirm:
        tasks.clear()
        update_task_list()

window = tk.Tk()
window.title("My To-Do List")
window.geometry("500x590")
window.configure(bg="#f4f6fb")

title_label = tk.Label(
    window,
    text="My To-Do List",
    font=("Arial", 22, "bold"),
    bg="#f4f6fb",
    fg="#2d3a8c"
)
title_label.pack(pady=20)

task_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=32,
    bd=2,
    relief="groove"
)
task_entry.pack(pady=8)

add_button = tk.Button(
    window,
    text="Add Task",
    font=("Arial", 12, "bold"),
    bg="#2d3a8c",
    fg="white",
    width=15,
    command=add_task
)
add_button.pack(pady=8)

task_listbox = tk.Listbox(
    window,
    font=("Arial", 13),
    width=43,
    height=13,
    selectbackground="#b9c5ff",
    bd=2,
    relief="groove"
)
task_listbox.pack(pady=12)

button_frame = tk.Frame(window, bg="#f4f6fb")
button_frame.pack(pady=5)

complete_button = tk.Button(
    button_frame,
    text="Mark Complete",
    font=("Arial", 11, "bold"),
    bg="#4caf50",
    fg="white",
    width=15,
    command=mark_completed
)
complete_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    font=("Arial", 11, "bold"),
    bg="#e74c3c",
    fg="white",
    width=15,
    command=delete_task
)
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(
    window,
    text="Clear All Tasks",
    font=("Arial", 11, "bold"),
    bg="#555555",
    fg="white",
    width=20,
    command=clear_all_tasks
)
clear_button.pack(pady=12)

window.mainloop()