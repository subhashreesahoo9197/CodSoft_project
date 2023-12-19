# Import the required packages to be used in the calculator
from tkinter import *
import math
import parser  # Import the parser module to fix the missing import

# here is a global variable for inputting any value
i = 0

# Create the main application window
root = Tk()
root.title('CodSoft Calculator')

# Create an input field (Entry widget)
display = Entry(root)
display.grid(row=0, column=0, columnspan=6, padx=10, pady=8, ipadx=8, ipady=8)

# Code to add buttons to the Calculator
Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0, sticky=N + S + E + W)
Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1, sticky=N + S + E + W)
Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2, sticky=N + S + E + W)

Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0, sticky=N + S + E + W)
Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1, sticky=N + S + E + W)
Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2, sticky=N + S + E + W)

Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0, sticky=N + S + E + W)
Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1, sticky=N + S + E + W)
Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2, sticky=N + S + E + W)

# Adding the operations to the calculator
Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0, sticky=N + S + E + W)
Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1, sticky=N + S + E + W)
Button(root, text=".", command=lambda: get_variables(".")).grid(row=5, column=2, sticky=N + S + E + W)

Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3, sticky=N + S + E + W)
Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3, sticky=N + S + E + W)
Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3, sticky=N + S + E + W)
Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3, sticky=N + S + E + W)

Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4, sticky=N + S + E + W)
Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4, sticky=N + S + E + W)
Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4, sticky=N + S + E + W)
Button(root, text="exp", command=lambda: get_operation("**")).grid(row=5, column=4, sticky=N + S + E + W)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5, sticky=N + S + E + W)
Button(root, text="x!", command=lambda: fact()).grid(row=3, column=5, sticky=N + S + E + W)
Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5, sticky=N + S + E + W)
Button(root, text="^2", command=lambda: get_operation("**2")).grid(row=5, column=5, sticky=N + S + E + W)
Button(root, text="=", command=lambda: calculate()).grid(columnspan=6, sticky=N + S + E + W)

# Function to give the numeric value to the calculator
def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

# Function to get operation from the keyboard
def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

# Delete all values from the display section
def clear_all():
    display.delete(0, END)

# Function which does the undo task
def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "Error")

# Function which does the calculation part
def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Function which defines the fractional part
def fact():
    entire_string = display.get()
    try:
        result = math.factorial(int(entire_string))
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")

# Calling the main function to perform all the tasks
root.mainloop()
