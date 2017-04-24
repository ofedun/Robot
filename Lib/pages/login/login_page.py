"""Login page object."""
from Lib.pages import BasePage
from Lib.elements import LoginForm
from selenium import webdriver


class LoginPage(BasePage):
    """Login page.

    Provides API for Login page.
    """
    def __init__(self):
        super(BasePage, self).__init__()
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')
        self.login_form_elements = LoginForm(self.driver)


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

    def is_current_user(self, expected):
        self.login_form_elements.check_is_current_user(expected)
