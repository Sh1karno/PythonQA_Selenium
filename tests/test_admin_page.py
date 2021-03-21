from PageObject.admin_page import AdminPage


class TestAdminPage:

    def test_failed_login(self, browser):
        browser.open(AdminPage.PATH)
        AdminPage(browser).login_admin("user", "")
        assert AdminPage(browser).display_warning_text() == \
            "No match for Username and/or Password.\n×"

    def test_passed_login(self, browser):
        browser.open(AdminPage.PATH)
        AdminPage(browser).login_admin("user", "bitnami")
        assert AdminPage(browser).display_admin_name() == \
            'John Doe'

    def test_open_product_table(self, browser):
        browser.open(AdminPage.PATH)
        AdminPage(browser) \
            .login_admin("user", "bitnami") \
            .click_to_catalog_menu_item() \
            .click_to_products_catalog_item() \
            .display_product_table()
