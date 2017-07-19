"""Class for handling base element on the page."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10

class BaseElement(object):
    def __init__(self, driver, element_tuple, timeout=TIMEOUT):
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

    def find_visible_element(self, locator_type, locator, timeout=TIMEOUT):
        """Find visible element.

        Returns:
            element : the WebElement once it is located.
        """
        wait = WebDriverWait(self.driver, timeout)
        find_by_locator = getattr(By, locator_type.upper())
        element = wait.until(EC.presence_of_element_located((find_by_locator, locator)))
        return element
