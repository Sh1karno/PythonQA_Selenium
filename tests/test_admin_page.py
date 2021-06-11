from PageObject.admin_page import AdminPage


class TestAdminPage:

    def test_failed_login(self, browser, admin_page):
        browser.open(admin_page.PATH)
        admin_page.login_admin("user", "")
        assert admin_page.display_warning_text() == \
            "No match for Username and/or Password.\n×"

    def test_passed_login(self, browser, admin_page):
        browser.open(admin_page.PATH)
        admin_page.login_admin("user", "bitnami")
        assert admin_page.display_admin_name() == \
            'John Doe'

    def test_open_product_table(self, browser, admin_page):
        browser.open(admin_page.PATH)
        admin_page \
            .login_admin("user", "bitnami") \
            .click_to_catalog_menu_item() \
            .click_to_products_catalog_item() \
            .display_product_table()
