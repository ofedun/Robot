"""Steps for Add AddressBook functionality."""
from Lib.pages import AddAddressBookPage
from Lib.pages import HomePage
from Lib.pages import BaseAuthPage
from Lib.pages import EditAddressBookPage
from Lib.steps_implementation.Browser import Browser


class AddAddressSteps(object):

    def __init__(self):
        self.driver = Browser().get_driver()

        self.add_address_book_page = AddAddressBookPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.base_auth_page = BaseAuthPage(self.driver)
        self.edit_address_page = EditAddressBookPage(self.driver)


    def open_add_address_page(self, item_name):
        self.base_auth_page.open_menu_item(item_name)

    def enter_valid_data(self):
        default_data = self.prepare_address_properties()
        self.add_address_book_page.enter_valid_data(default_data)

    def search_an_address(self, value):
        self.home_page.search_an_address(value)
        actual_results = self.home_page.get_search_results()
        assert value in actual_results

    def open_edit_address_page(self, item_name):
        self.base_auth_page.open_menu_item(item_name)

    def i_edit_the_address(self):
        self.edit_address_page.edit_an_address()

    def prepare_address_properties(self):
        # address_data = {}
        default_data = {
            'First name': 'First name',
            'Middle name': 'Middle name',
            'Last name': 'Last',
            'Address': 'Address',
            'Company': 'Company',
            'Mobile': 'Mobile',
            'Email': 'Email'
        }
        # default_data.update(address_data)
        return default_data