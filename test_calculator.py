"""
Comprehensive pytest unit tests for the Python Console Calculator.

Tests cover:
- All arithmetic operations (add, subtract, multiply, divide)
- Validation functions (validate_number, validate_operation)
- Edge cases (zeros, negatives, floats, large numbers)
- Error cases (division by zero, invalid inputs, empty strings, whitespace)
"""

import pytest
from calculator import (
    add,
    subtract,
    multiply,
    divide,
    validate_number,
    validate_operation,
)


# ============================================================================
# ARITHMETIC OPERATION TESTS
# ============================================================================


class TestAddOperation:
    """Tests for the add() function."""

    def test_add_positive_integers(self):
        """Test adding two positive integers."""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(1, 1) == 2

    def test_add_negative_integers(self):
        """Test adding negative integers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
        assert add(10, -5) == 5

    def test_add_with_zero(self):
        """Test addition with zero."""
        assert add(0, 0) == 0
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(-5, 0) == -5

    def test_add_floats(self):
        """Test adding floating-point numbers."""
        assert add(1.5, 2.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)
        assert add(-1.5, 2.5) == pytest.approx(1.0)

    def test_add_large_numbers(self):
        """Test adding very large numbers."""
        assert add(1000000, 2000000) == 3000000
        assert add(1e10, 2e10) == 3e10

    def test_add_mixed_integers_and_floats(self):
        """Test adding integers and floats together."""
        assert add(5, 2.5) == 7.5
        assert add(10.5, 5) == 15.5


class TestSubtractOperation:
    """Tests for the subtract() function."""

    def test_subtract_positive_integers(self):
        """Test subtracting two positive integers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 1) == 9
        assert subtract(100, 50) == 50

    def test_subtract_resulting_in_negative(self):
        """Test subtraction resulting in negative numbers."""
        assert subtract(3, 5) == -2
        assert subtract(1, 10) == -9

    def test_subtract_with_zero(self):
        """Test subtraction with zero."""
        assert subtract(0, 0) == 0
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5

    def test_subtract_negative_integers(self):
        """Test subtracting negative integers."""
        assert subtract(-5, -3) == -2
        assert subtract(-5, 3) == -8
        assert subtract(5, -3) == 8

    def test_subtract_floats(self):
        """Test subtracting floating-point numbers."""
        assert subtract(5.5, 2.5) == pytest.approx(3.0)
        assert subtract(0.5, 0.3) == pytest.approx(0.2)

    def test_subtract_large_numbers(self):
        """Test subtracting large numbers."""
        assert subtract(1000000, 500000) == 500000


class TestMultiplyOperation:
    """Tests for the multiply() function."""

    def test_multiply_positive_integers(self):
        """Test multiplying two positive integers."""
        assert multiply(3, 4) == 12
        assert multiply(5, 5) == 25
        assert multiply(10, 2) == 20

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        assert multiply(0, 0) == 0
        assert multiply(5, 0) == 0
        assert multiply(0, 100) == 0
        assert multiply(-5, 0) == 0

    def test_multiply_by_one(self):
        """Test multiplication by one (identity)."""
        assert multiply(1, 1) == 1
        assert multiply(5, 1) == 5
        assert multiply(1, 100) == 100

    def test_multiply_negative_integers(self):
        """Test multiplying negative integers."""
        assert multiply(-3, -4) == 12
        assert multiply(-5, 4) == -20
        assert multiply(5, -4) == -20

    def test_multiply_floats(self):
        """Test multiplying floating-point numbers."""
        assert multiply(2.5, 4.0) == 10.0
        assert multiply(0.5, 2.0) == pytest.approx(1.0)
        assert multiply(-1.5, 2.0) == pytest.approx(-3.0)

    def test_multiply_large_numbers(self):
        """Test multiplying large numbers."""
        assert multiply(1000, 1000) == 1000000
        assert multiply(1e6, 2) == 2e6


