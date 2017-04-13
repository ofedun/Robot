from Selenium2Library import Selenium2Library

class BasePage(object):
    """Base for the Page objects.

    Provides shared functionality for Page objects.
    """
    def __init__(self):
        self.browser = Selenium2Library()


    def visit(self, target_url=None):
        """Go to pages URL."""
        target_url = target_url
        self.browser.open_browser(target_url)

