class BaseElement(object):
    """Class for handling elements on pages."""
    def __init__(self, driver):
        self.driver = driver
        # self.element_id = element_id,
        # self.timeout = timeout,
        # self.locator_type = locator_type,
        # self.wait_time = wait_time

    def click(self):
        self.element = self.driver.find_element_by_id('element_id')
        self.element.click()

    def get_text(self):
        """Get element text."""
        element = self.driver.find_element_by_id('elementID')
        return element.getText()




    # def is_element_visible(self, finder, selector, wait_time=None):
    #     wait_time = wait_time or self.wait_time
    #     end_time = time.time() + wait_time
    #
    #     while time.time() < end_time:
    #         if finder(selector) and finder(selector).visible:
    #             return True
    #     return False
    #
    # def check_visibility_with_retry(browser, locator_type, locator):
    #     """Check whether element is visible."""
    #     return getattr(browser, 'is_element_visible_by_' + locator_type)(locator)
    #
    # def click_element_with_retry(browser, locator_type, locator):
    #     """Click an element.
    #
    #     If there is one of the listed exceptions the click is tried again.
    #     """
    #     getattr(browser, 'find_by_' + locator_type)(locator).first.click()
