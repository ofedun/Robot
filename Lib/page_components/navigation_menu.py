"""Logic code for Navigation object."""
from selenium.webdriver.support.wait import WebDriverWait

from Lib.page_components import BaseElement

ELEMENTMAP = {
    'menu_item': '//li[@class="all"]/a[contains(text(), "{item_name}")]'
}

class NavigationElement(BaseElement):
    """Functionality for the AddressBook navigation menu."""

    def __init__(self, driver):
        super(BaseElement, self).__init__()
        self.driver = driver


    def click_menu_item(self, item_name):
        # import time
        # time.sleep(10)
        self.driver.find_element_by_xpath(
            ELEMENTMAP['menu_item'].format(item_name=item_name)).click()

        # item = self.driver.find_element_by_xpath(
        #     ELEMENTMAP['menu_item'].format(item_name=item_name))
        # if item.isDisplayed:
        #     item.click()
        # else:
        #     WebDriverWait(10).until(item.isDisplayed)

        # item = self.driver.find_element_by_xpath(
        #     ELEMENTMAP['menu_item'].format(item_name=item_name)).click()
        # if self.is_element_visible_by_xpath(item):
        #     item.click()
