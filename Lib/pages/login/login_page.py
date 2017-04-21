"""Login page object."""
from Lib.pages import BasePage
from Lib.elements import LoginForm


class LoginPage(BasePage):
    """Login page.

    Provides API for Login page.
    """
    def __init__(self):
        BasePage.__init__(self)
        self.login_form_elements = LoginForm(driver=self.driver)


    def login(self, username, password):
        self.visit()
        self.login_form_elements.enter_username(username)
        self.login_form_elements.enter_password(password)
        self.click_submit_button()

    def enter_username(self, username):
        self.login_form_elements.enter_username(username)

    def enter_password(self, password):
        self.login_form_elements.enter_password(password)

    def click_submit_button(self):
        self.login_form_elements.click_submit_button()

    def logged_in_on_main_page(self, expected):
        self.login_form_elements.check_logged_in(expected)
