"""Steps for Add AddressBook functionality."""
from Lib.pages import AddAddressBookPage
from Lib.pages import HomePage
from Lib.pages import BaseAuthPage
from Lib.steps_implementation.base_test import BaseTest


class AddAddressSteps(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.add_address_book_page = AddAddressBookPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.base_auth_page = BaseAuthPage(self.driver)


    def open_add_new_address_page(self, item_name):
        self.base_auth_page.open_menu_item(item_name)

    def enter_valid_data(self):
        default_data = self.prepare_address_properties()
        self.add_address_book_page.enter_valid_data(default_data)

    def prepare_address_properties(self):
        # address_data = {}
        default_data = {
            'First name': '',
            'Middle name': '',
            'Last name': '',
            'Address': '',
            'Company': '',
            'Mobile': '',
            'E-mail': ''
        }
        # default_data.update(address_data)
        return default_data