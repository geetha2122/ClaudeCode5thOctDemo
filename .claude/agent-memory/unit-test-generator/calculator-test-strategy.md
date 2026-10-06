---
name: calculator-test-strategy
description: Effective testing strategy for Python calculator arithmetic and validation functions
metadata:
  type: project
---

## Calculator Test Coverage Strategy

### Test Organization Patterns

Organized tests into logical class groupings by function domain:
- **TestAddOperation, TestSubtractOperation, TestMultiplyOperation, TestDivideOperation** — Focused class per arithmetic operation for clear organization
- **TestValidateNumber, TestValidateOperation** — Dedicated validation test classes
- **TestArithmeticParametrized** — Parametrized tests combining multiple operations for efficiency
- **TestValidationParametrized** — Parametrized validation tests for both valid and invalid inputs
- **TestEdgeCases** — Boundary conditions and special scenarios

**Why:** Class-based organization groups related tests visually and allows pytest to run related tests together. Parametrization reduces code duplication while increasing test count.

### Critical Edge Cases for Arithmetic Operations

**Division by zero** — Most critical edge case
- Test with positive numerator: `divide(10, 0)` raises ValueError
- Test with negative numerator: `divide(-10, 0)` raises ValueError  
- Test with zero numerator: `divide(0, 0)` raises ValueError
- Parametrize over zero variants `[0, 0.0, -0.0]` to catch all representations
- Always verify exact error message: `"Division by zero is not allowed"`

**Why:** Division by zero is explicitly handled with ValueError in the implementation and is the most important error condition.

**Float precision** — Use `pytest.approx()` for all floating-point assertions
- Operations like `add(0.1, 0.2)` produce floating-point rounding errors
- Never use direct equality for floats: `assert result == 3.3` fails
- Always use: `assert result == pytest.approx(3.3)`
- Apply to intermediate results in chained operations

**Why:** Binary floating-point representation cannot exactly represent decimal values like 0.3, causing precision errors in arithmetic.

**Negative zero** — Handle `-0.0` correctly
- Test that operations with `-0.0` work correctly
- Include in division parametrization: `[0, 0.0, -0.0]`
- Verify operations treat `-0.0` and `0.0` equivalently

### Validation Function Testing Patterns

**Number validation** (`validate_number()`)
- Valid inputs: integers, floats, negatives, scientific notation, with leading/trailing signs
- Whitespace handling: leading/trailing spaces, tabs, newlines are stripped
- Empty inputs: bare `""` and whitespace-only strings both raise "Input cannot be empty"
- Invalid formats: non-numeric, multiple decimals, embedded letters all raise "is not a valid number"
- Return type: always converts to `float`, so `validate_number("5")` returns `5.0`

**Why:** The validation logic has two distinct paths (empty check vs. format validation) and three input scenarios (valid, whitespace, invalid), requiring separate test methods.

**Operation validation** (`validate_operation()`)
- Valid operations: `['+', '-', '*', '/']` only
- Whitespace handling: `"  +  "` strips to `"+"`
- Empty/whitespace-only inputs raise "Operation cannot be empty"
- Invalid operations include: `%`, `^`, multi-character like `"++"`, and word-like `"add"`
- Error messages must include suggestions: `"Use +, -, *, or /"`

**Why:** Different error paths require separate tests to ensure each validation branch works correctly.

### Parametrization Approach

**Effective parametrization structure:**
```python
@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (5, 0, 5),
    # ... more test cases
])
def test_add_parametrized(self, a, b, expected):
    assert add(a, b) == pytest.approx(expected)
```

**Why:** Reduces test code by 70%, allows easy addition of test cases, makes test output clearly show which specific inputs failed.

**Coverage strategy:** Include at least one case for each distinct code path:
- Operations with zero (identity/absorbing element tests)
- Negative number combinations (e.g., neg+neg, neg+pos, pos+neg)
- Float inputs to verify type handling
- Large numbers to verify no overflow issues

### Test Determinism Requirements

All tests are deterministic and repeatable because:
- No random data generation
- No time-dependent logic
- No external system calls
- No file I/O
- All test data hardcoded in parametrization
- Using `pytest.approx()` for float comparisons (not random thresholds)

**Why:** Deterministic tests guarantee consistent CI/CD behavior and make debugging failures reproducible.

### Complete Test Count Achieved

**124 total tests** across:
- 6 TestAddOperation tests
- 6 TestSubtractOperation tests
- 6 TestMultiplyOperation tests
- 10 TestDivideOperation tests
- 11 TestValidateNumber tests
- 11 TestValidateOperation tests
- 11 TestArithmeticParametrized (add) tests
- 8 TestArithmeticParametrized (subtract) tests
- 10 TestArithmeticParametrized (multiply) tests
- 7 TestArithmeticParametrized (divide) tests
- 3 TestArithmeticParametrized (divide by zero) tests
- 8 TestValidationParametrized (number valid) tests
- 7 TestValidationParametrized (number invalid) tests
- 4 TestValidationParametrized (operation valid) tests
- 8 TestValidationParametrized (operation invalid) tests
- 8 TestEdgeCases tests

All tests pass with 100% success rate on Python 3.12 with pytest 9.1.1.

### Key Learnings for Future Tests

1. **Whitespace is a distinct test case** — Always test strings with leading/trailing whitespace separately from valid/invalid format tests
2. **Error messages matter** — Test that error messages are specific and helpful, not just that exceptions are raised
3. **Float precision is pervasive** — Use `pytest.approx()` for all float assertions, including intermediate results
4. **Negative variants needed** — For each positive test case, include negative, zero, and float variants
5. **Parametrization scales well** — Even 11 test cases for a simple validation function is manageable with parametrization and more maintainable than if-statements
