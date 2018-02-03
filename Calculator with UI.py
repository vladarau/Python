from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from decimal import Decimal

root = Tk()
root.title("Calculator")

# Calculator logic
def calc(key):
    global memory
    if key == "=":
        # check that expression is correct
        str0 = "-0123456789("
        if calc_entry.get()[0] not in str0:
            calc_entry.delete(0, END)
            #calc_entry.insert(END, "Expression starts incorrectly")
            messagebox.showerror("Error", "Incorrect expression: should start with number or open bracket")

            #calculation
        try:
            ss = calc_entry.get().replace(" ", "")
            result = eval(ss)
            calc_entry.insert(END, "=" + str(result))
        except ValueError:
            calc_entry.delete(0, END)
            #calc_entry.insert(END, "Error!")
            messagebox.showerror("Error", "Incorrect expression")
    #clear all
    elif key == "C":
        calc_entry.delete(0, END)
    # -/+ switch
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

# Adding buttons to calculator
button_list = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "-/+", "=",
    "0", ".", "C", "(", ")"
]

r = 1
c = 0
p = []

for i in button_list:
    rel = ""
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text = i, command = cmd).grid(row = r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 30)
calc_entry.grid(row = 0, column = 0, columnspan = 5)
root.mainloop()