class TestDivideOperation:
    """Tests for the divide() function."""

    def test_divide_positive_integers(self):
        """Test dividing two positive integers."""
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0
        assert divide(100, 4) == 25.0

    def test_divide_resulting_in_float(self):
        """Test division resulting in fractional values."""
        assert divide(5, 2) == 2.5
        assert divide(1, 2) == 0.5
        assert divide(10, 3) == pytest.approx(3.333333333)

    def test_divide_with_negative_numbers(self):
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0
        assert divide(-1, 2) == -0.5

    def test_divide_with_floats(self):
        """Test dividing floating-point numbers."""
        assert divide(5.0, 2.0) == 2.5
        assert divide(7.5, 2.5) == pytest.approx(3.0)

    def test_divide_zero_numerator(self):
        """Test dividing zero (zero as numerator)."""
        assert divide(0, 5) == 0.0
        assert divide(0, -5) == 0.0

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            divide(10, 0)
        assert "Division by zero is not allowed" in str(exc_info.value)

    def test_divide_by_zero_with_negative_numerator(self):
        """Test division by zero with negative numerator."""
        with pytest.raises(ValueError) as exc_info:
            divide(-10, 0)
        assert "Division by zero is not allowed" in str(exc_info.value)

    def test_divide_by_zero_with_zero_numerator(self):
        """Test 0 / 0 raises ValueError."""
        with pytest.raises(ValueError) as exc_info:
            divide(0, 0)
        assert "Division by zero is not allowed" in str(exc_info.value)

    def test_divide_large_numbers(self):
        """Test dividing large numbers."""
        assert divide(1000000, 1000) == 1000.0
        assert divide(1e10, 2) == 5e9

    def test_divide_by_one(self):
        """Test dividing by one (identity)."""
        assert divide(5, 1) == 5.0
        assert divide(-5, 1) == -5.0


# ============================================================================
# VALIDATION FUNCTION TESTS
# ============================================================================


