#! /usr/bin/env python3
from tkinter import *


# insert text in entry
def set_text(text):
    entry.insert(END,text)
    return

# AC delete
def delete():
    entry.delete(0, END)
    return

# result when = clicked
def result():
    operation = entry.get()
    op_result = calculation(operation)
    entry.delete(0, END)
    entry.insert(END, op_result)
    return

# put number in percent
def percent():
    operation = entry.get()
    entry.delete(0, END)
    op_result = int(operation)/100
    entry.insert(END, op_result)
    return

# reverse 
def inverse():
    operation = entry.get()
    entry.delete(0, END)
    op_result = int(operation)*-1
    entry.insert(END, op_result)
    return

# calculation: finds *, /, -, + and exceutes in order the operations from the given string
def calculation(operation):
    i = 0
    operation_result = operation
    while i < len(operation)-1:
        if operation[i] == "*":
            operation_result = multiply(operation_result)
        if operation[i] == "/":
            operation_result = div(operation_result)
        i += 1

    i = 0
    while i < len(operation)-1:
        if operation[i] == "-":
            operation_result = min_op(operation_result)
        if operation[i] == "+":
            operation_result = add(operation_result)
        i += 1
    return operation_result

#decompose string and multiply
def multiply(operation):
    i = 0 #index
    num1 = "" #number to be multiplied
    num2 = "" #number to be multiplied
    operation1 = "" #first part of string before calculation
    operation2 = "" #second part of string after calculation
    while i < len(operation):
        if operation[i] == "*":
            j = i + 1
            k = i - 1

            #get first and second number to be multiplied
            while operation[j].isdigit() or operation[j]=='.':
                num1 += operation[j] #number 1 to be multiplied
                if j != len(operation)-1:
                    j += 1
                else:
                    break
            while operation[k].isdigit() or operation[k]=='.':
                num2 += operation[k] #number 2 to be multiplied
                if k != 0:
                    k = k - 1 
                else:
                    break     
            num2 = num2[::-1]

            if operation[i] == "*":
                calculation = float(num1) * float(num2) #number 1 x number 2

            #get the part before and after the calculation
            if k == 0:
                operational1 = ""
            else:
                while k >= 0:
                    operation1 += operation[k]
                    k = k - 1 
            if j == len(operation)-1:
                operation2 = ""
            else:
                while j <= len(operation)-1:
                    operation2 += operation[j]
                    j = j + 1
            operation1 = operation1[::-1]
            operation = operation1+str(calculation)+operation2 #creating new operation
            return operation
            return
        else:
            i += 1 
    return
        


def div(operation):
    i = 0 #index
    num1 = "" #number to be divided
    num2 = "" #number to divide
    operation1 = "" #first part of string before calculation
    operation2 = "" #second part of string after calculation
    while i < len(operation):
        if operation[i] == "/":
            j = i + 1
            k = i - 1

            #get first and second number to be divided
            while operation[j].isdigit() or operation[j]=='.':
                num1 += operation[j] #number 1 to be divided
                if j != len(operation)-1:
                    j += 1
                else:
                    break
            while operation[k].isdigit() or operation[k]=='.':
                num2 += operation[k] #number 2 to be divided
                if k != 0:
                    k = k - 1 
                else:
                    break     
            num2 = num2[::-1]

            if operation[i] == "/":
                calculation = float(num2) / float(num1) #number 1 / number 2
                calculation = float(calculation)

            #get the part before and after the calculation
            if k == 0:
                operational1 = ""
            else:
                while k >= 0:
                    operation1 += operation[k]
                    k = k - 1 
            if j == len(operation)-1:
                operation2 = ""
            else:
                while j <= len(operation)-1:
                    operation2 += operation[j]
                    j = j + 1
            operation1 = operation1[::-1]
            operation = operation1+str(calculation)+operation2 #creating new operation
            return operation
            return
        else:
            i += 1 
    return

 

def min_op(operation):
    i = 0 #index
    num1 = "" #number to be substracted
    num2 = "" #number to substract
    operation1 = "" #first part of string before calculation
    operation2 = "" #second part of string after calculation
    while i < len(operation):
        if operation[i] == "-":
            j = i + 1
            k = i - 1

            #get first and second number to be substracted
            while operation[j].isdigit() or operation[j]=='.':
                num1 += operation[j] #number 1 to be substracted
                if j != len(operation)-1:
                    j += 1
                else:
                    break
            while operation[k].isdigit() or operation[k]=='.':
                num2 += operation[k] #number 2 to be substracted
                if k != 0:
                    k = k - 1 
                else:
                    break     
            num2 = num2[::-1]

            if operation[i] == "-":
                calculation = float(num2) - float(num1) #number 1 - number 2
                calculation = float(calculation)

            #get the part before and after the calculation
            if k == 0:
                operational1 = ""
            else:
                while k >= 0:
                    operation1 += operation[k]
                    k = k - 1 
            if j == len(operation)-1:
                operation2 = ""
            else:
                while j <= len(operation)-1:
                    operation2 += operation[j]
                    j = j + 1
            operation1 = operation1[::-1]
            operation = operation1+str(calculation)+operation2 #creating new operation
            return operation
            return
        else:
            i += 1 
    return




