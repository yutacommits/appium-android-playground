from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage
from .connected_devices_page import ConnectedDevicesPage


class SettingsHomePage(BasePage):
    APPS = (AppiumBy.XPATH, '//*[@text="Apps"]')
    CONNECTED_DEVICES = (AppiumBy.XPATH, '//*[@text="Connected devices"]')

    def open_apps(self):
        self.click(self.APPS)

    def open_connected_devices(self):
        self.click(self.CONNECTED_DEVICES)
        return ConnectedDevicesPage(self.driver)
