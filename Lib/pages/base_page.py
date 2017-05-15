# from selenium import webdriver
# from selenium.webdriver import Chrome, Remote
#
#
# GLOBALTIMEOUT = 10
#
# class BasePage(object):
#     """Base for the Page objects.
#
#     Provides shared functionality for Page objects.
#     """
#     def __init__(self, browser='Chrome'):
#         self.driver = webdriver
#
#         def attach(session_id, session_url):
#             driver = webdriver.Remote(command_executor=session_url, desired_capabilities={'browserName': 'chrome'})
#             driver.session_id = session_id
#
#         if not hasattr(self.driver, 'session_id'):
#             self.driver = webdriver.Chrome()
#         else:
#             session_id = self.driver.session_id
#             session_url = self.driver.command_executor._url
#             attach(session_id, session_url)
#
#     def visit(self, url=None, browser='Chrome'):
#         """Go to pages URL."""
#         target_url = url
#         self.driver.get(target_url)
#         # import time
#         # time.sleep(10)


from Selenium2Library import Selenium2Library
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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

