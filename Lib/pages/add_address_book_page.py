"""Add AddressBook page object."""
from Lib.pages.base_auth_page import BaseAuthPage
from Lib.elements import AddAddressBookForm

class AddAddressBookPage(BaseAuthPage):
    """Add AddressBook page.

    Provides API for Add AddressBook page.
    """
    def __init__(self, driver):
        BaseAuthPage.__init__(self, driver)
        self.add_address_element = AddAddressBookForm(self.driver)

    def enter_valid_data(self, address_data):
        self.add_address_element.enter_valid_data(address_data)
        self.add_address_element.click_add_address_action()
