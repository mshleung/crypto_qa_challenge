"""
UI Automation tests using Appium.
"""
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUIAutomation:
    """Test suite for UI automation."""
    
    def test_app_launch(self, driver_android):
        """Test that the app launches successfully."""
        assert driver_android is not None
        # Take a screenshot to verify the app loaded
        driver_android.save_screenshot("app_launch.png")
        print("App launched successfully!")
    
    def test_find_element_by_id(self, driver_android):
        """Test finding an element by ID."""
        # Example: Find element by resource ID
        element = driver_android.find_element(AppiumBy.ID, "com.example.app:id/button")
        assert element is not None
    
    def test_find_element_by_class_name(self, driver_android):
        """Test finding an element by class name."""
        elements = driver_android.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
        assert len(elements) > 0
    
    def test_find_element_by_xpath(self, driver_android):
        """Test finding an element by XPath."""
        element = driver_android.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Click']")
        assert element is not None
    
    def test_click_button(self, driver_android):
        """Test clicking a button."""
        button = driver_android.find_element(AppiumBy.ID, "com.example.app:id/button")
        button.click()
        # Add assertion to verify the action result
    
    def test_send_keys(self, driver_android):
        """Test sending text to an input field."""
        input_field = driver_android.find_element(AppiumBy.ID, "com.example.app:id/textinput")
        input_field.send_keys("Hello, Appium!")
        assert input_field.get_attribute("text") == "Hello, Appium!"
    
    def test_wait_for_element(self, driver_android):
        """Test waiting for an element to appear."""
        wait = WebDriverWait(driver_android, 10)
        element = wait.until(
            EC.presence_of_element_located((AppiumBy.ID, "com.example.app:id/element"))
        )
        assert element is not None
    
    def test_get_element_text(self, driver_android):
        """Test getting text from an element."""
        element = driver_android.find_element(AppiumBy.ID, "com.example.app:id/text_view")
        text = element.text
        assert text is not None
    
    def test_element_displayed(self, driver_android):
        """Test if an element is displayed."""
        element = driver_android.find_element(AppiumBy.ID, "com.example.app:id/button")
        assert element.is_displayed()
    
    def test_element_enabled(self, driver_android):
        """Test if an element is enabled."""
        element = driver_android.find_element(AppiumBy.ID, "com.example.app:id/button")
        assert element.is_enabled()
