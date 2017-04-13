"""Component API for Login form."""

ELEMENTMAP = {
    'username': 'username',
    'password': 'password',
    'login_button': 'Login'
}

class LoginForm(object):
    """Functionality for the AddressBook Login Panel."""

    def __init__(self, container_element):
        """Instantiate the object.

        Args:
            container_element (WebDriverElement): the web element that contains
                the login box. All element location must only take place within
                this context, rather than the entire page.
        """
        self.container = container_element

    def login(self, username, password):
        """Attempt to log in to the system with AddressBook account credentials.

        Args:
            username (str): the username of the AddressBook user
            password (str): the password of the AddressBook user
        """
        self.container.find_by_name(
            ELEMENTMAP['username']).first.fill(username)
        self.container.find_by_name(
            ELEMENTMAP['password']).first.fill(password)
        login_button = self.container.find_by_text(
            ELEMENTMAP['login_button'])
        login_button.click()

    def enter_user_name(self, username):
        self.container.find_by_name(
            ELEMENTMAP['username']).first.fill(username)

    def enter_password(self, password):
        self.container.find_by_name(
            ELEMENTMAP['password']).first.fill(password)

    def click_submit_button(self):
        login_button = self.container.find_by_text(
            ELEMENTMAP['login_button'])
        login_button.click()