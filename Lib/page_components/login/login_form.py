"""Component API for Login form."""
from Lib.page_components import BaseComponent
from Lib.elements import InputField, Button


ELEMENTMAP = {
    'username': ('xpath', '//input[@name="user"]'),
    'password': ('xpath', '//input[@name="pass"]'),
    'login_button': ('xpath', '//input[@type="submit"]')
}

class LoginForm(BaseComponent):
    """Functionality for the AddressBook Login Panel."""

    def __init__(self, driver):
        super(BaseComponent, self).__init__()
        self.driver = driver

        self.username = InputField(self.driver, ELEMENTMAP['username'])
        self.password = InputField(self.driver, ELEMENTMAP['password'])
        self.login_button = Button(self.driver, ELEMENTMAP['login_button'])

    def login(self, username, password):
        """Attempt to log in to the system with AddressBook account credentials.

        Args:
            username (str): the username of the AddressBook user
            password (str): the password of the AddressBook user
        """
        self.username.set_value(username)
        self.password.set_value(password)
        self.login_button.click()

    def enter_username(self, username):
        self.username.set_value(username)

    def enter_password(self, password):
        self.password.set_value(password)

    def click_submit_button(self):
        self.login_button.click()
