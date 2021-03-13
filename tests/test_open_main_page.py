

def test_main_page(browser):
    logo = browser.find_element_by_css_selector("#logo")
    assert logo.text == "Your Store"

