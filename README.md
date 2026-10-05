# Python Console Calculator

A simple, user-friendly Python console calculator that performs basic arithmetic operations with comprehensive error handling.

## Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Input Validation**: Validates that inputs are valid numbers
- **Error Handling**:
  - Non-numeric input detection
  - Division by zero prevention
  - Unsupported operation detection
- **User-Friendly Interface**: Clear prompts and formatted output

## Requirements

- Python 3.x

## Usage

Run the calculator from the command line:

```bash
python3 calculator.py
```

### Example Session

```
=== Python Console Calculator ===

Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, *, /): +

Result: 10.0 + 5.0 = 15.0
```

## Error Handling Examples

### Division by Zero
```
Enter the first number: 10
Enter the second number: 0
Choose an operation (+, -, *, /): /

Error: Division by zero is not allowed
```

### Non-Numeric Input
```
Enter the first number: abc

Error: 'abc' is not a valid number
```

### Unsupported Operation
```
Enter the first number: 10
Enter the second number: 5
Choose an operation (+, -, *, /): %

Error: '%' is not a supported operation. Use +, -, *, or /
```

## Code Structure

The calculator is organized with the following functions:

- `add(a, b)` - Addition operation
- `subtract(a, b)` - Subtraction operation
- `multiply(a, b)` - Multiplication operation
- `divide(a, b)` - Division operation with zero check
- `validate_number(value)` - Validates numeric input
- `validate_operation(operation)` - Validates supported operation
- `main()` - Main calculator logic and user interaction

## Author

Created as part of Issue #1 implementation
