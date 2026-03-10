def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            a = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            try:
                result = divide(a, b)
            except ValueError as e:
                print(f"Error: {e}")
                continue
        else:
            print("Invalid operator. Please use +, -, *, /")
            continue

        print(f"Result: {a} {operator} {b} = {result}")

        again = input("Perform another calculation? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
