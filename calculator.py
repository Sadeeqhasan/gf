"""A simple calculator that performs basic arithmetic operations."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(a, operator, b):
    """Perform a calculation based on the given operator.

    Args:
        a: First number.
        operator: One of '+', '-', '*', '/'.
        b: Second number.

    Returns:
        The result of the operation.

    Raises:
        ValueError: If the operator is not supported or division by zero.
    """
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in operations:
        raise ValueError(f"Unsupported operator: {operator}. Use +, -, *, /")
    return operations[operator](a, b)


def main():
    """Run the calculator in interactive mode."""
    print("Simple Calculator")
    print("Type 'quit' to exit.\n")

    while True:
        expression = input("Enter expression (e.g. 2 + 3): ").strip()
        if expression.lower() == "quit":
            print("Goodbye!")
            break

        parts = expression.split()
        if len(parts) != 3:
            print("Error: Please enter in the format: number operator number")
            continue

        try:
            a = float(parts[0])
            operator = parts[1]
            b = float(parts[2])
            result = calculate(a, operator, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
