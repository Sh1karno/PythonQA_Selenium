import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(type(self).__name__)

    def __element(self, selector: dict, index: int):
        by = None
        if 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)[index]

    def _click(self, selector, index=0):
        self.logger.info(f"Clicking element: {selector}")
        ActionChains(self.driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        self.logger.info(f"Input {value} in input {selector}")
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, index=0, wait=3):
        self.logger.info(f"Element {selector} has become visible")
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self.__element(selector, index)))
