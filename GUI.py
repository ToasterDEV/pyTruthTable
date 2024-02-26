from customtkinter import *    # Importar todas las funciones de customtkinter
from CTkTable import CTkTable  # Importar para crear tablas en CustomTkinter
from itertools import product  # Importar la función product de itertools
from tabulate import tabulate  # Importar la función tabulate de tabulate
import re                      # Para trabajar con expresiones regulares

set_appearance_mode("grey")

app = CTk()


def verificar_entrada(entrada):
    # Función que verifica si una entrada es un número o una letra, y devuelve True o False.
    return bool(re.match("^[a-z^\/\|\(\)]+$", entrada))

def generate_table():
    global output

    # Pedir al usuario que ingrese la expresión
    expression = input.get()

    if not verificar_entrada(expression):
        # Si la entrada no es válida, mostrar mensaje de error
        output.insert("end", f"""ERROR: Enter a valid expression\n(no spaces, lowercase letters, no symbols not specified in the table).""")
        return

    output.delete(0.0, "end")
    table_data = []

    if "," not in expression:
        operators = {
                        "^": " and ",      # "^" and
                        "v": " or ",        # "v" or
                        "-": " not ",       # "-" not
                        "x": "!=",          # "x" xor
                        "|": "==",          # "/" implication
                        "/": "<="           # "|" if and only if
                    }

        # Separar del input las variables y la expresion
        variables = sorted({i for i in expression if i.isalpha() and i != "v" and i != "x"})
        # Reemplazar el símbolo a letras
        expression2 = expression
        for i in expression:
            if i in operators:
                expression2 = expression2.replace(i, operators[i])
        var = product([True, False], repeat=len(variables))
        for combination in var:
            table = dict(zip(variables, combination))
            result = eval(expression2, table)
            table_data.append([table[var] for var in variables] + [result])
        # Agregando primero las variables y luego la expresión a los encabezados de la tabla
        headers = list(variables) + [expression]

        output.insert("end", "Table of Truth\n")  # Primero inserta la etiqueta
        output.insert("end", tabulate(table_data, headers=headers, tablefmt="simple_grid"))  # Luego inserta la tabla generada

    elif "," in expression:  # Si hay una coma en la expresión (dos expresiones separadas por coma)
        expression = expression.split(",")  # Dividir las dos expresiones

        # Obtener las dos expresiones separadas
        expression_1 = expression[0]
        expression_2 = expression[1]

        operators = {"^": " and ", "v": " or ", "-": " not ", "X": "!=", "|": "==", "/": "<="}  # Definir los operadores lógicos y sus equivalentes en Python
        # Obtener las variables de cada expresión
        variables_1 = {i for i in expression_1 if i.isalpha() and i != "v" and i != "x"}
        variables_2 = {i for i in expression_2 if i.isalpha() and i != "v" and i != "x"}
        # Reemplazar los símbolos de operadores por sus equivalentes en Python para cada expresión
        expression2_1 = expression_1
        expression2_2 = expression_2
        for i in expression_1:
            if i in operators:
                expression2_1 = expression2_1.replace(i, operators[i])
        for i in expression_2:
            if i in operators:
                expression2_2 = expression2_2.replace(i, operators[i])
        # Generar todas las combinaciones posibles de valores de verdad para las variables de ambas expresiones
        var_1 = product([True, False], repeat=len(variables_1))
        var_2 = product([True, False], repeat=len(variables_2))
        # Evaluar ambas expresiones para todas las combinaciones posibles de valores de verdad de las variables
        for combination_1, combination_2 in zip(var_1, var_2):
            table_1 = dict(zip(variables_1, combination_1))  # Crear un diccionario que mapea las variables con sus valores de verdad correspondientes para la primera expresión
            table_2 = dict(zip(variables_2, combination_2))  # Crear un diccionario que mapea las variables con sus valores de verdad correspondientes para la segunda expresión
            result_1 = eval(expression2_1, table_1)  # Evaluar la primera expresión con los valores de verdad actuales
            result_2 = eval(expression2_2, table_2)  # Evaluar la segunda expresión con los valores de verdad actuales
            table_data.append([result_1, result_2])  # Agregar los resultados a la lista de resultados
        # Impresión de tabla de resultados con variables
        headers = [expression_1, expression_2]
        output.insert("end", "Table of Truth\n")  # Primero inserta la etiqueta
        output.insert("end", tabulate(table_data, headers=headers, tablefmt="simple_grid"))  # Inserta el resultado en formato tabulado
        # Comparación de los resultados de las dos expresiones
        if all(x == y for x, y in table_data): # Todas las filas son verdaderas o todas son falsas
            output.insert("end", "\nThe expressions are logically equivalent.")  # Si todos los pares de resultados son iguales, las expresiones son equivalentes lógicamente
        else:
            output.insert("end", "\nThe expressions are not logically equivalent.")  # Si hay al menos un par de resultados diferentes, las expresiones no son equivalentes lógicamente
    else:
        output.insert("end", "Between the expressions add a comma (all without spaces).")


#MAIN OF GUI
app.title("Truth Table")
app.geometry("1000x700")

title_frame = CTkFrame(master=app,width=1000,height=100,fg_color="black")
title_frame.grid_propagate(False)
title_frame.grid(row=0)
specs_frame = CTkFrame(master=app,width=200,height=200,fg_color="black")
specs_frame.grid_propagate(False)
specs_frame.grid(row=1,sticky="w")
input_frame = CTkFrame(master=app,width=800,height=200,fg_color="black")
input_frame.grid_propagate(False)
input_frame.grid(row=1,sticky="e")
output_frame = CTkFrame(master=app,width=1000,height=400,fg_color="black")
output_frame.grid_propagate(False)
output_frame.grid(row=2)

title = CTkLabel(master=title_frame,text="GENERATES TRUTH TABLES AND VERIFIES LOGICAL EQUIVALENCES\nBy FYOverflow && ToasterDEV",font=("console",25,"bold"))
title.place(anchor=CENTER,relx = .5, rely = .45)
input = CTkEntry(master=input_frame,placeholder_text="Enter the logical expression (without spaces)",width=500,height=60,fg_color="#F2F2F2",placeholder_text_color="black",text_color="black")
input.place(anchor=CENTER,relx = .5, rely = .4)
button = CTkButton(master=input_frame,text="Generate",command=generate_table,fg_color="#7F7F7F",text_color="black")
button.place(anchor=CENTER,relx = .5, rely = .62)

values = [["Insert","Value"],
          ["^"," and "],
          ["v"," or "],
          ["-"," not "],
          ["x"," xor"],
          ["/","inplication"],
          ["|","bicondicional"],
          [",","equivalence"]]

table = CTkTable(master=specs_frame, values=values, justify=True,height=24,width=30,border_color="#EF8354",header_color="#7F7F7F",text_color="black",colors=["#CCCCCC", "#A5A5A5"])
table.place(anchor=CENTER, relx=.5,rely=.5)

output = CTkTextbox(master=output_frame,width=1000,height=400, activate_scrollbars=True, font=("Consolas", 20, "bold"))
output.grid()

app.mainloop()