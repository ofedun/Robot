"""Component API for Add AddressBook form."""
from Lib.elements import BaseElement

ELEMENTMAP = {

}

class AddAddressBookForm(BaseElement):
    """Functionality for the Add AddressBook form."""
    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver

    def enter_valid_data(self):
        pass