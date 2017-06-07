"""Edit AddressBook page object."""
from Lib.pages.base_auth_page import BaseAuthPage

class EditAddressBookPage(BaseAuthPage):
    """Edit AddressBook page.

    Provides API for Edit AddressBook page.
    """
    def __init__(self, driver):
        BaseAuthPage.__init__(self, driver)

    # def edit_an_address(self):

