from tkinter import *
from tkinter import messagebox
import os

contacts = []
FILE_NAME = "contacts.txt"

# ---------------- File Functions ----------------
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")
                if len(data) == 4:
                    contacts.append(data)

    show_all()


def save_contacts():
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write("|".join(contact) + "\n")


# ---------------- Functions ----------------
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts.append([name, phone, email, address])
    save_contacts()
    show_all()
    clear_entries()


def show_all():
    contact_list.delete(0, END)
    for contact in contacts:
        contact_list.insert(END, f"{contact[0]} - {contact[1]}")


def search_contact():
    search = search_entry.get().lower()

    contact_list.delete(0, END)

    for contact in contacts:
        if search in contact[0].lower() or search in contact[1]:
            contact_list.insert(END, f"{contact[0]} - {contact[1]}")


def delete_contact():
    try:
        index = contact_list.curselection()[0]
        del contacts[index]
        save_contacts()
        show_all()

    except IndexError:
        messagebox.showwarning("Warning", "Select a contact first!")


def edit_contact():
    try:
        index = contact_list.curselection()[0]

        contacts[index] = [
            name_entry.get().strip(),
            phone_entry.get().strip(),
            email_entry.get().strip(),
            address_entry.get().strip()
        ]

        save_contacts()
        show_all()
        clear_entries()

    except IndexError:
        messagebox.showwarning("Warning", "Select a contact first!")


def load_selected(event):
    try:
        index = contact_list.curselection()[0]
        contact = contacts[index]

        clear_entries()

        name_entry.insert(0, contact[0])
        phone_entry.insert(0, contact[1])
        email_entry.insert(0, contact[2])
        address_entry.insert(0, contact[3])

    except IndexError:
        pass


def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)


# ---------------- GUI ----------------
root = Tk()
root.title("Contact Book")
root.geometry("500x620")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

Label(root,
      text="Contact Book",
      font=("Arial",20,"bold"),
      bg="#f5f5f5").pack(pady=10)

Label(root,text="Name",bg="#f5f5f5").pack()
name_entry = Entry(root,width=40)
name_entry.pack()

Label(root,text="Phone",bg="#f5f5f5").pack()
phone_entry = Entry(root,width=40)
phone_entry.pack()

Label(root,text="Email",bg="#f5f5f5").pack()
email_entry = Entry(root,width=40)
email_entry.pack()

Label(root,text="Address",bg="#f5f5f5").pack()
address_entry = Entry(root,width=40)
address_entry.pack()

Button(root,
       text="Add Contact",
       width=18,
       bg="#4CAF50",
       fg="white",
       command=add_contact).pack(pady=5)

Button(root,
       text="Update Contact",
       width=18,
       bg="#2196F3",
       fg="white",
       command=edit_contact).pack(pady=5)

search_entry = Entry(root,width=40)
search_entry.pack(pady=5)

Button(root,
       text="Search",
       width=15,
       command=search_contact).pack()

Button(root,
       text="Show All",
       width=15,
       command=show_all).pack(pady=5)

contact_list = Listbox(root,width=55,height=14)
contact_list.pack(pady=10)

contact_list.bind("<Double-Button-1>", load_selected)

Button(root,
       text="Delete Selected",
       width=20,
       bg="red",
       fg="white",
       command=delete_contact).pack(pady=5)

load_contacts()

root.mainloop()