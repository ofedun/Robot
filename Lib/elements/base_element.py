"""Class for handling base element on the page."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, element_tuple, timeout=10):
        self.driver = driver
        self.locator_type = element_tuple[0]
        self.locator = element_tuple[1]
        self.timeout = timeout

    def click(self):
        """Click action."""
        self.element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        self.element.click()

    def get_text(self):
        """Get element text.

        Returns:
            str: text of the element.
        """
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        return element.text

    def find_visible_element(self, locator_type, locator, timeout=None):
        wait = WebDriverWait(self.driver, 10)
        # elements = wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        # my_by_xpath = By.XPATH
        my_by_xpath = getattr(By, locator_type.upper())
        elements = wait.until(EC.presence_of_element_located((my_by_xpath, locator)))
        return elements
