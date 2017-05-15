from selenium import webdriver

class BaseTest(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

