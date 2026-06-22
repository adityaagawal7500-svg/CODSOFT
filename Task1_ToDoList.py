from tkinter import *
from tkinter import messagebox
import os

# ---------------- Main Window ----------------
root = Tk()
root.title("To-Do List")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

tasks = []
FILE_NAME = "tasks.txt"


# ---------------- File Functions ----------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for task in file.readlines():
                task = task.strip()
                if task:
                    tasks.append(task)
                    task_listbox.insert(END, task)


def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# ---------------- Functions ----------------
def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    tasks.append(task)
    task_listbox.insert(END, task)
    task_entry.delete(0, END)
    save_tasks()


def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        tasks.pop(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


def edit_task():
    try:
        selected = task_listbox.curselection()[0]
        new_task = task_entry.get().strip()

        if new_task == "":
            messagebox.showwarning("Warning", "Enter updated task.")
            return

        tasks[selected] = new_task
        task_listbox.delete(selected)
        task_listbox.insert(selected, new_task)

        task_entry.delete(0, END)
        save_tasks()

    except IndexError:
        messagebox.showwarning("Warning", "Please select a task.")


def clear_tasks():
    if len(tasks) == 0:
        return

    answer = messagebox.askyesno("Confirm", "Delete all tasks?")

    if answer:
        task_listbox.delete(0, END)
        tasks.clear()
        save_tasks()


# ---------------- Heading ----------------
title = Label(
    root,
    text="My To-Do List",
    font=("Arial", 20, "bold"),
    bg="#f4f4f4",
    fg="#333333"
)
title.pack(pady=15)


# ---------------- Entry ----------------
task_entry = Entry(
    root,
    width=35,
    font=("Arial", 14)
)

task_entry.pack(pady=10)
task_entry.bind("<Return>", lambda event: add_task())


# ---------------- Buttons ----------------
button_frame = Frame(root, bg="#f4f4f4")
button_frame.pack()

Button(
    button_frame,
    text="Add",
    width=10,
    bg="#4CAF50",
    fg="white",
    command=add_task
).grid(row=0, column=0, padx=5)

Button(
    button_frame,
    text="Edit",
    width=10,
    bg="#2196F3",
    fg="white",
    command=edit_task
).grid(row=0, column=1, padx=5)

Button(
    button_frame,
    text="Delete",
    width=10,
    bg="#f44336",
    fg="white",
    command=delete_task
).grid(row=0, column=2, padx=5)

Button(
    button_frame,
    text="Clear All",
    width=10,
    bg="#ff9800",
    fg="white",
    command=clear_tasks
).grid(row=0, column=3, padx=5)


# ---------------- Listbox ----------------
frame = Frame(root)
frame.pack(pady=20)

scrollbar = Scrollbar(frame)

task_listbox = Listbox(
    frame,
    width=45,
    height=15,
    font=("Arial", 12),
    yscrollcommand=scrollbar.set
)

scrollbar.config(command=task_listbox.yview)

scrollbar.pack(side=RIGHT, fill=Y)
task_listbox.pack(side=LEFT)


# ---------------- Footer ----------------
Label(
    root,
    text="CodSoft Python Internship Project",
    font=("Arial", 10),
    bg="#f4f4f4",
    fg="gray"
).pack(pady=10)


# ---------------- Load Existing Tasks ----------------
load_tasks()

root.mainloop()