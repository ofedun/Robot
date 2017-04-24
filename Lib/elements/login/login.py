"""Component API for Login form."""
from Lib.elements import BaseElement


ELEMENTMAP = {
    'username': 'user',
    'password': 'pass',
    'login_button': '//input[@type="submit"]',
    'logout_link': 'Logout',
    'logged_username': 'admin'
}

class LoginForm(BaseElement):
    """Functionality for the AddressBook Login Panel."""

    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver

    def login(self, username, password):
        """Attempt to log in to the system with AddressBook account credentials.

        Args:
            username (str): the username of the AddressBook user
            password (str): the password of the AddressBook user
        """
        self.driver.find_element_by_name(
            ELEMENTMAP['username']).first.fill(username)
        self.driver.find_element_by_name(
            ELEMENTMAP['password']).first.fill(password)
        login_button = self.driver.find_by_text(
            ELEMENTMAP['login_button'])
        login_button.click()

    def enter_username(self, username):
        self.driver.find_element_by_name(
            ELEMENTMAP['username']).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(
            ELEMENTMAP['password']).send_keys(password)

    def click_submit_button(self):
        login_button = self.driver.find_element_by_xpath(
            ELEMENTMAP['login_button'])
        login_button.click()

    def check_is_current_user(self, expected):
        self.driver.find_element_by_link_text(
                ELEMENTMAP['logout_link'])
        username = self.driver.find_element_by_xpath(
            ELEMENTMAP['logged_username'])
        if username == expected:
            return username

