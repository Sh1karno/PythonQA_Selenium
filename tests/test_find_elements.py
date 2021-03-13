

class TestFindElements:

    def test_find_elements_main_page(self, browser):
        browser.find_element_by_css_selector("input.input-lg")    # search bar
        browser.find_elements_by_css_selector(".swiper-viewport")    # advertising sliders
        browser.find_elements_by_css_selector(".product-layout")[0]    # first product widget
        browser.find_elements_by_xpath("//footer")    # footer
        browser.find_element_by_link_text("About Us")    # link "About us"

    def test_find_elements_catalog_page(self, browser):
        browser.get(browser.url + "/index.php?route=product/category&path=20")
        browser.find_elements_by_css_selector('button[data-toggle=dropdown]')[1]    # Cart
        browser.find_element_by_partial_link_text('Cameras')    # filter "Cameras"
        browser.find_element_by_css_selector('[onclick="cart.add(\'42\', \'2\');"]')   # button "Add to Cart"
        browser.find_element_by_css_selector('[alt="HP Banner"]')    # advertising banner
        browser.find_elements_by_xpath('//footer/div/div/div/ul/li/a')    # link "About us"

    def test_find_elements_product_page(self, browser):
        browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")
        browser.find_element_by_css_selector("button#button-cart")    # button "Add to Cart
        browser.find_element_by_css_selector("input#input-quantity")    # input field quantity
        browser.find_element_by_css_selector("[data-original-title=\"Add to Wish List\"]")    # button "Add to Cart"
        browser.find_elements_by_css_selector("div.btn-group > button.btn-default")[0]    # button "Like"
        browser.find_element_by_partial_link_text('OpenCart')    # lint "OpenCart"

    def test_find_elements_login_page(self, browser):
        browser.get(browser.url + "/index.php?route=account/login")
        browser.find_elements_by_css_selector("[placeholder=\"E-Mail Address\"]")   # input field "Email"
        browser.find_elements_by_css_selector("[placeholder=\"Password\"]")    # input field "Password"
        browser.find_elements_by_link_text("Continue")    # button "Continue" to create new customer
        browser.find_elements_by_link_text("Forgotten Password")    # button "Forgotten Password"
        browser.find_elements_by_css_selector("input.btn")    # button "Login"

    def test_find_elements_admin_login_page(self, browser):
        browser.get(browser.url + "/admin/")
        browser.find_elements_by_css_selector("a.navbar-brand")    # title bar
        browser.find_elements_by_css_selector("[placeholder=\"Username\"]")    # input field
        browser.find_elements_by_css_selector("[placeholder=\"Password\"]")    # input field "Password"
        browser.find_elements_by_link_text("Forgotten Password")    # button "Forgotten Password"
        browser.find_elements_by_css_selector("button.btn-primary")    # button "Login"
