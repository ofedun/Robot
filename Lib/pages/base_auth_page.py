"""Address Book BaseAuth Page object."""
from .base_page import BasePage
from Lib.page_components import HeaderElement
from Lib.page_components import NavigationElement


class BaseAuthPage(BasePage):
    """BaseAuth Page of Address Book."""
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.header_elements = HeaderElement(self.driver)
        self.navigation_menu = NavigationElement(self.driver)


    def get_current_username(self, expected):
        """Get name of logged in user.

        Args:
            expected (str): the name of expected user.

        Returns:
            str: Name of logged in user.

        """
        return self.header_elements.get_current_username(expected)

    def open_menu_item(self, item_name):
        """Open Add New Address page.

        Args:
            item_name(str): Item name to navigate.
        """
        self.navigation_menu.click_menu_item(item_name)

    # def log_out(self):