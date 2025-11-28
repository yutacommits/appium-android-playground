from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from .bluetooth_page import BluetoothPage


class ConnectionPreferencesPage(BasePage):
    BLUETOOTH = (AppiumBy.XPATH, '//*[@text="Bluetooth"]')

    def open_bluetooth(self):
        self.click(self.BLUETOOTH)
        return BluetoothPage(self.driver)
