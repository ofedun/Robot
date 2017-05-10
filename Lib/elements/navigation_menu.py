"""Logic code for Navigation object."""
from Lib.elements import BaseElement

ELEMENTMAP = {
    'add_new_link': '//li[@class="all"]/a[contains(text(), "add new")]'
}

class NavigationElement(BaseElement):
    """Functionality for the AddressBook navigation menu."""

    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver

    def get_current_username(self, expected):
        self.driver.find_element_by_link_text(
            ELEMENTMAP['logout_link'])
        username = self.driver.find_element_by_xpath(
            ELEMENTMAP['logged_username'].format(name=expected))
        return username.text[1:-1]

    def open_add_new_address(self):
        self.driver.find_element_by_xpath(
            ELEMENTMAP['add_new_link']).click()