def add(operation):
    i = 0 #index
    num1 = "" #number to be added
    num2 = "" #number to be added
    operation1 = "" #first part of string before calculation
    operation2 = "" #second part of string after calculation
    while i < len(operation):
        if operation[i] == "+":
            j = i + 1
            k = i - 1

            #get first and second number to be added
            while operation[j].isdigit() or operation[j]=='.':
                num1 += operation[j] #number 1 to be added
                if j != len(operation)-1:
                    j += 1
                else:
                    break
            while operation[k].isdigit() or operation[k]=='.':
                num2 += operation[k] #number 2 to be added
                if k != 0:
                    k = k - 1 
                else:
                    break     
            num2 = num2[::-1]

            if operation[i] == "+":
                calculation = float(num2) + float(num1) #number 1 + number 2
                calculation = float(calculation)

            #get the part before and after the calculation
            if k == 0:
                operational1 = ""
            else:
                while k >= 0:
                    operation1 += operation[k]
                    k = k - 1 
            if j == len(operation)-1:
                operation2 = ""
            else:
                while j <= len(operation)-1:
                    operation2 += operation[j]
                    j = j + 1
            operation1 = operation1[::-1]
            operation = operation1+str(calculation)+operation2 #creating new operation
            return operation
            return
        else:
            i += 1 
    return

############################ MAKE WINDOW

# create blank window with class TK
window = Tk() 


#resize buttons to window size
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=1)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_rowconfigure(5, weight=1)

# create input in the beginning of the calculator
entry = Entry(window)

#creating button in the window
b1 = Button(window, text="1", command=lambda:set_text("1")) 
b2 = Button(window, text="2", command=lambda:set_text("2")) 
b3 = Button(window, text="3", command=lambda:set_text("3")) 
b4 = Button(window, text="4", command=lambda:set_text("4")) 
b5 = Button(window, text="5", command=lambda:set_text("5")) 
b6 = Button(window, text="6", command=lambda:set_text("6")) 
b7 = Button(window, text="7", command=lambda:set_text("7")) 
b8 = Button(window, text="8", command=lambda:set_text("8")) 
b9 = Button(window, text="9", command=lambda:set_text("9")) 
b0 = Button(window, text="0", command=lambda:set_text("0"))
bac = Button(window, text="AC", command=lambda:delete()) 
binverse = Button(window, text="+/-", command=lambda:inverse())
bpercent = Button(window, text="%", command=lambda:percent())  
bdiv = Button(window, text="/", command=lambda:set_text("/"))
bmulti = Button(window, text="x", command=lambda:set_text("*"))
bminus = Button(window, text="-", command=lambda:set_text("-"))
badd = Button(window, text="+", command=lambda:set_text("+"))
bequal = Button(window, text="=", command=lambda:result())
bcomma = Button(window, text=",", command=lambda:set_text("."))

#place the buttons and entry in the first free spot

entry.grid(row=0, column=1, columnspan = 4, sticky=N+S+E+W)

bac.grid(row=1, column=1, sticky=N+S+E+W)
binverse.grid(row=1, column=2, sticky=N+S+E+W)
bpercent.grid(row=1, column=3, sticky=N+S+E+W)
bdiv.grid(row=1, column=4, sticky=N+S+E+W)

b7.grid(row=2, column=1, sticky=N+S+E+W)
b8.grid(row=2, column=2, sticky=N+S+E+W)
b9.grid(row=2, column=3, sticky=N+S+E+W)
bmulti.grid(row=2, column=4, sticky=N+S+E+W)

b4.grid(row=3, column=1, sticky=N+S+E+W)
b5.grid(row=3, column=2, sticky=N+S+E+W)
b6.grid(row=3, column=3, sticky=N+S+E+W)
bminus.grid(row=3, column=4, sticky=N+S+E+W)

b1.grid(row=4, column=1, sticky=N+S+E+W)
b2.grid(row=4, column=2, sticky=N+S+E+W)
b3.grid(row=4, column=3, sticky=N+S+E+W)
badd.grid(row=4, column=4, sticky=N+S+E+W)

b0.grid(row=5, column=1, columnspan = 2, sticky=N+S+E+W)
bcomma.grid(row=5, column=3, sticky=N+S+E+W)
bequal.grid(row=5, column=4, sticky=N+S+E+W)

#loop that never ends or window will close 
window.mainloop() 