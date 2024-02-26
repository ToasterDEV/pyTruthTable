# Truth Table Generator

This program is a graphical user interface (GUI) application that generates truth tables for logical expressions and verifies their logical equivalences. It is built using the `customtkinter` library for the GUI components and utilizes several other libraries for processing the logical expressions and generating the tables.

## Features

- Generate truth tables for single logical expressions.
- Check logical equivalence between two logical expressions.
- User-friendly GUI with clear instructions and input validation.

## Requirements

- Python 3.x
- Libraries: `customtkinter`, `CTkTable`, `itertools`, `tabulate`, `re`

## Usage

1. Run the program.
2. Enter a logical expression in the input field. Use the following symbols for logical operators:
   - `^` for AND
   - `v` for OR
   - `-` for NOT
   - `x` for XOR
   - `/` for implication
   - `|` for biconditional
   - `,` for checking equivalence between two expressions
3. Click the "Generate" button to generate the truth table.
4. If you entered two expressions separated by a comma, the program will also check if they are logically equivalent and display the result.

## Code Explanation

1. **Imports:**
   - `customtkinter` for the GUI elements.
   - `CTkTable` for creating tables in CustomTkinter.
   - `product` from `itertools` for generating all combinations of truth values.
   - `tabulate` for formatting the truth tables.
   - `re` for working with regular expressions.

2. **Setting Appearance:**
   - `set_appearance_mode("grey")` sets the theme of the GUI to grey.

3. **Function Definitions:**
   - `verificar_entrada(entrada)`: Checks if the input is a valid logical expression using a regular expression.
   - `generate_table()`: Main function that generates the truth table based on the user's input. It handles both single expressions and comparisons between two expressions for logical equivalence.

4. **GUI Layout:**
   - The GUI is divided into several frames: `title_frame`, `specs_frame`, `input_frame`, and `output_frame`.
   - `title_frame` contains the title label.
   - `specs_frame` displays a table showing the symbols used in logical expressions and their meanings.
   - `input_frame` contains the input field where the user enters the logical expression and a button to generate the truth table.
   - `output_frame` contains a textbox where the generated truth table and the result of the logical equivalence check (if applicable) are displayed.

5. **Main GUI Loop:**
   - `app.mainloop()` starts the GUI application.

## Example

Input: `a^b`
Output:
```
Table of Truth
+-----+-----+-------+
|   a |   b | a ^ b |
+-----+-----+-------+
| True|True |  True |
| True|False| False |
|False|True | False |
|False|False| False |
+-----+-----+-------+
```

Input: `a^b,a|b`
Output:
```
Table of Truth
+-------+-------+
| a ^ b | a | b |
+-------+-------+
|  True |  True |
| False |  True |
| False |  True |
| False | False |
+-------+-------+

The expressions are not logically equivalent.
```