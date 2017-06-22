"""Edit AddressBook page object."""
from Lib.pages.base_auth_page import BaseAuthPage
from Lib.page_components import EditAddressBookForm

class EditAddressBookPage(BaseAuthPage):
    """Edit AddressBook page.

    Provides API for Edit AddressBook page.
    """
    def __init__(self, driver):
        BaseAuthPage.__init__(self, driver)
        self.edit_address_component = EditAddressBookForm(self.driver)

    def enter_data_on_edit(self, address_data):
        """Edit an address."""
        self.edit_address_component.enter_data_on_edit(address_data)
        self.edit_address_component.click_update_address_action()

    def get_address_details(self):
        """Get address details on Edit page."""
        return self.edit_address_component.get_address_details()

