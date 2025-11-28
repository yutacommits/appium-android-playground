from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from .connection_preferences_page import ConnectionPreferencesPage


class ConnectedDevicesPage(BasePage):
    CONNECTION_PREFERENCES = (AppiumBy.XPATH, '//*[@text="Connection preferences"]')

    def open_connection_preferences(self):
        self.click(self.CONNECTION_PREFERENCES)
        return ConnectionPreferencesPage(self.driver)
