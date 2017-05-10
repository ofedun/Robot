"""Steps for Login functionality."""
from Lib.pages import LoginPage
# from Lib.pages import HomePage


class LoginSteps(object):

    def __init__(self):
        self.login_page = LoginPage()
        # self.home_page = HomePage()


    def open_login_page(self, url, browser):
        self.login_page.visit(url, browser)

    def enter_username(self, username):
        self.login_page.enter_username(username)

    def enter_password(self, password):
        self.login_page.enter_password(password)

    def click_login_button(self):
        self.login_page.click_submit_button()

    # def attempt_to_login_with_credentials(self, username, password):
    #     self.login_page.login(username, password)

    def logged_in_on_main_page(self, expected):
        actual_user = self.home_page.get_current_username(expected)
        assert actual_user == expected
