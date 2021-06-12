

class TestFindElements:

    def test_find_elements_main_page(self, driver):
        driver.find_element_by_css_selector("input.input-lg")    # search bar
        driver.find_elements_by_css_selector(".swiper-viewport")    # advertising sliders
        driver.find_elements_by_css_selector(".product-layout")[0]    # first product widget
        driver.find_elements_by_xpath("//footer")    # footer
        driver.find_element_by_link_text("About Us")    # link "About us"

    def test_find_elements_catalog_page(self, driver):
        driver.open("/index.php?route=product/category&path=20")
        driver.find_elements_by_css_selector('button[data-toggle=dropdown]')[1]    # Cart
        driver.find_element_by_partial_link_text('Cameras')    # filter "Cameras"
        driver.find_element_by_css_selector('[onclick="cart.add(\'42\', \'2\');"]')   # button "Add to Cart"
        driver.find_element_by_css_selector('[alt="HP Banner"]')    # advertising banner
        driver.find_elements_by_xpath('//footer/div/div/div/ul/li/a')    # link "About us"

    def test_find_elements_product_page(self, driver):
        driver.open("/index.php?route=product/product&path=57&product_id=49")
        driver.find_element_by_css_selector("button#button-cart")    # button "Add to Cart
        driver.find_element_by_css_selector("input#input-quantity")    # input field quantity
        driver.find_element_by_css_selector("[data-original-title=\"Add to Wish List\"]")    # button "Add to Cart"
        driver.find_elements_by_css_selector("div.btn-group > button.btn-default")[0]    # button "Like"
        driver.find_element_by_partial_link_text('OpenCart')    # lint "OpenCart"

    def test_find_elements_login_page(self, driver):
        driver.open("/index.php?route=account/login")
        driver.find_elements_by_css_selector("[placeholder=\"E-Mail Address\"]")   # input field "Email"
        driver.find_elements_by_css_selector("[placeholder=\"Password\"]")    # input field "Password"
        driver.find_elements_by_link_text("Continue")    # button "Continue" to create new customer
        driver.find_elements_by_link_text("Forgotten Password")    # button "Forgotten Password"
        driver.find_elements_by_css_selector("input.btn")    # button "Login"

    def test_find_elements_admin_login_page(self, driver):
        driver.open("/admin/")
        driver.find_elements_by_css_selector("a.navbar-brand")    # title bar
        driver.find_elements_by_css_selector("[placeholder=\"Username\"]")    # input field
        driver.find_elements_by_css_selector("[placeholder=\"Password\"]")    # input field "Password"
        driver.find_elements_by_link_text("Forgotten Password")    # button "Forgotten Password"
        driver.find_elements_by_css_selector("button.btn-primary")    # button "Login"
