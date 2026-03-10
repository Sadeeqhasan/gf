# Simple Calculator

A simple command-line calculator written in Python that supports basic arithmetic operations.

## Features

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)
- Error handling for division by zero and invalid input

## Usage

Run the calculator interactively:

```bash
python calculator.py
```

Then enter expressions in the format `number operator number`:

```
Enter expression (e.g. 2 + 3): 10 + 5
Result: 15.0
Enter expression (e.g. 2 + 3): 8 / 2
Result: 4.0
Enter expression (e.g. 2 + 3): quit
Goodbye!
```

You can also import and use the functions directly:

```python
from calculator import add, subtract, multiply, divide, calculate

add(2, 3)          # 5
subtract(10, 4)    # 6
multiply(3, 7)     # 21
divide(15, 3)      # 5.0
calculate(2, "+", 3)  # 5
```

## Running Tests

```bash
python -m pytest test_calculator.py -v
```