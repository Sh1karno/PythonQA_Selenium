from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestAdminPage:

    def test_failed_login(self, browser, wait):
        browser.get(browser.url + "/admin/")

        username_field = browser.find_element_by_css_selector("[placeholder=\"Username\"]")
        username_field.send_keys("user")

        password_field = browser.find_element_by_css_selector("[placeholder=\"Password\"]")
        password_field.send_keys("")

        login_button = browser.find_element_by_css_selector("button.btn-primary")
        login_button.click()

        alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert")))
        assert alert.text == "No match for Username and/or Password.\n×"

    def test_passed_login(self, browser, wait):
        browser.get(browser.url + "/admin/")

        username_field = browser.find_element_by_css_selector("[placeholder=\"Username\"]")
        username_field.send_keys("user")

        password_field = browser.find_element_by_css_selector("[placeholder=\"Password\"]")
        password_field.send_keys("bitnami")

        login_button = browser.find_element_by_css_selector("button.btn-primary")
        login_button.click()

        john = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.dropdown-toggle")))
        assert john.text == 'John Doe'

    def test_open_product_table(self, browser, wait):
        browser.get(browser.url + "/admin/")

        username_field = browser.find_element_by_css_selector("[placeholder=\"Username\"]")
        username_field.send_keys("user")

        password_field = browser.find_element_by_css_selector("[placeholder=\"Password\"]")
        password_field.send_keys("bitnami")

        login_button = browser.find_element_by_css_selector("button.btn-primary")
        login_button.click()

        catalog = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[href=\"#collapse1\"]")))
        catalog.click()

        products = wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Products")))
        products.click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-product")))
