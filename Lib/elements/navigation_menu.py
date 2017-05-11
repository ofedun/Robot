"""Logic code for Navigation object."""
from Lib.elements import BaseElement

ELEMENTMAP = {
    'menu_item': '//li[@class="all"]/a[contains(text(), "{item_name}")]'
}

class NavigationElement(BaseElement):
    """Functionality for the AddressBook navigation menu."""

    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver


    # def open_add_new_address(self):
    #     self.driver.find_element_by_xpath(
    #         ELEMENTMAP['add_new_link']).click()

    def click_menu_item(self, item_name):
        self.driver.find_element_by_xpath(
            ELEMENTMAP['menu_item'].format(item_name=item_name)).click()
