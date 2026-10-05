def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def validate_number(value):
    value = value.strip()
    if not value:
        raise ValueError("Input cannot be empty")
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"'{value}' is not a valid number")


def validate_operation(operation):
    operation = operation.strip()
    if not operation:
        raise ValueError("Operation cannot be empty")
    valid_operations = ['+', '-', '*', '/']
    if operation not in valid_operations:
        raise ValueError(f"'{operation}' is not a supported operation. Use +, -, *, or /")
    return operation


def main():
    print("=== Python Console Calculator ===\n")

    try:
        num1_input = input("Enter the first number: ")
        num1 = validate_number(num1_input)

        num2_input = input("Enter the second number: ")
        num2 = validate_number(num2_input)

        operation = input("Choose an operation (+, -, *, /): ")
        operation = validate_operation(operation)

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"\nResult: {num1} {operation} {num2} = {result}\n")

    except ValueError as e:
        print(f"\nError: {e}\n")
    except KeyboardInterrupt:
        print("\n\nCalculation cancelled.\n")


if __name__ == "__main__":
    main()
