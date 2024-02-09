from customtkinter import *
from itertools import product

set_appearance_mode("dark")

app = CTk()

app.title("Truth Table")
app.geometry("400x500")

display = CTkEntry(app,width=400,height=100,font=("Mono", 30),fg_color='grey')
display.pack()

buttons = CTkFrame(app,width=400,height=500)
buttons.pack()

# ---------------Functions---------------

i = 0

def get_letters(n):
    global i
    display.insert(i, n)
    i += 1


def get_opers(operator):
    global i
    opers_len = len(operator)
    display.insert(i, operator)
    i += opers_len

def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:- 1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")

def generate():
    global variables
    inputst = display.get()
    variables = list(set([char for char in inputst if char.isalpha()]))
    if variables:
        truth_table = list(product([True, False], repeat=len(variables)))
        print("Truth Table:")
        print(variables)
        for row in truth_table:
            print(row)
    else:
        print("No variables found")

# ---------------Functions---------------
# ----------------Buttons----------------
# -----------------Row-0-----------------

button = CTkButton(buttons, text='(', command=lambda:get_opers('('), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=0, column=0)
button = CTkButton(buttons, text=')', command=lambda:get_opers(')'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=0, column=1)
button = CTkButton(buttons, text='AC', command=lambda:clear_display(), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=0, column=2)
button = CTkButton(buttons, text='DEL', command=lambda:undo(), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=0, column=3)

# -----------------Row-0-----------------
# -----------------Row-1-----------------

button = CTkButton(buttons, text='~', command=lambda:get_opers('~'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=1, column=0)
button = CTkButton(buttons, text='∧', command=lambda:get_opers('∧'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=1, column=1)
button = CTkButton(buttons, text='∨', command=lambda:get_opers('∨'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=1, column=2)
button = CTkButton(buttons, text='→', command=lambda:get_opers('→'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=1, column=3)

# -----------------Row-1-----------------
# -----------------Row-2-----------------

button = CTkButton(buttons, text='p', command=lambda:get_letters('p'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=2, column=0)
button = CTkButton(buttons, text='q', command=lambda:get_letters('q'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=2, column=1)
button = CTkButton(buttons, text='↔', command=lambda:get_opers('↔'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=2, column=2)
button = CTkButton(buttons, text='⊕', command=lambda:get_opers('⊕'), width=100, height=100, font=("Mono", 50), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=2, column=3)

# -----------------Row-2-----------------
# -----------------Row-3-----------------

button = CTkButton(buttons, text='r', command=lambda:get_letters('r'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=3, column=0)
button = CTkButton(buttons, text='s', command=lambda:get_letters('s'), width=100, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=3, column=1)
button = CTkButton(buttons, text='=', command=lambda:generate(), width=200, height=100, font=("Mono", 30), fg_color="black", hover_color="grey", border_width=1, border_color="grey")
button.grid(row=3, column=2,columnspan=2)

# -----------------Row-2-----------------

# ----------------Buttons----------------




app.mainloop()