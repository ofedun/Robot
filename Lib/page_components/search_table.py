"""logic code for Search object."""

from Lib.page_components import BaseComponent
from Lib.elements import InputField, TextElement

DEFAULT_CONTAINER = '//table[@id="maintable"]'
ATTRIBUTE = 'test'

ELEMENTMAP = {
    'search_box': ('xpath', '//input[@name="searchstring"]'),
    # 'row': ('xpath', '//tr[@name="entry"]'),
    'search_results_row': '//tr[@name="entry"]/td[contains(., {"value"})]',
    'no_results_row': ''
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

    def get_search_results(self, value):
        """Get search results."""
        TextElement(self.driver, ('xpath', ELEMENTMAP['search_results_row'].format(value=value))).get_element_with_retry()



        # if self.driver.find_element_by_xpath(ELEMENTMAP['no_results_row']):
        #     WebDriverWait(self.driver, GLOBAL_TIMEOUT=10).until(ELEMENTMAP['row'], ATTRIBUTE)
        # return self.find_text_in_search_results(value)

    # def find_text_in_search_results(self, value):
    #     result = self.driver.find_element_by_xpath(ELEMENTMAP['single_search_results_row'])
    #     return result.text(value)