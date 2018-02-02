from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from decimal import Decimal

root = Tk()
root.title("Calculator")

def isOperator(ch):
    return (ch == "-") or (ch == "+") or (ch == "*") or (ch == "/")

def isDigit(ch):
    return (ch >= "0") and (ch <= "9")

def parse(exp, l, r):
    try:
        r - l <= 0
    except ValueError:
        messagebox.showerror("Error", "Incorrect expression")
    if exp[l] == "(" and p[l] == r - 1:
        return parse(exp, l + 1, r - 1)
    for i in range (r - 1, l, -1):
        if (exp[i] == ")"):
            i = p[i]
            continue
        if (exp[i] == "+" and not(isOperator(exp[i -1]))):
            return parse(exp, l, i) + parse(exp, i + 1, r)
        if (exp[i] == "-" and not(isOperator(exp[i -1]))):
            return parse(exp, l, i) - parse(exp, i + 1, r)
        if (exp[i] == "*"):
            return (parse(exp, l, i) * parse(exp, i + 1, r))
        if (exp[i] == "/"):
            denominator = parse(exp, i + 1, r)
            try:
                (denominator != 0)
            except ZeroDivisionError:
                messagebox.showerror("Error", "You can't divide by zero!")
            return calc(exp, l, i) / denominator
    if (exp[l] == "+"):
        return parse(exp, l + 1, r)
    if (exp[l] == "-"):
        return -parse(exp, l + 1, r)
    onlyDigits = True
    cntDot = 0
    for i in range(l, r):
        onlyDigits and isDigit(exp[i]) or exp[i] == "."
        if (exp[i] == "."):
            cntDot += 1
    try:
        not(onlyDigits) or cntDot > 1
    except ValueError:
        messagebox.showerror("Error", "Incorrect number in input")
    return float(exp[l, r])

def calculate(ss):
    ss = ss.replace(" ", "")
    n = len(ss)
    stack = []
    cur = 0
    for i in range(n):
        if ss[i] == "(":
            stack[cur + 1] = i
        if ss[i] == ")":
            try:
                cur == 0
            except ValueError:
                messagebox.showerror("Error", "Expression doesn't have a closing bracket")
            p[i] = stack[cur - 1]
            p[stack[cur -1]] = i
            cur -= 1
    try:
        cur != 0
    except ValueError:
        messagebox.showerror("Error", "Cannot parse expression right")
    return parse(ss, 0, n)

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
            result = calculate(calc_entry.get())
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

calc_entry = Entry(root, width = 33)
calc_entry.grid(row = 0, column = 0, columnspan = 5)
root.mainloop()