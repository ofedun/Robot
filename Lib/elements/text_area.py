"""Class for handling Text area elements."""
from base_element import BaseElement, TIMEOUT


class TextArea(BaseElement):


    def set_value(self, value):
        """Set the value of the form element.

        Args:
           value(str): Value to be set.
        """
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        if element.is_displayed():
            element.clear()
            element.send_keys(value)

    def get_value(self):
        """Get the value of the form element.

        Returns:
            (str): A field value.
        """
        element = self.find_visible_element(self.locator_type, self.locator, self.timeout)
        return element.text
