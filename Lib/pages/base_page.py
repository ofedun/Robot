from Selenium2Library import Selenium2Library


# create new class that inherits from Selenium2Library
class CustomSeleniumLibrary(Selenium2Library):
    # create a new keyword called "get webdriver instance"
    def get_webdriver_instance(self):
        return self._current_browser()


class BasePage(object):
    """Base for the Page objects.

    Provides shared functionality for Page objects.
    """
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url=None, browser='Chrome'):
        """Go to pages URL."""
        target_url = url
        self.driver.get(target_url)
