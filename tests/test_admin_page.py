import allure


class TestAdminPage:

    @allure.title("Failed login to admin page")
    def test_failed_login(self, driver, url, admin_page):
        """ Description """
        with allure.step(f'Browser opened on {url}{admin_page.PATH}'):
            driver.open(admin_page.PATH)
        with allure.step(f'Trying to login without password'):
            admin_page.login_admin("user", "")
        assert admin_page.display_warning_text() == \
            "No match for Username and/or Password.\n×"

    @allure.title("Success login to admin page")
    def test_passed_login(self, browser, url, admin_page):
        """ Description """
        with allure.step(f'Browser opened on {url}{admin_page.PATH}'):
            browser.open(admin_page.PATH)
        with allure.step(f'Trying to login without password'):
            admin_page.login_admin("user", "bitnami")
        assert admin_page.display_admin_name() == \
            'John Doe'

    @allure.title("Open product table in admin page")
    def test_open_product_table(self, driver, url,  admin_page):
        """ Description """
        with allure.step(f'Browser opened on {url}{admin_page.PATH}'):
            driver.open(admin_page.PATH)
        admin_page \
            .login_admin("user", "bitnami") \
            .click_to_catalog_menu_item() \
            .click_to_products_catalog_item() \
            .display_product_table()
