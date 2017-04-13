class BasePage(object):
    """Base for the Page objects.

    Provides shared functionality for Page objects.
    """
    def __init__(self, driver):
        self.browser = driver


    def visit(self, target_url=None):
        """Go to pages URL."""
        target_url = target_url
        self.browser.visit(target_url)

