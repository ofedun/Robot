"""Class for handling input field elements."""
from base_element import BaseElement


class InputField(BaseElement):
    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver


    # def set_value(self, value):
    #     """Set the value of the form element."""
    #     element = self.driver.find_element_by_xpath(self.locator)
    #     if element.is_displayed():
    #         element.send_keys(value)

    def set_value(self, value):
        """Set the value of the form element."""
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        element.send_keys(value)

    def get_value(self):
        """Get the value of the form element.

        Returns:
            (str): A field value.
        """
        element = self.find_visible_element(self.locator, self.locator, self.timeout)
        return element
