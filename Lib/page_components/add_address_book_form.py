"""Component API for Add AddressBook form."""
from Lib.elements import InputField
from Lib.elements import BaseElement

GLOBAL_TIMEOUT = 10

ELEMENTMAP = {
    'next_button': '//input[@value="Next"][1]',
    'first_name': '//input[@name="firstname"]',
    'middle_name': '//input[@name="middlename"]',
    'last_name': '//input[@name="lastname"]',
    'address': '//textarea[@name="address"]',
    'company': '//input[@name="company"]',
    'email': '//input[@name="email"]',
    'mobile': '//input[@name="mobile"]',
    'enter_button': '//input[@value="Enter"][2]'

}

# driver = 'blahhh'


class AddAddressBookForm(BaseElement):
    """Functionality for the Add AddressBook form."""
    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver


        # for key, value in ELEMENTMAP.items():
        #     setattr(self, key, InputField(self, value))

        # self.first_name = InputField(self.driver, ELEMENTMAP['first_name'])
        self.first_name = InputField(ELEMENTMAP['first_name'])
        self.middle_name = InputField(ELEMENTMAP['middle_name'])
        self.last_name = InputField(ELEMENTMAP['last_name'])
        self.address = InputField(ELEMENTMAP['address'])
        self.company = InputField(ELEMENTMAP['company'])
        self.email = InputField(ELEMENTMAP['email'])
        self.mobile = InputField(ELEMENTMAP['mobile'])


    def enter_valid_data(self, address_data):
        next_button = self.driver.find_element_by_xpath(ELEMENTMAP['next_button'])
        next_button.click()
        for field_name, value in address_data.items():
            getattr(self, field_name.replace(' ', '_').lower()).set_value(value)


    def click_add_address_action(self):
        enter_button = self.driver.find_element_by_xpath(
            ELEMENTMAP['enter_button'])
        enter_button.click()
        # print(driver)
        # print(self.driver)
