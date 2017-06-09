"""logic code for Search object."""

from Lib.page_components import BaseComponent
from Lib.elements import InputField, TextElement

DEFAULT_CONTAINER = '//table[@id="maintable"]'
ATTRIBUTE = 'test'

ELEMENTMAP = {
    'search_box': ('xpath', '//input[@name="searchstring"]'),
    # 'row': ('xpath', '//tr[@name="entry"]'),
    'search_results_row': '//tr[@name="entry"]/td[contains(., {"value"})]',
    'no_results_row': '',
    'row': '//table[@id="maintable"]//tr[@name="entry"]',
    'name': '//table[@id="maintable"]//tr[@name="entry"]{row_number}/td[3]',
    'address': '',

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
        search_results = []
        for i in range(1, (len(self.driver.find_element_by_xpath(ELEMENTMAP['row'])))):
            search_data = {}
            name = TextElement(self.driver, ('xpath', (ELEMENTMAP['name']).format(row_number=i))).get_text()
            search_data['name']=name
            address = ''
            search_results.append(search_data)
        return search_results


        # for k, v in
        # TextElement(self.driver, ('xpath', ELEMENTMAP['search_results_row'].format(value=value))).get_element_with_retry()
