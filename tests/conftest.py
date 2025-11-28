import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName="Android",
    automationName="uiautomator2",
    deviceName="Android",
    appPackage="com.android.settings",
    appActivity=".Settings",
    language="en",
    locale="US",
)

appium_server_url = "http://localhost:4723"


@pytest.fixture()
def driver():
    driver = webdriver.Remote(
        appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities)
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
