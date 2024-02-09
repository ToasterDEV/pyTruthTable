# pyTruthTable - Truth Table Generator

This Python script utilizes the `customtkinter` library to provide a graphical user interface for generating truth tables based on logical expressions input by the user. It supports basic logical operations and variables.

## Dependencies

- `customtkinter`: A library that enhances Tkinter widgets with a more modern and customizable look.
- `itertools`: A standard Python module for efficient looping and is used here for generating product combinations to create truth tables.

To install `customtkinter`, run:

```bash
pip install customtkinter
```

## Setup and Execution

Ensure you have Python installed on your system along with the required `customtkinter` library. Save the script to a file, for example, `truth_table_generator.py`, and run it using Python:

```bash
python truth_table_generator.py
```

## Features

- **Dark Mode Interface:** The application uses a dark appearance mode for reduced eye strain and improved readability.
- **Logical Expression Input:** Users can input logical expressions using variables (`p`, `q`, `r`, `s`) and operators (`~`, `∧`, `∨`, `→`, `↔`, `⊕`).
- **Truth Table Generation:** Upon pressing the `=` button, the application generates and prints the truth table for the given expression in the console.
- **Editing Functions:** Users can clear the entire input or delete the last character using the `AC` and `DEL` buttons, respectively.

## Usage

1. **Start the Application:** Launch the script to open the GUI.
2. **Enter Logical Expression:** Use the buttons on the interface to input your logical expression. Each button press adds a corresponding character to the input field.
3. **Generate Truth Table:** Press the `=` button to generate the truth table. The variables and their truth values will be printed in the console.
4. **Edit or Clear Input:** Use the `AC` button to clear the input field or the `DEL` button to remove the last character.

## GUI Components

- **Input Field:** A large entry where the logical expression is displayed.
- **Buttons:** For inputting variables, operators, and controlling the display (clear and delete).
- **Truth Table Output:** Upon pressing the `=` button, the truth table is generated and printed to the console, not in the GUI itself.