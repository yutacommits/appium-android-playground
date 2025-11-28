from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from pages.settings_home_page import SettingsHomePage


def test_find_apps(driver):
    settings = SettingsHomePage(driver)
    settings.open_apps()


def test_disable_bluetooth(driver):
    settings = SettingsHomePage(driver)
    connected_devices = settings.open_connected_devices()
    connection_preferences = connected_devices.open_connection_preferences()
    bluetooth = connection_preferences.open_bluetooth()
    bluetooth.toggle_bluetooth()
