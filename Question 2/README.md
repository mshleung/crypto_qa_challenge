# Question 2: Appium UI Automation for MyObservatory APK

## Project Overview
This project contains automated UI tests for the MyObservatory Android APK using Appium and pytest.

## Prerequisites
- Python 3.8 or newer (recommended: Python 3.10+)
- Poetry (for dependency and environment management)
- Appium server (running and accessible)
- Android emulator or device with the MyObservatory APK installed

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd <repo-root>/Question 2
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

### 5. Configure Appium and Emulator/Device
- Start the Appium server on another terminal window: appium -p 4723 (default: http://localhost:4723)
- Ensure your Android emulator or device is running and the APK path in `conftest.py` is correct.
- the APK that was used in this assignment is included in the root folder of this assignment. 

### 6. Run the Tests
You can run all tests using Poetry:
```
poetry run pytest -s tests/test_ui_automation.py
```
Or, if you activated the Poetry shell:
```
pytest -s tests/test_ui_automation.py
```

- The `-s` flag shows print/debug output from the tests.
- You can also run all tests in the folder:
```
poetry run pytest -s tests/
```

## File Structure
- `tests/test_ui_automation.py` — Main UI automation test suite
- `conftest.py` — Pytest fixtures for Appium driver setup/teardown
- `pyproject.toml` — Poetry dependency and environment configuration

## Notes
- Make sure the Appium server and emulator/device are running before executing tests.
- You can adjust device capabilities and APK path in `conftest.py` as needed.
- All dependencies (Appium-Python-Client, selenium, requests, pytest) are managed by Poetry.

## Troubleshooting
- If you see import errors, ensure you are running inside the Poetry environment.
- If Appium cannot connect to the device, check that the emulator/device is running and accessible.
- For more verbose output, add `-v` to the pytest command.

---

For any issues, please refer to the comments in the test and fixture files, or contact the project maintainer.
