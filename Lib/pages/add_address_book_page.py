"""Add AddressBook page object."""
from Lib.pages.base_auth_page import BaseAuthPage
from Lib.page_components import AddAddressBookForm

class AddAddressBookPage(BaseAuthPage):
    """Add AddressBook page.

    Provides API for Add AddressBook page.
    """
    def __init__(self, driver):
        BaseAuthPage.__init__(self, driver)
        self.add_address_form = AddAddressBookForm(self.driver)

    def enter_valid_data(self, address_data):
        self.add_address_form.enter_valid_data(address_data)
        self.add_address_form.click_add_address_action()
