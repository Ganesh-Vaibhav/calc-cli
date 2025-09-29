import pytest
from calculator import operations
from calculator.operations import Calculator, parse_number
from calculator.cli import handle_line
# Parameterized tests for arithmetic operations
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (-1, 5, 4),
        (0, 0, 0),
        (2.5, 1.5, 4.0),
    ],
)
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (5, 3, 2),
        (0, 5, -5),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6),
        (5, 0, 0),
        (2.5, 4, 10.0),
    ],
)
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (6, 3, 2),
        (5, 2, 2.5),
    ],
)
def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)


# parse_number tests covering ints, floats, whitespace, and bad inputs
@pytest.mark.parametrize(
    "s,expected",
    [
        ("10", 10),
        ("  -3  ", -3),
        ("2.5", 2.5),
        ("  0.0", 0.0),
    ],
)
def test_parse_number_valid(s, expected):
    assert parse_number(s) == expected


@pytest.mark.parametrize("s", ["", "   ", "abc", "1,000", "12a"])
def test_parse_number_invalid(s):
    with pytest.raises(ValueError):
        parse_number(s)


# Tests that exercise CLI's handle_line branches to ensure coverage
def test_handle_line_success(tmp_path, capsys):
    # Use a known good line
    cont = handle_line("add 2 3")
    assert cont is True
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out


def test_handle_line_unknown_operation(capsys):
    cont = handle_line("pow 2 2")
    assert cont is True
    captured = capsys.readouterr()
    assert "Unknown operation" in captured.out


def test_handle_line_bad_format(capsys):
    cont = handle_line("add 1")
    assert cont is True
    captured = capsys.readouterr()
    assert "Expected format" in captured.out


def test_handle_line_input_error(capsys):
    cont = handle_line("add foo 1")
    assert cont is True
    captured = capsys.readouterr()
    assert "Input error" in captured.out


def test_handle_line_divide_by_zero(capsys):
    cont = handle_line("div 5 0")
    assert cont is True
    captured = capsys.readouterr()
    assert "Math error" in captured.out


def test_handle_line_quit(capsys):
    cont = handle_line("quit")
    assert cont is False
    captured = capsys.readouterr()
    assert "Goodbye" in captured.out
