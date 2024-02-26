# Truth Table Generator

This is a simple GUI application built with `customtkinter` and `ttg` (Truth Table Generator) libraries to generate truth tables for logical expressions.

## Dependencies

- `customtkinter`: Used for creating the GUI elements with a modern look.
- `ttg`: Used for generating the truth tables based on the given variables and expressions.

## Usage

1. **Set Appearance Mode**: The appearance mode is set to "grey" for the application.
   ```python
   set_appearance_mode("grey")
   ```

2. **Create Main Application Window**:
   ```python
   app = CTk()
   app.title("Truth Table")
   app.geometry("1000x600")
   ```

3. **Generate Truth Table Function**:
   - This function is triggered by the "Generate" button.
   - It takes the variables and expression from the input fields, splits them by commas, and generates the truth table using the `Truths` class from the `ttg` library.
   - If there is an error in the input format or expression, it displays "Something went wrong".
   ```python
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
   ```

4. **GUI Layout**:
   - Title label with "Generador de tablas de verdad".
   - Input fields for variables and expression.
   - "Generate" button to trigger the truth table generation.
   - Output label to display the generated truth table or error message.

5. **Main Event Loop**:
   ```python
   app.mainloop()
   ```

## Example

To generate a truth table for the expression "A and B" with variables "A, B", enter the following:

- Variables: `A, B`
- Expression: `A and B`

Click "Generate" to view the truth table.