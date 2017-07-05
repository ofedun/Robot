from selenium import webdriver

def singleton(class_):
  instances = {}
  def getinstance(*args, **kwargs):
    if class_ not in instances:
        instances[class_] = class_(*args, **kwargs)
    return instances[class_]
  return getinstance

@singleton
class Browser(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def close_browser(self):
        """Quit browser."""
        # self.driver.close()
        self.driver.quit()
