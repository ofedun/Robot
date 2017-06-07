"""Class for handling base components on the page."""

class BaseComponent(object):
    """Base for the base components.

    Provides functionality for page components.
    """
    def __init__(self, driver, element_tupple, timeout=10):
        self.driver = driver
        self.locator_type = element_tupple[0]
        self.locator = element_tupple[1]
        self.timeout = timeout
