"""Steps for Add AddressBook functionality."""
import string

from Lib.pages import AddAddressBookPage
from Lib.pages import HomePage
from Lib.pages import BaseAuthPage
from Lib.pages import EditAddressBookPage
from Lib.steps_implementation.Browser import Browser
import random

from database import Database


class AddAddressSteps(object):

    def __init__(self):
        self.driver = Browser().get_driver()

        self.add_address_book_page = AddAddressBookPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.base_auth_page = BaseAuthPage(self.driver)
        self.edit_address_page = EditAddressBookPage(self.driver)
        self.test_suffix = self.get_random_string()


    def open_add_address_page(self, item_name):
        self.base_auth_page.open_menu_item(item_name)

    def enter_valid_data(self):
        default_data = self.prepare_address_properties()
        default_data['Address'] = self.append_suffix(default_data['Address'])
        self.add_address_book_page.enter_valid_data(default_data)

    def search_an_address(self, value):
        value = self.append_suffix(value)
        self.home_page.search_an_address(value)
        actual_results = self.home_page.get_search_results()

        address_list = []
        for item in actual_results:
            actual_adddress = item['address']
            address_list.append(actual_adddress)
        assert value in address_list

    def load_dump_file(self):
        self.database = Database('localhost', 'root', 'password', 'address_book')
        self.database.load_dump('/home/olena/src/address-book/robot/dump.sql')

    def open_edit_address_page_with_address_name(self, address_name):
        address_name = self.append_suffix(address_name)
        self.home_page.open_edit_address(address_name)

    def i_edit_an_address_with_the_details(self):
        address_data = self.prepare_address_properties()
        address_updated_data = {
            'First name': 'Robot',
            'Last name': 'Test1',
            'Address': 'New York-{suffix}'.format(suffix=self.test_suffix)
        }
        address_data.update(address_updated_data)
        self.edit_address_page.enter_data_on_edit(address_data)

    def the_address_should_be_updated_with_appropriate_details(self):
        actual_address_details = self.edit_address_page.get_address_details()
        expected_address_data = {
            'First name': 'Robot',
            'Last name': 'Test1',
            'Address': 'New York-{suffix}'.format(suffix=self.test_suffix)
        }
        for key, value in expected_address_data.iteritems():
            # print('key:'+key)
            # print('Value:'+value)
            assert value == actual_address_details[key]

    def delete_an_address(self, address_name):
        address_name = self.append_suffix(address_name)
        self.home_page.delete_an_address(address_name)

    def address_should_be_deleted(self, address_name):
        address_name = self.append_suffix(address_name)
        self.home_page.search_an_address(address_name)
        actual_results = self.home_page.get_search_results()
        assert address_name not in actual_results

    def prepare_address_properties(self):
        # address_data = {}
        default_data = {
            'First name': 'First name',
            'Middle name': 'Middle name',
            'Last name': 'Last',
            'Address': 'London',
            'Company': 'Company',
            'Mobile': 'Mobile',
            'Email': 'Email'
        }
        # default_data.update(address_data)
        return default_data

    def get_random_string(self, lenght=5):
        """Generate random alphabetical string.

        Args:
            lenght: how long random string should be.

        Returns:
            string: a randomly generated string.
        """
        return ''.join(random.sample(string.lowercase, lenght))

    def append_suffix(self, value):
        """Generate the suffix.

        Args:
            value(str): value to add suffix to.

        Returns:
            str: a string of randomly generated suffix.
        """
        return '{value}-{suffix}'.format(value=value, suffix=self.test_suffix)
