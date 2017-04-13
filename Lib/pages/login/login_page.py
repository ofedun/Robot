"""Login page object."""
from Lib.pages import BasePage


class LoginPage(BasePage):
    """Login page.

    Provides API for Login page.
    """

    def login(self, username, password):
        self.visit()
        self.login_page.enter_user_name(username)
        self.login_page.enter_password(password)
        self.click_submit_button()

    def enter_user_name(self, username):
        self.elements.login.enter_user_name(username)

    def enter_password(self, password):
        self.elements.login.enter_password(password)

    def click_submit_button(self):
        self.elements.login.click_submit_button()
