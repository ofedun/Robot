"""Logic code for Header object."""
from Lib.page_components import BaseComponent
from Lib.elements import TextElement

ELEMENTMAP = {
    'logout_link': '//form[@name="logout"]//a[contains(., "Logout")]',
    'logged_username': '//form[@class="header"]/b["{{name}}"]'
}

class HeaderElement(BaseComponent):
    """Functionality for the AddressBook header panel."""

    def __init__(self, driver):
        super(BaseComponent, self).__init__()
        self.driver = driver


    def get_current_username(self, expected):
        """Get current logged in username.

        Args:
            expected(str): Expected username.

        Returns:
            str: Logged in username.
        """
        username = TextElement(
            self.driver, ('xpath', ELEMENTMAP['logged_username'].format(name=expected)))
        return username.get_text()[1:-1]
