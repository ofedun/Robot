"""Component API for Add AddressBook form."""
from Lib.elements import InputField
from Lib.elements import BaseElement
from Lib.elements import Button

# GLOBAL_TIMEOUT = 10

ELEMENTMAP = {
    'next_button': ('xpath', '//input[@value="Next"][1]'),
    'first_name': ('xpath', '//input[@name="firstname"]'),
    'middle_name': ('xpath', '//input[@name="middlename"]'),
    'last_name': ('xpath', '//input[@name="lastname"]'),
    'address': ('xpath', '//textarea[@name="address"]'),
    'company': ('xpath', '//input[@name="company"]'),
    'email': ('xpath', '//input[@name="email"]'),
    'mobile': ('xpath', '//input[@name="mobile"]'),
    'enter_button': ('xpath', '//input[@value="Enter"][2]')

}

# driver = 'blahhh'


class AddAddressBookForm(BaseElement):
    """Functionality for the Add AddressBook form."""
    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver


        # for key, value in ELEMENTMAP.items():
        #     setattr(self, key, InputField(self, value))

        self.first_name = InputField(self.driver, ELEMENTMAP['first_name'])
        self.middle_name = InputField(self.driver, ELEMENTMAP['middle_name'])
        self.last_name = InputField(self.driver, ELEMENTMAP['last_name'])
        self.address = InputField(self.driver, ELEMENTMAP['address'])
        self.company = InputField(self.driver, ELEMENTMAP['company'])
        self.email = InputField(self.driver, ELEMENTMAP['email'])
        self.mobile = InputField(self.driver, ELEMENTMAP['mobile'])
        # self.next_button = Button(self.driver, ELEMENTMAP['next_button'])
        # self.enter_button = Button(self.driver, ELEMENTMAP['enter_button'])


    def enter_valid_data(self, address_data):
        next_button = self.driver.find_element_by_xpath(ELEMENTMAP['next_button'][1])
        next_button.click()
        # self.next_button.click_with_retry()
        for field_name, value in address_data.items():
            getattr(self, field_name.replace(' ', '_').lower()).set_value(value)


    def click_add_address_action(self):
        enter_button = self.driver.find_element_by_xpath(
            ELEMENTMAP['enter_button'][1])
        enter_button.click()
        # print(driver)
        # print(self.driver)
