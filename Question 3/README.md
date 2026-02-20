# Question 3: SZSE Market Data API Test Project

## Project Overview
This project demonstrates how to access and verify market data from the Shenzhen Stock Exchange (SZSE) API using Python and pytest.

## Prerequisites
- Python 3.8 or newer (recommended: Python 3.10+)
- Poetry (for dependency and environment management)

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/mshleung/crypto_qa_challenge
cd <repo-root>/Question 3
```

### 2. Install Poetry (if not already installed)
```
pip install poetry
```

### 3. Install Dependencies
Poetry will create and manage a virtual environment for you:
```
poetry install
```

### 4. Activate the Poetry Environment (optional)
You can run commands directly with Poetry (see below), or activate the shell:
```
poetry shell
```

## Running the Tests

All test scripts are located in the `tests/` directory.

To run the main market data test:
```
poetry run pytest -s tests/test_market_data_api.py
```
Or, if you activated the Poetry shell:
```
pytest -s tests/test_market_data_api.py
```

- The `-s` flag shows print/debug output from the tests.
- You can also run all tests in the folder:
```
poetry run pytest -s tests/
```

## File Structure
- `tests/test_market_data_api.py` — Main test script for SZSE market data API
- `pyproject.toml` — Poetry dependency and environment configuration

## Notes
- The test script generates a random cache-busting parameter for each API request.
- The script robustly handles network, HTTP, and data extraction errors.
- All dependencies (requests, pytest) are managed by Poetry.

## Troubleshooting
- If you see import errors, ensure you are running inside the Poetry environment.
- If the API response changes or is unavailable, check your internet connection and the SZSE site status.
- For more verbose output, add `-v` to the pytest command.

---

For any issues, please refer to the comments in the test script or contact the project maintainer.
