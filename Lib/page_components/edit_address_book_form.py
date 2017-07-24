"""Component for Edit Addressbook form."""
from Lib.elements import TextArea
from Lib.page_components import BaseComponent
from Lib.elements import InputField
from Lib.elements import Button


ELEMENTMAP = {
    'edit_address_button':
        '//table[@id="maintable"]//tr[@name="entry"]/td[contains(., "{address_name}")]'
        '/following-sibling::td/a/img[@title="Edit"]',
    'update_button': ('xpath', '//input[@value="Update"]'),
    'first_name': ('xpath', '//input[@name="firstname"]'),
    'middle_name': ('xpath', '//input[@name="middlename"]'),
    'last_name': ('xpath', '//input[@name="lastname"]'),
    'address': ('xpath', '//textarea[@name="address"]'),
    'company': ('xpath', '//input[@name="company"]'),
    'email': ('xpath', '//input[@name="email"]'),
    'mobile': ('xpath', '//input[@name="mobile"]')
}

class EditAddressBookForm(BaseComponent):
    """Functionality for Edit Addressbook form."""
    def __init__(self, driver):
        super(BaseComponent, self).__init__()
        self.driver = driver

        self.first_name = InputField(self.driver, ELEMENTMAP['first_name'])
        self.middle_name = InputField(self.driver, ELEMENTMAP['middle_name'])
        self.last_name = InputField(self.driver, ELEMENTMAP['last_name'])
        self.address = TextArea(self.driver, ELEMENTMAP['address'])
        self.company = InputField(self.driver, ELEMENTMAP['company'])
        self.email = InputField(self.driver, ELEMENTMAP['email'])
        self.mobile = InputField(self.driver, ELEMENTMAP['mobile'])

    def open_edit_address(self, address_name):
        """Open Edit Address action."""
        edit_address_action = Button(
            self.driver, ('xpath', ELEMENTMAP['edit_address_button'].format(address_name=address_name)))
        edit_address_action.click()

    def enter_data_on_edit(self, address_data):
        for field_name, field_value in address_data.items():
            getattr(self, field_name.replace(' ', '_').lower()).set_value(field_value)

    def click_update_address_action(self):
        Button(self.driver, ELEMENTMAP['update_button']).click()

    def get_address_details(self):
        """Get address details on Edit page.

        Returns:
            address_dict(dict): an address details.
        """
        address_dict = {
            'First name': self.first_name.get_value(),
            'Middle name': self.middle_name.get_value(),
            'Last name': self.last_name.get_value(),
            'Address': self.address.get_value(),
            'Company': self.company.get_value(),
            'Email': self.email.get_value(),
            'Mobile': self.mobile.get_value()
        }
        return address_dict
