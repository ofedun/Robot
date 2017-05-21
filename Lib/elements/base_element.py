"""Class for handling base element on the page."""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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

    def get_text(self):
        """Get element text."""
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        return element.getText()

    def get_element_with_retry(self, locator_type, locator):
        """Get element(s)."""
        return getattr(self, 'find_by_' + locator_type)(locator)

    def find_visible_element(self, locator_type, locator, timeout=None):
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.presence_of_element_located(locator))
        # return element

        element = self.driver.find_element_by_xpath(locator)
        # element = getattr(self, 'find_by_' + locator_type)(locator)
        wait = WebDriverWait(self.driver, 10)
        elements = wait.until(EC.presence_of_element_located(element))
        return elements


        # try:
        #     elements = WebDriverWait(element, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        # finally:
        #     ff.quit()
        # return

    # def is_element_present(self, finder, selector, wait_time=None):
    #     wait_time = wait_time or self.wait_time
    #     end_time = time.time() + wait_time
    #
    #     while time.time() < end_time:
    #         if finder(selector):
    #             return True
    #     return False