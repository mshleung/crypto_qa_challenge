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