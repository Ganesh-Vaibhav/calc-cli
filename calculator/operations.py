"""Core calculator operations and input helpers."""

from __future__ import annotations
from typing import Union

Number = Union[int, float]


class Calculator:
    """Simple calculator implementing basic arithmetic operations."""

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        return a + b

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        return a - b

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        return a * b

    @staticmethod
    def divide(a: Number, b: Number) -> Number:
        if b == 0:
            # Explicit, clear error for callers
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


def parse_number(s: str) -> Number:
    """
    Parse a string into an int or float.
    Raises ValueError if the input is not a valid number representation.
    """

    s = s.strip()
    if s == "":
        raise ValueError("Empty input is not a number.")

    # Try int first, then float
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError as exc:
            raise ValueError(f"Invalid number: {s!r}") from exc
