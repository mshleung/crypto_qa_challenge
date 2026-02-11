"""
Conftest file for Appium test setup and configuration.
"""
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


@pytest.fixture
def driver_android():
    """Fixture to setup and teardown Android driver."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"  # Change this to your device
    options.app = "/Users/mac/Downloads/myobservatory-5-18.apk"  # Change this to your app path
    options.automation_name = "UiAutomator2"
    options.no_reset = False  # Reinstall app before each test
    
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    # Uninstall app after test
    driver.remove_app("com.myobservatory")  # Change this to your app's package name
    driver.quit()


@pytest.fixture
def driver_ios():
    """Fixture to setup and teardown iOS driver."""
    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.device_name = "iPhone 15"  # Change this to your device
    options.app = "/path/to/your/app.app"  # Change this to your app path
    options.automation_name = "XCUITest"
    
    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
