"""REPL interface for the command-line calculator."""

from __future__ import annotations
from calculator.operations import Calculator, parse_number
import sys


OPERATIONS = {
    "add": Calculator.add,
    "+": Calculator.add,
    "sub": Calculator.subtract,
    "-": Calculator.subtract,
    "mul": Calculator.multiply,
    "*": Calculator.multiply,
    "div": Calculator.divide,
    "/": Calculator.divide,
    "q": None,
    "quit": None,
    "exit": None,
}


def print_welcome():
    print("Calculator REPL")
    print("Type operation (add, sub, mul, div or + - * /). Type 'q' or 'quit' to exit.")
    print("Examples:")
    print("  add 3 4")
    print("  / 10 2")
    print()


def handle_line(line: str) -> bool:
    """
    Handle a single REPL line.
    Returns False if REPL should exit; True to continue.
    """
    line = line.strip()
    if not line:
        return True  # ignore empty lines

    parts = line.split()
    op_token = parts[0].lower()

    if op_token in ("q", "quit", "exit"):
        print("Goodbye.")
        return False

    if op_token not in OPERATIONS:
        print(f"Unknown operation: {op_token!r}. Use add, sub, mul, div or + - * /.")
        return True

    if len(parts) != 3:
        print("Expected format: <operation> <number1> <number2>")
        return True

    _, a_str, b_str = parts
    try:
        a = parse_number(a_str)
        b = parse_number(b_str)
    except ValueError as ve:
        print(f"Input error: {ve}")
        return True

    func = OPERATIONS[op_token]
    try:
        result = func(a, b)
    except ZeroDivisionError as zde:
        print(f"Math error: {zde}")
        return True
    except Exception as exc:
        print(f"Unexpected error: {exc}")
        return True

    # Nicely print integers without trailing .0 when possible
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    print(f"Result: {result}")
    return True


def repl():
    print_welcome()
    while True:
        try:
            line = input("> ")
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break
        keep_running = handle_line(line)
        if not keep_running:
            break


if __name__ == "__main__":
    repl()
