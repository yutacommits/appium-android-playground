from appium.webdriver.common.appiumby import AppiumBy
from .base_page import BasePage


class BluetoothPage(BasePage):
    TOGGLE = (
        AppiumBy.XPATH,
        '//android.widget.Switch[@resource-id="android:id/switch_widget"]',
    )

    def toggle_bluetooth(self):
        self.click(self.TOGGLE)

    def is_bluetooth_enabled(self):
        el = self.find(self.TOGGLE)
        return el.get_attribute("checked") == "true"
