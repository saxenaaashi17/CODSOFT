import tkinter as tk
from tkinter import messagebox

contacts = []


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def refresh_contact_list(contact_data=None):
    contact_listbox.delete(0, tk.END)

    data_to_show = contacts if contact_data is None else contact_data

    for contact in data_to_show:
        contact_listbox.insert(
            tk.END,
            f"{contact['name']}  |  {contact['phone']}"
        )


def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Missing Details",
            "Name and phone number are required."
        )
        return

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })

    clear_fields()
    refresh_contact_list()
    messagebox.showinfo("Success", "Contact added successfully.")


def get_selected_index():
    selected = contact_listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "No Selection",
            "Please select a contact first."
        )
        return None

    selected_text = contact_listbox.get(selected[0])
    selected_name = selected_text.split("  |  ")[0]

    for index, contact in enumerate(contacts):
        if contact["name"] == selected_name:
            return index

    return None


def view_contact():
    index = get_selected_index()

    if index is None:
        return

    contact = contacts[index]

    messagebox.showinfo(
        "Contact Details",
        f"Name: {contact['name']}\n"
        f"Phone: {contact['phone']}\n"
        f"Email: {contact['email']}\n"
        f"Address: {contact['address']}"
    )


def update_contact():
    index = get_selected_index()

    if index is None:
        return

    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning(
            "Missing Details",
            "Enter at least name and phone number before updating."
        )
        return

    contacts[index] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    clear_fields()
    refresh_contact_list()
    messagebox.showinfo("Updated", "Contact updated successfully.")


def delete_contact():
    index = get_selected_index()

    if index is None:
        return

    confirm = messagebox.askyesno(
        "Delete Contact",
        "Are you sure you want to delete this contact?"
    )

    if confirm:
        del contacts[index]
        refresh_contact_list()
        clear_fields()
        messagebox.showinfo("Deleted", "Contact deleted successfully.")


def search_contact():
    search_text = search_entry.get().strip().lower()

    if search_text == "":
        refresh_contact_list()
        return

    filtered_contacts = []

    for contact in contacts:
        if (
            search_text in contact["name"].lower()
            or search_text in contact["phone"].lower()
        ):
            filtered_contacts.append(contact)

    refresh_contact_list(filtered_contacts)


def load_selected_contact(event):
    selected = contact_listbox.curselection()

    if not selected:
        return

    selected_text = contact_listbox.get(selected[0])
    selected_name = selected_text.split("  |  ")[0]

    for contact in contacts:
        if contact["name"] == selected_name:
            clear_fields()

            name_entry.insert(0, contact["name"])
            phone_entry.insert(0, contact["phone"])
            email_entry.insert(0, contact["email"])
            address_entry.insert(0, contact["address"])
            break


window = tk.Tk()
window.title("Contact Book")
window.geometry("650x650")
window.configure(bg="#f4f6fb")

title_label = tk.Label(
    window,
    text="Contact Book",
    font=("Arial", 24, "bold"),
    bg="#f4f6fb",
    fg="#2d3a8c"
)
title_label.pack(pady=18)

form_frame = tk.Frame(window, bg="#f4f6fb")
form_frame.pack(pady=5)

tk.Label(form_frame, text="Name:", font=("Arial", 12), bg="#f4f6fb").grid(
    row=0, column=0, padx=8, pady=7, sticky="e"
)
name_entry = tk.Entry(form_frame, font=("Arial", 12), width=35)
name_entry.grid(row=0, column=1, padx=8, pady=7)

tk.Label(form_frame, text="Phone:", font=("Arial", 12), bg="#f4f6fb").grid(
    row=1, column=0, padx=8, pady=7, sticky="e"
)
phone_entry = tk.Entry(form_frame, font=("Arial", 12), width=35)
phone_entry.grid(row=1, column=1, padx=8, pady=7)

tk.Label(form_frame, text="Email:", font=("Arial", 12), bg="#f4f6fb").grid(
    row=2, column=0, padx=8, pady=7, sticky="e"
)
email_entry = tk.Entry(form_frame, font=("Arial", 12), width=35)
email_entry.grid(row=2, column=1, padx=8, pady=7)

tk.Label(form_frame, text="Address:", font=("Arial", 12), bg="#f4f6fb").grid(
    row=3, column=0, padx=8, pady=7, sticky="e"
)
address_entry = tk.Entry(form_frame, font=("Arial", 12), width=35)
address_entry.grid(row=3, column=1, padx=8, pady=7)

action_frame = tk.Frame(window, bg="#f4f6fb")
action_frame.pack(pady=10)

tk.Button(
    action_frame, text="Add Contact", font=("Arial", 11, "bold"),
    bg="#2d3a8c", fg="white", width=14, command=add_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    action_frame, text="Update", font=("Arial", 11, "bold"),
    bg="#4caf50", fg="white", width=12, command=update_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    action_frame, text="Delete", font=("Arial", 11, "bold"),
    bg="#e74c3c", fg="white", width=12, command=delete_contact
).grid(row=0, column=2, padx=5)

tk.Button(
    action_frame, text="View Details", font=("Arial", 11, "bold"),
    bg="#555555", fg="white", width=14, command=view_contact
).grid(row=0, column=3, padx=5)

search_frame = tk.Frame(window, bg="#f4f6fb")
search_frame.pack(pady=8)

tk.Label(
    search_frame, text="Search by name or phone:",
    font=("Arial", 12), bg="#f4f6fb"
).grid(row=0, column=0, padx=5)

search_entry = tk.Entry(search_frame, font=("Arial", 12), width=25)
search_entry.grid(row=0, column=1, padx=5)

tk.Button(
    search_frame, text="Search", font=("Arial", 10, "bold"),
    bg="#2d3a8c", fg="white", command=search_contact
).grid(row=0, column=2, padx=5)

tk.Button(
    search_frame, text="Show All", font=("Arial", 10, "bold"),
    bg="#777777", fg="white", command=refresh_contact_list
).grid(row=0, column=3, padx=5)

contact_listbox = tk.Listbox(
    window, font=("Arial", 12), width=62, height=12,
    bd=2, relief="groove", selectbackground="#b9c5ff"
)
contact_listbox.pack(pady=12)
contact_listbox.bind("<<ListboxSelect>>", load_selected_contact)

window.mainloop()