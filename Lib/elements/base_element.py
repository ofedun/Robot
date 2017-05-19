"""Class for handling base element on the page."""

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

    def find_visible_element(self, locator_type, locator, timeout):
        try:
            element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
        finally:
            ff.quit(
