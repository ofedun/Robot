"""logic code for Search object."""

from Lib.page_components import BaseComponent
from Lib.elements import InputField, TextElement

DEFAULT_CONTAINER = '//table[@id="maintable"]'
ATTRIBUTE = 'test'

ELEMENTMAP = {
    'search_box': ('xpath', '//input[@name="searchstring"]'),
    'search_results_row': '//tr[@name="entry"]/td[contains(., {"value"})]',
    'no_results_row': '',
    'row': '//table[@id="maintable"]//tr[@name="entry"]',
    'name': '//table[@id="maintable"]//tr[@name="entry"]{row_number}/td[3]',
    'address': '//table[@id="maintable"]//tr[@name="entry"][1]/td[4]',
    'all_email': '//table[@id="maintable"]//tr[@name="entry"][1]/td[5]',
    'all_phones': '//table[@id="maintable"]//tr[@name="entry"][1]/td[6]'

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

    def get_search_results(self):
        """Get search results.

        Returns:
            search_results(list): A list of dicts.
        """
        # search_results = []
        # address_rows = self.driver.find_element_by_xpath(ELEMENTMAP['row'])
        # for i in range(1, len(address_rows)):
        #     search_data = {}
        #     name = TextElement(self.driver, ('xpath', (ELEMENTMAP['name']).format(row_number=i))).get_text()
        #     search_data['name']=name
        #     address = TextElement(self.driver, ('xpath', (ELEMENTMAP['address']).format(row_number=i))).get_text()
        #     search_data['address']=address
        #     all_email = TextElement(self.driver, ('xpath', (ELEMENTMAP['all_email']).format(row_number=i))).get_text()
        #     search_data['all_email']=all_email
        #     all_phones = TextElement(self.driver, ('xpath', (ELEMENTMAP['all_phones']).format(row_number=i))).get_text()
        #     search_data['all_phones']=all_phones
        #     # search_data = {
        #     #     'name': name,
        #     #     'address': address,
        #     #     'all_email': all_email,
        #     #     'all_phones': all_phones
        #     # }
        #     search_results.append(search_data)
        # return search_results

        search_results = []
        address_rows = self.driver.find_element_by_xpath(ELEMENTMAP['row']).text
        for i in range(len(address_rows)):
            address_data = {
                'name': TextElement(self.driver, ('xpath', (ELEMENTMAP['name']).format(row_number=i))[i]).get_text(),
                'address': TextElement(self.driver, ('xpath', (ELEMENTMAP['address']).format(row_number=i))[i]).get_text(),
                'all_email': TextElement(self.driver, ('xpath', (ELEMENTMAP['all_email']).format(row_number=i))).get_text(),
                'all_phones': TextElement(self.driver, ('xpath', (ELEMENTMAP['all_phones']).format(row_number=i))).get_text()
            }
            search_results.append(address_data)
        return search_results
