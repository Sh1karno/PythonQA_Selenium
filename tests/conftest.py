import pytest

from PageObject.admin_page import AdminPage


@pytest.fixture(scope="function")
def admin_page(browser):
    return AdminPage(browser)
