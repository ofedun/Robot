"""logic code for Search object."""
from selenium.webdriver.support.ui import WebDriverWait
from Lib.elements import BaseElement

DEFAULT_CONTAINER = '//table[@id="maintable"]'
ATTRIBUTE = 'test'

ELEMENTMAP = {
    'search_box': '{container}//input[@name="searchstring"]',
    'row': '{container}//tr[@name="entry"]',
    'single_search_results_row': '{container}//tr[@name="entry"]/td[contains(., {"value"})]',
    'no_results_row': ''
}


class SearchTable(BaseElement):
    """Functionality for Search table."""
    def __init__(self, driver, container=DEFAULT_CONTAINER):
        super(BaseElement, self).__init__()
        self.driver = driver

    def search_for_items(self, value):
        """Perform a search."""
        self.driver.find_element_by_xpath(ELEMENTMAP['search_box'])
        row = self.driver.find_element_by_xpath(ELEMENTMAP['row'])
        script = 'arguments[0].setAttribute("{attr}", "{value}")'.format(
            attr=ATTRIBUTE,
            value=ATTRIBUTE
        )
        self.driver.execute_script(script, row)
        self.driver.find_element_by_xpath(ELEMENTMAP['single_search_results_row'])
        self.driver.find_element_by_xpath(ELEMENTMAP['search_box']).sendKeys(value)
        if self.driver.find_element_by_xpath(ELEMENTMAP['no_results_row']):
            WebDriverWait(self.driver, GLOBAL_TIMEOUT).until(ELEMENTMAP['row'], ATTRIBUTE)
        return self.find_text_in_search_results(value)

    def find_text_in_search_results(self, value):
        result = self.driver.find_element_by_xpath(ELEMENTMAP['single_search_results_row'])
        return result.text(value)