"""Steps for Login functionality."""
class LoginSteps(object):

    def open_login_page(context):
        context.pages.login_page.visit()

    def attempt_to_login_with_credentials(self, username, password):
        self.pages.login_page.login(username, password)

    def i_am_logged_in_on_main_page(self):
        self.pages.login_page.logged_in()