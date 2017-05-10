"""Steps for Add AddressBook functionality."""
from Lib.pages import AddAddressBookPage
from Lib.pages import HomePage

class AddAddressBook(object):

    def __init__(self):
        self.add_address_book_page = AddAddressBookPage
        self.home_page = HomePage


    def open_add_new_address_page(self):
        self.home_page.open_add_new_address()

    def enter_valid_data(self):
        self.add_address_book_page.enter_valid_data()