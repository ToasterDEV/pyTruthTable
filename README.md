# Truth Table Generator

This program generates truth tables and verifies logical equivalences for logical expressions using the `customtkinter` library for the graphical user interface and the `ttg` library for generating truth tables.

## Dependencies

- `customtkinter`: Used for creating the graphical user interface.
- `CTkTable`: Used for creating tables in CustomTkinter.
- `itertools`: Used for generating product combinations of truth values.
- `tabulate`: Used for formatting the truth tables in a tabular format.
- `re`: Used for working with regular expressions.
- `ttg`: Used for generating truth tables (Teorías y Teoremas Gráficos).

## Functions

### `verificar_entrada(entrada)`

Verifies if an expression input is a valid expression. Currently checks for lowercase letters and specified symbols.

**Parameters:**

- `entrada`: The expression input to be verified.

**Returns:** `bool` indicating whether the expression is valid.

### `final_result(variables, expression2)`

Generates and prints the truth table for the given variables and expression.

**Parameters:**

- `variables`: List of variables in the expression.
- `expression2`: The expression with operators replaced by their Python equivalents.

### `generate_table()`

Main function that handles the generation of the truth table based on the user input. It processes the input expression, replaces operators with their Python equivalents, and generates the truth table using the `Truths` class from the `ttg` library.

## Main GUI Components

- **Title Frame:** Displays the title of the application.
- **Specifications Frame:** Displays the table of symbols and their meanings.
- **Input Frame:** Contains the input field for the logical expression and the generate button.
- **Output Frame:** Displays the generated truth table and the result of logical equivalence verification.

## Usage

1. Run the program.
2. Enter a logical expression in the input field. Use lowercase letters for variables and the following symbols for operators:
   - `^`: AND
   - `v`: OR
   - `-`: NOT
   - `x`: XOR
   - `/`: Implication
   - `|`: Biconditional
   - `,`: Equivalence (separate two expressions with a comma for equivalence checking)
3. Click the "Generate" button to generate the truth table and verify logical equivalence if applicable.