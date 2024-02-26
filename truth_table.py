from customtkinter import *
from ttg import Truths

set_appearance_mode("grey")

app = CTk()

app.title("Truth Table")
app.geometry("1000x600")

""" ---------------------------------------- """

def Generate_table():
    global result

    vars = str(variables.get())
    statement = str(expression.get())

    if all(i.isalpha() or i == ',' for i in vars):
        vars = vars.split(',')
        statement = statement.split(',')
        try:
            result = Truths(vars, statement, ints=False).as_prettytable()
        except:
            result = 'Something went wrong'
    output.configure(text=result)

""" ---------------------------------------- """

title = CTkLabel(master=app,text='Generador de tablas de verdad',font=('consolas',30),width=1000,height=50)
title.pack()

main_frame = CTkFrame(master=app)
main_frame.pack()

variables = CTkEntry(master=main_frame, placeholder_text='Ingrese las variables de la expresion, separado por comas> ',width=500,height=60)
variables.pack()

expression = CTkEntry(master=main_frame, placeholder_text='Ingrese la expresion completa, separado por comas> ',width=500,height=60)
expression.pack()

button = CTkButton(master=main_frame, text='Generate', command=lambda:Generate_table())
button.pack()

second_frame = CTkFrame(master=app)
second_frame.pack()

output = CTkLabel(master=second_frame, text='...', bg_color='black', font=('console', 10), width=1000, height=400)
output.pack()

app.mainloop()
