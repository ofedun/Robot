"""Address Book homepage object."""
from .base_auth_page import BaseAuthPage
from Lib.page_components import SearchTable


class HomePage(BaseAuthPage):
    """Home page of Address Book."""
    def __init__(self, driver):
        BaseAuthPage.__init__(self, driver)
        self.search_table = SearchTable(self.driver)

    def search_an_address(self, value):
        """Search an address on the Home page.

        Args:
            value(str): A value to be searched.
        """
        self.actual_value = self.search_table.search_for_items(value)

    def get_search_results(self):
        """Get search results."""
        actual_results = self.search_table.get_search_results()
        return actual_results