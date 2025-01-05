from tkinter import *

def press(key):
    current_text = entry_text.get()
    entry_text.set(current_text + str(key))

def calculate():
    try:
        result = eval(entry_text.get())
        entry_text.set(str(result))
    except:
        entry_text.set("Error")

def clear():
    entry_text.set("")

root = Tk()
root.title("SIMPLE CALCULATOR")


entry_text = StringVar()
entry = Entry(root, textvariable=entry_text, font=('arial', 18), bd=5, relief=RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0


for button in buttons:
    if button == "=":
        Button(root, text=button, font=('arial', 18), bd=2, bg="lightblue", 
               command=calculate).grid(row=row_val, column=col_val, ipadx=20, ipady=10, padx=5, pady=5)
    elif button == "C":
        Button(root, text=button, font=('arial', 18), bd=2, bg="lightcoral", 
               command=clear).grid(row=row_val, column=col_val, ipadx=20, ipady=10, padx=5, pady=5)
    elif button in "+-*/":
        Button(root, text=button, font=('arial', 18), bd=2, bg="lightgray", 
               command=lambda b=button: press(b)).grid(row=row_val, column=col_val, ipadx=20, ipady=10, padx=5, pady=5)
    else:
        Button(root, text=button, font=('arial', 18), bd=2, 
               command=lambda b=button: press(b)).grid(row=row_val, column=col_val, ipadx=20, ipady=10, padx=5, pady=5)

  
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


root.mainloop()
