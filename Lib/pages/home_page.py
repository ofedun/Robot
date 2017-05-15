"""Address Book homepage object."""
from .base_auth_page import BaseAuthPage


class HomePage(BaseAuthPage):
    """Home page of Address Book."""
    def __init__(self, driver):
        BaseAuthPage.__init__(self, driver)

    # def search_address(self):