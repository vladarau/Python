def expr(): # calculating expression
    a = item()
    global index
    global curlex
    while (index < len(curlex) and(curlex[index] == "+" or curlex[index] == "-")):
        index += 1
        if (curlex[index - 1] == "+"):
            a += item()
        else:
            a -= item()
    return a

def item(): #calculating summand
    a = mult()
    global index
    global curlex
    while (index < len(curlex) and (curlex[index] == "*" or curlex[index] == "/")):
        index += 1
        if (curlex[index - 1] == "*"):
            a *= mult()
        else:
            denominator = mult()
            try:
                a /= denominator
            except ZeroDivisionError:
                print("Division by zero!")
                exit(0)
    return a

def mult(): #calculating multiplier
    a = 0
    global index
    global curlex
    if (curlex[index] == "("): #calculating expression in the brackets
        index += 1
        a = expr()
        if index >= len(curlex) or curlex[index] != ")":
            print("Expression doesn't have a close bracket!")
            exit(0)
        index += 1
    else:
        if (curlex[index] == "-"): # checking for negative multipliers
            index += 1
            a = (-1) * mult()
        else:
            number = "" #extracting a number from expression adding a dor if it is a float number
            if curlex[index] == ".":
                print("Number must start with a digit!")
                exit(0)
            while (index < len(curlex) and ((curlex[index] >= "0" and curlex[index] <= "9") or curlex[index] == ".")):
                number += curlex[index]
                index += 1
            try:
                a = float(number)
            except ValueError:
                print("Incorrect number!")
                exit(0)
    return a

while True:
     try:
        expression = input()
     except EOFError:
         exit(0)
     curlex = expression.replace(" ", "")
     index = 0
     print(expr())