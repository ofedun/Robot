"""Component API for Add AddressBook form."""
from Lib.elements import BaseElement

ELEMENTMAP = {
    'next_button': '//input[@value="Next"][1]',
    'first_name': '//input[@name="firstname"]',
    'middle_name': '//input[@name="middlename"]',
    'last_name': '//input[@name="lastname"]',
    'address_input': '//textarea[@name="address"]',
    'company': '//input[@name="company"]',
    'email': '//input[@name="email"]',
    'mobile_telephone': '//input[@name="mobile"]',
    'enter_button': '//input[@value="Enter"][2]'

}

class AddAddressBookForm(BaseElement):
    """Functionality for the Add AddressBook form."""
    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver

    def enter_valid_data(self, address_data):
        next_button = self.driver.find_by_xpath['next_button']
        next_button.click()
        for fild_name, value in address_data:
            form_element = self.get_form_element(
                self, ELEMENTMAP[self.to_form_element_name(fild_name)])
            form_element.set_value(value)


    def click_add_address_action(self):
        enter_button = self.driver.find_by_text(
            ELEMENTMAP['enter_button'])
        enter_button.click()