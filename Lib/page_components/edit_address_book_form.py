"""Component for Edit Addressbook form."""

from Lib.page_components import BaseComponent
from Lib.elements import InputField
from Lib.elements import Button


ELEMENTMAP = {
    'edit_address': '//table[@id="maintable"]//tr[@name="entry"]/td/a/img[@title="Edit"]',
    'update_button': '//input[@value="Update"]'
}

class EditAddressBookForm(BaseComponent):
    """Functionality for Edit Addressbook form."""
    def __init__(self, driver):
        super(BaseComponent, self).__init__()
        self.driver = driver

        # self.edit_button = Button(self.driver, ELEMENTMAP['edit_button'])
        self.update_button = Button(self.driver, ELEMENTMAP['update_button'])

    def open_edit_address(self, address_name):
        """Open Edit Address action."""
        edit_address_action = Button(self.driver, ('xpath', ELEMENTMAP['edit_button']))
        edit_address_action.click()
