"""Steps for Add AddressBook functionality."""
from Lib.pages import AddAddressBookPage
from Lib.pages import HomePage
from Lib.steps_implementation.base_test import BaseTest

class AddAddressBook(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.add_address_book_page = AddAddressBookPage(self.driver)
        self.home_page = HomePage(self.driver)


    def open_add_new_address_page(self):
        self.home_page.open_add_new_address()

    def enter_valid_data(self):
        self.add_address_book_page.enter_valid_data()
