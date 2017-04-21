"""Component API for Login form."""
from Lib.elements import BaseElement


ELEMENTMAP = {
    'username': 'user',
    'password': 'pass',
    'login_button': '//input[@type="submit"]',
    'loggedin_user': ''
}

class LoginForm(BaseElement):
    """Functionality for the AddressBook Login Panel."""

    def login(self, username, password):
        """Attempt to log in to the system with AddressBook account credentials.

        Args:
            username (str): the username of the AddressBook user
            password (str): the password of the AddressBook user
        """
        self.driver.find_by_name(
            ELEMENTMAP['username']).first.fill(username)
        self.driver.find_by_name(
            ELEMENTMAP['password']).first.fill(password)
        login_button = self.driver.find_by_text(
            ELEMENTMAP['login_button'])
        login_button.click()

    def enter_username(self, username):
        self.driver.find_element_by_name(
            ELEMENTMAP['username']).first.fill(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(
            ELEMENTMAP['password']).first.fill(password)

    def click_submit_button(self):
        login_button = self.driver.find_elements_by_xpath(
            ELEMENTMAP['login_button'])
        login_button.click()

    def check_logged_in(self, expected):
        username = self.driver.find_by_text(
            ELEMENTMAP['loggedin_user'])
        if username == expected:
            return username

