# Appium Setup Guide

## Prerequisites

1. **Node.js**: Install from https://nodejs.org/
2. **Java JDK**: Required for Android testing
3. **Android SDK**: For Android emulator and testing
4. **Xcode**: For iOS testing (macOS only)
5. **Python 3.x**: Your Python environment

## Installation Steps

### 1. Install Appium Server

```bash
npm install -g appium
```

### 2. Install Appium Drivers

```bash
appium driver install uiautomator2  # For Android
appium driver install xcuitest      # For iOS
```

### 3. Install Python Dependencies

```bash
cd /Users/mac/Documents/crypto_qa_challenge/Question\ 2
pip install -r requirements.txt
```

## Running Appium Server

### Start Appium Server (Default: localhost:4723)

```bash
appium
```

### Or with specific host and port

```bash
appium --address 127.0.0.1 --port 4723
```

## Technology Stack

- **Appium**: Open-source tool for mobile UI automation
- **Selenium WebDriver**: For element interaction and waiting
- **pytest**: Test framework for organizing and running tests

## Configure Your Tests

1. Update the device names, app paths, and platform details in `conftest.py`
2. Modify element locators in `test_ui_automation.py` to match your application
3. Add your specific test scenarios

## Running Tests

```bash
# Run all tests
pytest test_ui_automation.py -v

# Run specific test
pytest test_ui_automation.py::TestUIAutomation::test_app_launch -v

# Run with detailed output
pytest test_ui_automation.py -v -s
```

## Common Element Locator Strategies

- `AppiumBy.ID`: Android resource ID or iOS accessibility identifier
- `AppiumBy.CLASS_NAME`: Element class name
- `AppiumBy.XPATH`: XPath query
- `AppiumBy.ACCESSIBILITY_ID`: Accessibility identifier
- `AppiumBy.ANDROID_UIAUTOMATOR`: Android UIAutomator query
- `AppiumBy.PREDICATE`: iOS predicate string

## Useful Resources

- [Appium Documentation](https://appium.io/)
- [Appium Python Client](https://github.com/appium/python-client)
- [Selenium Wait Documentation](https://www.selenium.dev/documentation/webdriver/waits/)
