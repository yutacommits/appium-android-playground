from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_scroll(self, locator):
        self.driver.implicitly_wait(0)
        timeout = 1
        wait = WebDriverWait(self.driver, timeout)
        retry = 0
        while retry < 2:
            try:
                return wait.until(EC.visibility_of_element_located(locator))
            except:
                self.scroll_down()
            finally:
                self.driver.implicitly_wait(5)
            retry += 1

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def scroll_down(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']

        self.driver.execute_script('mobile: scrollGesture', {
            'left': width * 0.1,
            'top': height * 0.1,
            'width': width * 0.8,
            'height': height * 0.8,
            'direction': 'down',
            'percent': 1.0
        })