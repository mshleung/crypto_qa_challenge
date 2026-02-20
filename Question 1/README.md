# Question 1: Pyramid Generator Function

## Project Overview
This project implements and tests a function to generate a centered pyramid pattern using a specified character and number of levels.

## Prerequisites
- Python 3.8 or newer (recommended: Python 3.10+)
- pytest (for running the test suite)

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd <repo-root>/Question 1
```

### 2. (Optional) Create a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install pytest
```

## Running the Solution
To generate and print a pyramid directly:
```
python3 solution.py
```

## Running the Tests
To run all tests and see detailed output:
```
pytest -s test_solution.py
```

- The `-s` flag shows print/debug output from the tests.
- You can also use `pytest -v -s test_solution.py` for more verbose output.

## File Structure
- `solution.py` — Contains the `generate_pyramid` function and example usage
- `test_solution.py` — Test suite for the pyramid function

## Notes
- The function and tests handle a variety of edge cases and input validation.
- All tests are self-contained and require only pytest as a dependency.

---

For any issues, please refer to the comments in the code or contact the project maintainer.
