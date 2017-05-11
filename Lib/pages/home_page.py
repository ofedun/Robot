"""Address Book homepage object."""
from .base_auth_page import BaseAuthPage


class HomePage(BaseAuthPage):
    """Home page of Address Book."""
    def __init__(self):
        BaseAuthPage.__init__(self)

    # def search_address(self):