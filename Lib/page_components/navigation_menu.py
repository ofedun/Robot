"""Logic code for Navigation object."""

from Lib.page_components import BaseComponent
from Lib.elements import Link

ELEMENTMAP = {
    'menu_item': '//li[@class="all"]/a[contains(text(), "{item_name}")]'
}

class NavigationElement(BaseComponent):
    """Functionality for the AddressBook navigation menu."""

    def __init__(self, driver):
        super(BaseComponent, self).__init__()
        self.driver = driver


    def click_menu_item(self, item_name):
        """Click item in navigation menu.

        Args:
            item_name(str): Item name to be clicked.
        """
        Link(self.driver, ('xpath', ELEMENTMAP['menu_item'].format(
            item_name=item_name))).click()
