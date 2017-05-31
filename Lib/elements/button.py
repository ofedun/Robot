"""Class for handling buttons on pages."""
from Lib.elements import BaseElement


class Button(BaseElement):
    """Class for handling buttons on pages."""

    def __init__(self, driver, element_tuple, timeout=10):
        self.driver = driver
        self.locator_type = element_tuple[0]
        self.locator = element_tuple[1]
        self.timeout = timeout
        super(BaseElement, self).__init__()

    def click_with_retry(self):
        """Click on the button."""
        self.find_visible_element(
            self.locator_type,
            self.locator,
            self.timeout
        )
        self.click_element_with_retry(
            self.locator_type,
            self.locator
        )

    # def check_visibility_with_retry(driver, locator_type, locator):
    #     """Check whether element is visible."""
    #     return getattr(driver, 'is_element_visible_by_' + locator_type)(locator)