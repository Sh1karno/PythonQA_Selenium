import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from selenium.webdriver.support.wait import WebDriverWait


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


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], help="Browser")
    parser.addoption("--url", action="store", default="http://localhost", help="This is opened url")
    parser.addoption("--no_headless", action="store_true", help="off headless option")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    headless = request.config.getoption("--no_headless")

    driver = None

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = False
        else:
            options.headless = True
        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = False
        else:
            options.headless = True
        driver = webdriver.Firefox(options=options)

    elif browser == "opera":
        options = OperaOptions()
        # headless mode is not supported by Opera browser
        driver = webdriver.Opera(options=options)

    def browser_close():
        driver.close()

    driver.maximize_window()

    driver.get(url)
    driver.url = url

    request.addfinalizer(browser_close)

    return driver


@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 3)

