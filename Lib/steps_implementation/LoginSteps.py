"""Steps for Login functionality."""
from Lib.pages import LoginPage


class LoginSteps(object):

    def __init__(self):
        self.login_page = LoginPage()


    def open_login_page(self, url, browser):
        self.login_page.visit(url, browser)

    def enter_username(self, username):
        self.login_page.enter_username(username)

    def enter_password(self, password):
        self.login_page.enter_password(password)

    def click_login_button(self):
        self.login_page.click_submit_button()

    def attempt_to_login_with_credentials(self, username, password):
        self.login_page.login(username, password)

    def logged_in_on_main_page(self, expected):
        actual_user = self.login_page.is_current_user(expected)
        assert actual_user == expected


    #     assert username == expected
    #     if not username(expected):
    #         raise AssertionError("No username: '%s'" % (expected))
