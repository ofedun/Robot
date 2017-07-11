"""logic code for Search object."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Lib.page_components import BaseComponent
from Lib.elements import Button, InputField, TextElement, CheckboxElement

TIMEOUT = 10

ELEMENTMAP = {
    'search_box': ('xpath', '//input[@name="searchstring"]'),
    'search_results_row': '//tr[@name="entry"]/td[contains(., {"value"})]',
    'no_results_row': '',
    'row': '//table[@id="maintable"]//tr[@name="entry"]',
    'name': '//table[@id="maintable"]//tr[@name="entry"][{row_number}]/td[3]',
    'address': '//table[@id="maintable"]//tr[@name="entry"][{row_number}]/td[4]',
    'all_email': '//table[@id="maintable"]//tr[@name="entry"][{row_number}]/td[5]',
    'all_phones': '//table[@id="maintable"]//tr[@name="entry"][{row_number}]/td[6]',
    'select_address':
        '//table[@id="maintable"]//tr[@name="entry"]/'
        'td[contains(., "{address_name}")]/parent::*/td/input[@type="checkbox"]',
    'delete_button': '//input[@value="Delete"]'

}


class SearchTable(BaseComponent):
    """Functionality for Search table."""
    def __init__(self, driver, container=DEFAULT_CONTAINER):
        super(BaseComponent, self).__init__()
        self.driver = driver

        self.search_field = InputField(self.driver, ELEMENTMAP['search_box'])


    def search_for_items(self, value):
        """Perform a search action with specified value."""
        self.search_field.set_value(value)

    def select_the_address(self, address_name):
        """Select an address action."""
        select_address_action = CheckboxElement(
            self.driver, ('xpath', ELEMENTMAP['select_address'].format(address_name=address_name)))
        select_address_action.click()

    def delete_address_action(self):
        """Click delete address."""
        delete_button = Button(self.driver, ('xpath', ELEMENTMAP['delete_button']))
        delete_button.click()
        self.wait_and_confirm_popup()

    def wait_and_confirm_popup(self):
        try:
            WebDriverWait(self.driver, TIMEOUT).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            print("no alert to accept")

    def get_search_results(self):
        """Get search results.

        Returns:
            search_results(list): A list of dicts.
        """
        search_results = []
        address_rows = self.driver.find_elements_by_xpath(ELEMENTMAP['row'])
        for i in range(len(address_rows)):
            address_data = {
                'name': TextElement(
                    self.driver, ('xpath', (ELEMENTMAP['name']).format(
                        row_number=i+1))).get_text(),
                'address': TextElement(
                    self.driver, ('xpath', (ELEMENTMAP['address']).format(
                        row_number=i+1))).get_text(),
                'all_email': TextElement(
                    self.driver, ('xpath', (ELEMENTMAP['all_email']).format(
                        row_number=i+1))).get_text(),
                'all_phones': TextElement(
                    self.driver, ('xpath', (ELEMENTMAP['all_phones']).format(
                        row_number=i+1))).get_text()
            }
            search_results.append(address_data)
        return search_results
