# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python Console Calculator** — a simple command-line utility that performs basic arithmetic operations (+, -, *, /) with comprehensive input validation and error handling.

## Running the Application

```bash
python3 calculator.py
```

The calculator runs interactively, prompting for two numbers and an operation, then displaying the result.

## Architecture

The codebase is structured as a single-file application:

**calculator.py** — Contains:
- **Operation functions** (`add`, `subtract`, `multiply`, `divide`) — Pure arithmetic operations
- **Validation functions** (`validate_number`, `validate_operation`) — Input validation with error context
- **main()** — Interactive loop that orchestrates user prompts, validation, operation dispatch, and error handling

The design separates concerns: operation logic is distinct from validation, which is distinct from the UI/interaction layer. Error handling is centralized in `main()` using exception handling for both validation errors and user interruption.

## Development

There are no build steps or external dependencies. The project uses only Python 3.x standard library.

**To test**: Run `python3 calculator.py` manually and verify behavior across normal cases (basic arithmetic) and error cases (invalid input, division by zero, unsupported operations).

## Git History

- **335cc77** — Initial implementation with core arithmetic and validation
- **09e8f32** — Added README documentation
