"""Class for handling input field elements."""
from selenium.common.exceptions import NoSuchElementException


class InputField(object):
    def __init__(self, locator, driver, xpath, timeout):
        self.locator = locator
        self.driver = driver
        self.xpath = xpath
        self.timeout = timeout

    def set_value(self, value):
        """Set the value of the form element."""
        self.driver.is_element_present_by_id(self.xpath, self.timeout)
        value.send_keys()

    def get_value(self):
        """Get the value of the form element.

        Returns:
            (str): A field value.
        """
        self.driver.is_element_present_by_id(self.xpath, self.timeout)
        return self.driver.find_by_id(self.xpath).first.value

    def is_element_present_by_id(self, text):
        try:
            body = self.driver.find_element_by_xpath(self.xpath)  # find element by xpath
        except NoSuchElementException:
            return False
        return text in body.text  # check if the xpath is present