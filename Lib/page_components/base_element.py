import time

class BaseElement(object):
    """Class for handling page_components on pages."""
    def __init__(self, driver, wait_time, klass, element_id):
        self.driver = driver
        self.klass = klass
        self.element_id = element_id,
        # self.timeout = timeout,
        # self.locator_type = locator_type,
        self.wait_time = wait_time

    def click(self):
        self.element = self.driver.find_element_by_id('element_id')
        self.element.click()

    def get_text(self):
        """Get element text."""
        element = self.driver.find_element_by_id('elementID')
        return element.getText()

    def check_visibility_with_retry(browser, locator_type, locator):
        """Check whether element is visible."""
        return getattr(browser, 'is_element_visible_by_' + locator_type)(locator)

    def is_element_visible_by_xpath(self, xpath, wait_time=None):
        return self.is_element_visible(self.driver.find_by_xpath, xpath, wait_time)

    def is_element_visible(self, finder, selector, wait_time=None):
        wait_time = wait_time or self.wait_time
        end_time = time.time() + wait_time

        while time.time() < end_time:
            if finder(selector) and finder(selector).visible:
                return True
        return False

    def to_form_element_name(field_name):
        """Convert field name to match item in element map."""
        return field_name.strip().replace(' ', '_').replace('/', '_').lower()

    def get_object(self, browser, timeout):
        """Initialise and return the form element."""
        return self.klass(self.element_id, browser, timeout)

    def get_form_element(form, element_id):
        """Get form element for provided element ID."""
        matches = [
            x for x in form._form_elements(form)
            if x.element_id == element_id]
        if len(matches) == 0:
            raise NotImplementedError(
                'You have not defined a field for element "{element_id}"'
                    .format(element_id=element_id)
            )
        return matches[0].get_object(form.driver, 10)

    def _form_elements(form):
        return [getattr(form, x) for x in dir(form)
                if type(getattr(form, x)) == BaseElement]



    # def is_element_visible(self, finder, selector, wait_time=None):
    #     wait_time = wait_time or self.wait_time
    #     end_time = time.time() + wait_time
    #
    #     while time.time() < end_time:
    #         if finder(selector) and finder(selector).visible:
    #             return True
    #     return False
    #

    #
    # def click_element_with_retry(browser, locator_type, locator):
    #     """Click an element.
    #
    #     If there is one of the listed exceptions the click is tried again.
    #     """
    #     getattr(browser, 'find_by_' + locator_type)(locator).first.click()
