import logging
import os

from datetime import datetime
from selenium.webdriver.support.events import AbstractEventListener


class Listener(AbstractEventListener):

    test_name = None

    def on_exception(self, exception, driver):
        screenshot_name = f'screenshots/exception_{self.test_name}_{datetime.now().strftime("%Y-%m-%d_%H%M%S")}.png'
        os.makedirs(os.path.dirname(screenshot_name), exist_ok=True)
        logging.error(f'EXCEPTION!: {exception}')
        driver.save_screenshot(screenshot_name)
