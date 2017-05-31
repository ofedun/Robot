"""Class for handling base element on the page."""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseElement(object):
    def __init__(self, driver, locator, locator_type, timeout=10):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type
        self.timeout = timeout

    def click(self):
        self.element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        self.element.click()

    def click_element_with_retry(self, locator_type, locator):
        """Click an element.

        If there is one of the listed exceptions the click is tried again.
        """
        getattr(self.driver, 'find_element_by_' + locator_type)(locator).click()

    def get_text(self):
        """Get element text."""
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        return element.getText()

    def get_element_with_retry(self, locator_type, locator):
        """Get element(s)."""
        return getattr(self.driver, 'find_element_by_' + locator_type)(locator)

    def find_visible_element(self, locator_type, locator, timeout=None):
        # element = getattr(self, 'find_by_' + locator_type)(locator)
        wait = WebDriverWait(self.driver, 10)
        # elements = wait.until(EC.presence_of_element_located((self.driver, By.XPATH(locator))))
        elements = wait.until(EC.presence_of_element_located(
            getattr(self.driver, 'find_element_by_' + locator_type)(locator)))
        return elements
