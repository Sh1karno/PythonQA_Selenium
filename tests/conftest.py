import pytest

from PageObject.admin_page import AdminPage


@pytest.fixture(scope="function")
def admin_page(driver):
    return AdminPage(driver)
