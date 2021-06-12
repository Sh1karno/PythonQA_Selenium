import pytest
import logging
import os

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
                     action="store", choices=["chrome", "firefox", "opera"], default="firefox", help="Choice browser")
    parser.addoption("--url",
                     action="store", default="localhost", help="This is opened url")
    parser.addoption("--headless",
                     action="store_true", default=False, help="Off headless option")
    parser.addoption("--executor",
                     action="store", default="localhost", help="Choice executor, \"local\" to run local drivers")
    parser.addoption("--bversion",
                     action="store", help="Choice browser version")
    parser.addoption("--vnc",
                     action="store_true", default=False, help="Enable video translation")
    parser.addoption("--logs",
                     action="store_true", default=False, help="Enable logging")
    parser.addoption("--videos",
                     action="store_true", default=False, help="Enable video recording")


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


@pytest.fixture(scope="session")
def browser(request):
    browser = request.config.getoption("--browser")
    return browser


@pytest.fixture(scope="session")
def url(request):
    url = f'http://{request.config.getoption("--url")}'
    return url


@pytest.fixture(scope="session")
def bversion(request):
    bversion = request.config.getoption("--bversion")
    return bversion


@pytest.fixture(scope="session")
def executor(request):
    executor = request.config.getoption("--executor")
    return executor


@pytest.fixture(scope="function")
def driver(request, url, executor, bversion, browser):
    headless = request.config.getoption("--headless")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    logger = logging.getLogger('BrowserLogger')

    test_name = request.node.name

    listener = Listener()
    listener.test_name = test_name

    driver = None

    if executor == "local":
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = EventFiringWebDriver(webdriver.Chrome(options=options), listener)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = EventFiringWebDriver(webdriver.Firefox(options=options), listener)
        elif browser == "opera":
            options = OperaOptions()
            # headless mode is not supported by Opera browser
            driver = EventFiringWebDriver(webdriver.Opera(options=options), listener)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"

        caps = {
            "browserName": browser,
            "browserVersion": bversion,
            "name": "Opencard tests",
            "selenoid:options": {
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            },
            'acceptSslCerts': True,
            'acceptInsecureCerts': True,
            'timeZone': 'Europe/Moscow',
            'goog:chromeOptions': {}
        }

        driver = webdriver.Remote(
            command_executor=executor_url,
            desired_capabilities=caps
        )

    driver.maximize_window()
    logger.info(f"Browser {browser} started with {driver.desired_capabilities}")

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    logger.info(f"===== Test {test_name} started =====")
    driver.open()

    def fin():
        driver.quit()
        logger.info(f"===== Test {test_name} finished =====")

    request.addfinalizer(fin)

    return driver


@pytest.fixture(scope="session", autouse=True)
def allure_enviroment(browser, bversion, executor):
    filename = "allure-results/environment.properties"
    data = f"Browser={browser}\nBrowser.Version={bversion}\nStand={executor}"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as file:
        file.write(data)
