import pytest
import logging

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.events import EventFiringWebDriver
from listener import Listener


logging.basicConfig(level=logging.INFO,
                    format="'%(asctime)s %(levelname)s %(filename)s %(message)s'",
                    filename="logs/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     choices=["chrome", "firefox", "opera"],
                     help="Choice browser")
    parser.addoption("--url",
                     action="store",
                     default="http://localhost",
                     help="This is opened url")
    parser.addoption("--headless",
                     action="store_true",
                     help="Off headless option")


@pytest.fixture(scope="session", autouse=True)
def set_time_testrun():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print('\nTEST-RUN RUNTIME:', end_time - start_time)


@pytest.fixture(scope="function", autouse=True)
def set_time_test():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print(' | test-case runtime:', end_time - start_time)


@pytest.fixture(scope="function")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="function")
def browser(request, url):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    logger = logging.getLogger('BrowserLogger')

    test_name = request.node.name
    logger.info(f"===== Test {test_name} started =====")

    listener = Listener()
    listener.test_name = test_name

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if not headless:
            options.headless = True
        driver = EventFiringWebDriver(webdriver.Chrome(options=options), listener)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if not headless:
            options.headless = True
        driver = EventFiringWebDriver(webdriver.Firefox(options=options), listener)
    elif browser == "opera":
        options = OperaOptions()
        # headless mode is not supported by Opera browser
        driver = EventFiringWebDriver(webdriver.Opera(options=options), listener)

    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info(f"===== Test {test_name} finished =====")

    request.addfinalizer(fin)

    logger.info(f"Browser {browser} started with {driver.desired_capabilities}")

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()

    return driver

