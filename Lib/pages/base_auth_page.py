"""Address Book BaseAuth Page object."""
from .base_page import BasePage
from Lib.elements import HeaderElement
from Lib.elements import NavigationElement


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
            bool: True if expected user is logged in.

        """
        return self.header_elements.get_current_username(expected)

    def open_add_new_address(self):
        """Open Add New Address page."""
        self.navigation_menu.click_menu_item('add new')

    # def select_navigation(self):
    #
    # def log_out(self):