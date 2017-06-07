"""Logic code for Navigation object."""
from selenium.webdriver.support.wait import WebDriverWait

from Lib.elements import BaseElement
# from Lib.page_components import BaseComponent
from Lib.elements import Link

ELEMENTMAP = {
    'menu_item': '//li[@class="all"]/a[contains(text(), "{item_name}")]'
}

class NavigationElement(BaseElement):
    """Functionality for the AddressBook navigation menu."""

    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver

        # self.menu_item = Link(self.driver, ELEMENTMAP['menu_item'])


    def click_menu_item(self, item_name):
        """Click item in navigation menu.

        Args:
            item_name(str): Item name to be clicked.
        """
        # self.menu_item.click()
        self.driver.find_element_by_xpath(
            ELEMENTMAP['menu_item'].format(item_name=item_name)).click()
