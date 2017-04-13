"""Steps for Login functionality."""
from Lib.pages import LoginPage

class LoginSteps(object):

    def __init__(self):
        self.page = LoginPage()

    def open_login_page(self):
        self.page.visit()

    def attempt_to_login_with_credentials(self, username, password):
        self.page.login(username, password)

    def i_am_logged_in_on_main_page(self):
        self.page.logged_in()