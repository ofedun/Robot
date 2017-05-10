"""Add AddressBook page object."""
from Lib.pages import HomePage
from Lib.elements import AddAddressBookForm

class AddAddressBookPage(HomePage):
    """Add AddressBook page.

    Provides API for Add AddressBook page.
    """
    def __init__(self):
        HomePage.__init__(self)
        self.add_address_element = AddAddressBookForm(self.driver)

    def enter_valid_data(self):
        self.add_address_element.enter_valid_data()
