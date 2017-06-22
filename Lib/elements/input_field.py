"""Class for handling input field elements."""
from base_element import BaseElement


class InputField(BaseElement):
    def __init__(self, driver, element_tuple, timeout=10):
        self.driver = driver
        self.locator_type = element_tuple[0]
        self.locator = element_tuple[1]
        self.timeout = timeout
        super(BaseElement, self).__init__()


    def set_value(self, value):
        """Set the value of the form element.

        Args:
           value(str): Value to be set.
        """
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        if element.is_displayed():
            element.send_keys(value)

    def get_value(self):
        """Get the value of the form element.

        Returns:
            (str): A field value.
        """
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        return element.text
