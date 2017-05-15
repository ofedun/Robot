"""Login page object."""
from Lib.pages import BasePage
from Lib.elements import LoginForm


class LoginPage(BasePage):
    """Login page.

    Provides API for Login page.
    """
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.login_form_elements = LoginForm(self.driver)


    def login(self, username, password):
        """Login into AddressBook site.

        Args:
            username (str): the username of AddressBook user.
            password (str): the password to set.
        """
        self.visit()
        self.login_form_elements.enter_username(username)
        self.login_form_elements.enter_password(password)
        self.login_form_elements.click_submit_button()

    def enter_username(self, username):
        """Enter username on Login form.

        Args:
            username (str): the username of AddressBook user.
        """
        self.login_form_elements.enter_username(username)

    def enter_password(self, password):
        """Enter password on Login form.

        Args:
            password (str): the password to set.
        """
        self.login_form_elements.enter_password(password)

    def click_submit_button(self):
        """Click Submit button on Login form."""
        self.login_form_elements.click_submit_button()

