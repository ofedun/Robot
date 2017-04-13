from selenium import webdriver
import elements as elements
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

HOME_HOST = 'home_host_netloc'


class ChromeWebDriver(object):
    driver_name = "Chrome"

    def __init__(self, user_agent=None, wait_time=2, fullscreen=False,
                 **kwargs):

        options = Options()

        if user_agent is not None:
            options.add_argument("--user-agent=" + user_agent)

        if fullscreen:
            options.add_argument('--kiosk')

        self.driver = Chrome(chrome_options=options, **kwargs)


_DRIVERS = {
    'chrome': ChromeWebDriver
}

class Placeholder(object):
    """Placeholder for page objects."""

def get_browser(options):
    browser = Browser('chrome')
    browser.driver = webdriver.Chrome(chrome_options=options)
    return browser


class DriverNotFoundError(Exception):
    pass


def Browser(driver_name='firefox', *args, **kwargs):
    """
    Returns a driver instance for the given name.

    When working with ``firefox``, it's possible to provide a profile name
    and a list of extensions.

    If you don't provide any driver_name, then ``firefox`` will be used.

    If there is no driver registered with the provided ``driver_name``, this
    function will raise a :class:`splinter.exceptions.DriverNotFoundError`
    exception.
    """

    try:
        driver = _DRIVERS[driver_name]
    except KeyError:
        raise DriverNotFoundError("No driver for %s" % driver_name)
    return driver(*args, **kwargs)

def _add_pages_to_context(context):
    context.pages = Placeholder()
    _add_login_page(context)

def _add_login_page(context):
    context.pages.login_page = pages.LoginPage(
        context.browser,
        'http', HOME_HOST,
        login_form=elements.LoginForm
    )