import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone:
        contacts.append((name, phone, email))
        refresh_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showwarning("Error", "Name and Phone are required!")

def refresh_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact[0]}: {contact[1]} ({contact[2]})")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contacts.pop(selected[0])
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showwarning("Error", "No contact selected!")

def update_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        if name and phone:
            contacts[index] = (name, phone, email)
            refresh_contact_list()
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showwarning("Error", "Name and Phone are required!")
    else:
        messagebox.showwarning("Error", "No contact selected!")

root = tk.Tk()
root.title("Simple Contact Manager")
root.geometry("400x400")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack(pady=5)

tk.Label(root, text="Email:").pack(pady=5)
email_entry = tk.Entry(root)
email_entry.pack(pady=5)

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Contact Details:").pack(pady=3)
contact_list = tk.Listbox(root)
contact_list.pack(pady=3, fill=tk.BOTH, expand=True)



root.mainloop()

