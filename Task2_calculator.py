from tkinter import *
from tkinter import messagebox

# ---------------- Main Window ----------------
root = Tk()
root.title("Calculator")
root.geometry("350x520")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# ---------------- Display ----------------
display = Entry(
    root,
    font=("Arial", 22),
    bd=8,
    relief=RIDGE,
    justify="right",
    bg="white"
)
display.pack(fill=X, padx=10, pady=10)

# ---------------- Functions ----------------
def click(value):
    display.insert(END, value)

def clear():
    display.delete(0, END)

def backspace():
    current = display.get()
    display.delete(0, END)
    display.insert(0, current[:-1])

def calculate():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, END)
        display.insert(END, result)
    except Exception:
        messagebox.showerror("Error", "Invalid Expression")
        display.delete(0, END)

# ---------------- Button Layout ----------------
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

frame = Frame(root, bg="#f5f5f5")
frame.pack()

for row in buttons:
    row_frame = Frame(frame, bg="#f5f5f5")
    row_frame.pack()

    for btn in row:

        if btn == "=":
            color = "#4CAF50"
        elif btn in "+-*/":
            color = "#FF9800"
        else:
            color = "white"

        Button(
            row_frame,
            text=btn,
            font=("Arial", 16, "bold"),
            width=6,
            height=2,
            bg=color,
            command=calculate if btn == "=" else lambda b=btn: click(b)
        ).pack(side=LEFT, padx=3, pady=3)

# ---------------- Bottom Buttons ----------------
bottom = Frame(root, bg="#f5f5f5")
bottom.pack(pady=10)

Button(
    bottom,
    text="⌫ Back",
    font=("Arial", 14),
    width=12,
    bg="#FFC107",
    command=backspace
).grid(row=0, column=0, padx=5)

Button(
    bottom,
    text="Clear",
    font=("Arial", 14),
    width=12,
    bg="#F44336",
    fg="white",
    command=clear
).grid(row=0, column=1, padx=5)

# ---------------- Keyboard Support ----------------
display.bind("<Return>", lambda event: calculate())
display.bind("<Escape>", lambda event: clear())

# ---------------- Footer ----------------
Label(
    root,
    text="Calculator - CodSoft Internship",
    font=("Arial", 10),
    bg="#f5f5f5",
    fg="gray"
).pack(pady=10)

root.mainloop()