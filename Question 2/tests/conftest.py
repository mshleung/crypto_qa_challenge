"""
Conftest file for Appium test setup and configuration.
"""
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection
from appium.common.helper import library_version


@pytest.fixture(scope="module")
def driver_android():
    """Fixture to setup and teardown Android driver."""
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"  # Change this to your device
    options.app = "/Users/mac/Downloads/myobservatory-5-18.apk"  # Change this to your app path
    options.automation_name = "UiAutomator2"
    options.no_reset = False  # Reinstall app before each test
    # Auto grant runtime permissions on install
    options.set_capability("autoGrantPermissions", True)
    
    # Create a RemoteConnection using ClientConfig to avoid deprecated RemoteConnection warnings
    client_config = ClientConfig(remote_server_addr="http://localhost:4723", keep_alive=True)
    # Ensure Appium-style User-Agent header remains present
    RemoteConnection.user_agent = f"appium/{library_version()} ({RemoteConnection.user_agent})"
    remote_conn = RemoteConnection(client_config=client_config)
    driver = webdriver.Remote(command_executor=remote_conn, options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def uninstall_app_after_session():
    """Uninstall the app once after the whole test session finishes."""
    yield
    # Create a lightweight driver to remove the app at the end of the session.
    try:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.device_name = "emulator-5554"
        options.automation_name = "UiAutomator2"
        # Do not set options.app to avoid reinstalling

        client_config = ClientConfig(remote_server_addr="http://localhost:4723", keep_alive=True)
        RemoteConnection.user_agent = f"appium/{library_version()} ({RemoteConnection.user_agent})"
        remote_conn = RemoteConnection(client_config=client_config)
        drv = webdriver.Remote(command_executor=remote_conn, options=options)
        drv.remove_app("hko.MyObservatory_v1_0")
        drv.quit()
    except Exception:
        # best-effort uninstall; ignore errors
        pass


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
