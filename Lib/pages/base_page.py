from selenium import webdriver
from selenium.webdriver import Chrome, Remote
import sys

GLOBALTIMEOUT = 10

class BasePage(object):
    """Base for the Page objects.

    Provides shared functionality for Page objects.
    """
    def __init__(self, url, browser='Chrome'):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver
        self.url = url

        def attach(session_id, session_url):
            driver = webdriver.Remote(command_executor=session_url, desired_capabilities={'browserName': 'chrome'})
            driver.session_id = session_id

        session_url = self.driver.command_executor._url
        session_id = self.driver.session_id
        if session_id is None:
            self.driver = webdriver.Chrome()
        else:
            attach(session_id, session_url)



        # def open():
        #     driver = Chrome()
        #     print("%s  %s" % (driver.session_id, driver.command_executor._url))
        #
        # def attach(sid, url):
        #     driver = Remote(command_executor=url, desired_capabilities={})
        #     driver.session_id = sid
        #     driver.find_element_by_xpath("//input[contains(@value, 'Lucky')]").click()
        #
        # sid = sys.argv[1] if len(sys.argv) > 1 else None
        # url = sys.argv[2] if len(sys.argv) > 2 else None
        #
        # if sid is None:
        #     open()
        # else:
        #     attach(sid, url)



        # if (driver.toString().contains("null"))

        # if selenium webdriver exists:
        #     self.driver = find_existent_instance_of_webdriver()
        # else:
        #     self.driver = webdriver.Chrome()


    def visit(self, url=None, browser='Chrome'):
        """Go to pages URL."""
        target_url = url
        self.driver.get(target_url)
        import time
        time.sleep(10)