class TestValidateNumber:
    """Tests for the validate_number() function."""

    def test_validate_integer_string(self):
        """Test validating integer strings."""
        assert validate_number("5") == 5.0
        assert validate_number("42") == 42.0
        assert validate_number("0") == 0.0

    def test_validate_negative_number(self):
        """Test validating negative number strings."""
        assert validate_number("-5") == -5.0
        assert validate_number("-42.5") == -42.5

    def test_validate_float_string(self):
        """Test validating floating-point number strings."""
        assert validate_number("3.14") == 3.14
        assert validate_number("0.5") == 0.5
        assert validate_number(".5") == 0.5

    def test_validate_scientific_notation(self):
        """Test validating numbers in scientific notation."""
        assert validate_number("1e3") == 1000.0
        assert validate_number("1.5e2") == 150.0
        assert validate_number("1E-2") == 0.01

    def test_validate_with_whitespace(self):
        """Test that leading and trailing whitespace is stripped."""
        assert validate_number("  5  ") == 5.0
        assert validate_number("\t10\n") == 10.0
        assert validate_number("  3.14  ") == 3.14

    def test_validate_empty_string_raises_error(self):
        """Test that empty strings raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_number("")
        assert "Input cannot be empty" in str(exc_info.value)

    def test_validate_whitespace_only_raises_error(self):
        """Test that whitespace-only strings raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_number("   ")
        assert "Input cannot be empty" in str(exc_info.value)

        with pytest.raises(ValueError) as exc_info:
            validate_number("\t\n")
        assert "Input cannot be empty" in str(exc_info.value)

    def test_validate_non_numeric_string_raises_error(self):
        """Test that non-numeric strings raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_number("abc")
        assert "is not a valid number" in str(exc_info.value)

    def test_validate_invalid_formats_raise_error(self):
        """Test various invalid number formats."""
        invalid_inputs = ["12.34.56", "1a2", "5++", "1.2.3", "abc123"]
        for invalid_input in invalid_inputs:
            with pytest.raises(ValueError) as exc_info:
                validate_number(invalid_input)
            assert "is not a valid number" in str(exc_info.value)

    def test_validate_large_numbers(self):
        """Test validating very large numbers."""
        assert validate_number("999999999999") == 999999999999.0
        assert validate_number("1e100") == 1e100

    def test_validate_very_small_numbers(self):
        """Test validating very small numbers."""
        assert validate_number("0.0001") == 0.0001
        assert validate_number("1e-10") == 1e-10


class TestValidateOperation:
    """Tests for the validate_operation() function."""

    def test_validate_addition_operation(self):
        """Test validating addition operation."""
        assert validate_operation("+") == "+"

    def test_validate_subtraction_operation(self):
        """Test validating subtraction operation."""
        assert validate_operation("-") == "-"

    def test_validate_multiplication_operation(self):
        """Test validating multiplication operation."""
        assert validate_operation("*") == "*"

    def test_validate_division_operation(self):
        """Test validating division operation."""
        assert validate_operation("/") == "/"

    def test_validate_all_valid_operations(self):
        """Test all valid operations in one test."""
        for op in ["+", "-", "*", "/"]:
            assert validate_operation(op) == op

    def test_validate_operation_with_whitespace(self):
        """Test that whitespace is stripped from operations."""
        assert validate_operation("  +  ") == "+"
        assert validate_operation("\t-\n") == "-"
        assert validate_operation("  *") == "*"
        assert validate_operation("/  ") == "/"

    def test_validate_empty_operation_raises_error(self):
        """Test that empty operations raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_operation("")
        assert "Operation cannot be empty" in str(exc_info.value)

    def test_validate_whitespace_only_operation_raises_error(self):
        """Test that whitespace-only operations raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_operation("   ")
        assert "Operation cannot be empty" in str(exc_info.value)

        with pytest.raises(ValueError) as exc_info:
            validate_operation("\t\n")
        assert "Operation cannot be empty" in str(exc_info.value)

    def test_validate_invalid_operations_raise_error(self):
        """Test that unsupported operations raise ValueError."""
        invalid_ops = ["%", "^", "&", "|", "++", "**", "x", "add", "="]
        for invalid_op in invalid_ops:
            with pytest.raises(ValueError) as exc_info:
                validate_operation(invalid_op)
            error_msg = str(exc_info.value)
            assert "is not a supported operation" in error_msg
            assert f"'{invalid_op}'" in error_msg

    def test_validate_operation_multiple_characters_raises_error(self):
        """Test that multi-character strings raise ValueError."""
        with pytest.raises(ValueError) as exc_info:
            validate_operation("+-")
        assert "is not a supported operation" in str(exc_info.value)

    def test_validate_operation_error_message_includes_suggestion(self):
        """Test that error message includes supported operations."""
        with pytest.raises(ValueError) as exc_info:
            validate_operation("x")
        error_msg = str(exc_info.value)
        assert "Use +, -, *, or /" in error_msg


# ============================================================================
# PARAMETRIZED TESTS FOR COMPREHENSIVE COVERAGE
# ============================================================================


class TestArithmeticParametrized:
    """Parametrized tests for all arithmetic operations."""

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (0, 0, 0),
            (5, 0, 5),
            (0, 5, 5),
            (-5, 0, -5),
            (0, -5, -5),
            (3, 4, 7),
            (-3, 4, 1),
            (3, -4, -1),
            (-3, -4, -7),
            (1.5, 2.5, 4.0),
            (-1.5, 2.5, 1.0),
        ],
    )
    def test_add_parametrized(self, a, b, expected):
        """Parametrized tests for addition."""
        assert add(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (5, 3, 2),
            (0, 0, 0),
            (5, 0, 5),
            (0, 5, -5),
            (-3, -4, 1),
            (3, -4, 7),
            (-3, 4, -7),
            (5.5, 2.5, 3.0),
        ],
    )
    def test_subtract_parametrized(self, a, b, expected):
        """Parametrized tests for subtraction."""
        assert subtract(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (0, 0, 0),
            (5, 0, 0),
            (0, 5, 0),
            (1, 5, 5),
            (5, 1, 5),
            (3, 4, 12),
            (-3, 4, -12),
            (3, -4, -12),
            (-3, -4, 12),
            (2.5, 4, 10.0),
        ],
    )
    def test_multiply_parametrized(self, a, b, expected):
        """Parametrized tests for multiplication."""
        assert multiply(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (10, 2, 5.0),
            (5, 2, 2.5),
            (0, 5, 0.0),
            (-10, 2, -5.0),
            (10, -2, -5.0),
            (-10, -2, 5.0),
            (7.5, 2.5, 3.0),
        ],
    )
    def test_divide_parametrized(self, a, b, expected):
        """Parametrized tests for division."""
        assert divide(a, b) == pytest.approx(expected)

    @pytest.mark.parametrize("divisor", [0, 0.0, -0.0])
    def test_divide_by_zero_parametrized(self, divisor):
        """Parametrized tests for division by zero."""
        with pytest.raises(ValueError) as exc_info:
            divide(10, divisor)
        assert "Division by zero is not allowed" in str(exc_info.value)


class TestValidationParametrized:
    """Parametrized tests for validation functions."""

    @pytest.mark.parametrize(
        "value,expected",
        [
            ("0", 0.0),
            ("5", 5.0),
            ("-10", -10.0),
            ("3.14", 3.14),
            (".5", 0.5),
            ("1e3", 1000.0),
            ("  42  ", 42.0),
            ("\t5\n", 5.0),
        ],
    )
    def test_validate_number_valid_inputs(self, value, expected):
        """Parametrized tests for valid number inputs."""
        assert validate_number(value) == pytest.approx(expected)

    @pytest.mark.parametrize(
        "invalid_value",
        [
            "",
            "   ",
            "\t\n",
            "abc",
            "12.34.56",
            "1a2",
            "not_a_number",
        ],
    )
    def test_validate_number_invalid_inputs(self, invalid_value):
        """Parametrized tests for invalid number inputs."""
        with pytest.raises(ValueError):
            validate_number(invalid_value)

    @pytest.mark.parametrize("operation", ["+", "-", "*", "/"])
    def test_validate_operation_valid_inputs(self, operation):
        """Parametrized tests for valid operation inputs."""
        assert validate_operation(operation) == operation

    @pytest.mark.parametrize(
        "invalid_op",
        [
            "",
            "   ",
            "%",
            "^",
            "x",
            "add",
            "++",
            "**",
        ],
    )
    def test_validate_operation_invalid_inputs(self, invalid_op):
        """Parametrized tests for invalid operation inputs."""
        with pytest.raises(ValueError):
            validate_operation(invalid_op)


# ============================================================================
# EDGE CASES AND BOUNDARY CONDITIONS
# ============================================================================


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""

    def test_very_small_positive_numbers(self):
        """Test operations with very small positive numbers."""
        small = 1e-10
        assert add(small, small) == pytest.approx(2e-10)
        assert multiply(small, 2) == pytest.approx(2e-10)

    def test_operations_with_max_safe_integers(self):
        """Test operations with very large numbers."""
        large = 10**15
        assert add(large, large) == pytest.approx(2 * large)
        assert subtract(large, large) == 0

    def test_negative_zero_handling(self):
        """Test handling of negative zero."""
        assert subtract(0, 0) == 0
        assert add(-0, 0) == 0

    def test_division_resulting_in_very_small_number(self):
        """Test division producing very small results."""
        result = divide(1, 1000000)
        assert result == pytest.approx(1e-6)

    def test_chained_operations_with_floats(self):
        """Test multiple operations in sequence."""
        result1 = add(1.1, 2.2)
        result2 = multiply(result1, 2)
        result3 = divide(result2, 2)
        assert result3 == pytest.approx(3.3)

    def test_subtract_resulting_in_very_small_difference(self):
        """Test subtraction of very close numbers."""
        a = 1.0000001
        b = 1.0000002
        result = subtract(a, b)
        assert result == pytest.approx(-0.0000001)

    def test_validate_number_with_leading_sign(self):
        """Test validation of numbers with explicit sign."""
        assert validate_number("+5") == 5.0
        assert validate_number("+3.14") == 3.14

    def test_validate_number_zero_variations(self):
        """Test validation of zero in various formats."""
        assert validate_number("0") == 0.0
        assert validate_number("0.0") == 0.0
        assert validate_number("0e5") == 0.0
        assert validate_number(".0") == 0.0
