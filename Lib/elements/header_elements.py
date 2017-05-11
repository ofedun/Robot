"""Logic code for Header object"""
from Lib.elements import BaseElement

ELEMENTMAP = {
    'logout_link': 'Logout',
    'logged_username': '//form[@class="header"]/b["{{name}}"]'
}

class HeaderElement(BaseElement):
    """Functionality for the AddressBook header panel."""

    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver

    def get_current_username(self, expected):
        self.driver.find_element_by_link_text(
            ELEMENTMAP['logout_link'])
        username = self.driver.find_element_by_xpath(
            ELEMENTMAP['logged_username'].format(name=expected))
        return username.text[1:-1]