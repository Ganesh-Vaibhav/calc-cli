# calc-cli

A simple command-line calculator with a REPL interface, built in Python. Includes full unit tests using `pytest` and a GitHub Actions CI pipeline that enforces **100% test coverage**.

## Features
- REPL interface (interactive)
- Arithmetic: addition, subtraction, multiplication, division
- Input validation and clear error messages
- Graceful handling of division by zero
- Comprehensive unit tests (parameterized) and CI coverage enforcement

## Setup (local)
1. Clone and create a GitHub repo, or initialize locally:
```bash
git init
```
# add files, commit, create GitHub repo, push...
Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate    # Windows (PowerShell)
```
# Install dependencies:
```bash
pip install -r requirements.txt
Run the REPL
python -m calculator.cli
```
```bash
Examples:
> add 2 3
Result: 5
> / 10 2
Result: 5
> quit
Goodbye.
Running tests locally
pytest --cov=calculator --cov-fail-under=100
This will run tests and fail if coverage is below 100%.
```
# Continuous Integration
A GitHub Actions workflow is included at .github/workflows/ci.yml. It runs the same command as above on every push/pull request and enforces the 100% coverage requirement.
# Notes on design
calculator.operations contains the pure logic (easy to test).
calculator.cli handles the REPL and uses the operations functions — separation keeps logic/testable and UI minimal.
Input parsing is centralized in parse_number to follow DRY.
