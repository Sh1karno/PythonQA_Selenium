from .base_page import BasePage


class AdminPage(BasePage):
    """Страница администратора"""

    PATH = "/admin/"

    USERNAME_FIELD = {'css': "[placeholder=\"Username\"]"}
    PASSWORD_FIELD = {'css': "[placeholder=\"Password\"]"}
    LOGIN_BUTTON = {'css': "button.btn-primary"}
    WARNING_MESSAGE = {'css': "div.alert"}
    ADMIN_NAME = {'css': "a.dropdown-toggle"}
    CATALOG_MENU_ITEM = {'css': "[href=\"#collapse1\"]"}
    PRODUCTS_TABLE = {'css': "#form-product"}
    PRODUCTS_CATALOG_ITEM = {'css': "#collapse1>li.active>a"}

    def login_admin(self, username, password):
        self._input(self.USERNAME_FIELD, username)
        self._input(self.PASSWORD_FIELD, password)
        self._click(self.LOGIN_BUTTON)
        return self

    def display_warning_text(self):
        return self._wait_for_visible(self.WARNING_MESSAGE).text

    def display_admin_name(self):
        return self._wait_for_visible(self.ADMIN_NAME).text

    def click_to_catalog_menu_item(self):
        self._wait_for_visible(self.CATALOG_MENU_ITEM).click()
        return self

    def click_to_products_catalog_item(self):
        self._wait_for_visible(self.PRODUCTS_CATALOG_ITEM).click()
        return self

    def display_product_table(self):
        return self._wait_for_visible(self.PRODUCTS_TABLE)
