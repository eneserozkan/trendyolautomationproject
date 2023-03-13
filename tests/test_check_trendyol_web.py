import time

from pages.basket_page import BasketPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestCheckTrendyolWeb(BaseTest):
    valid_mail = "e******89@gmail.com"
    valid_password = "8*******"
    search_product = "ayakkabı"

    def test_check_trendyol_web(self):
        home_page = HomePage(self.driver)
        home_page.close_pop_up()
        home_page.accept_cookie()
        assert home_page.is_on_home_page(), "Not on home page!"
        home_page.click_login_button()

        login_page = LoginPage(self.driver)
        login_page.fill_email_textbook(self.valid_mail)
        login_page.fill_password_box(self.valid_password)
        login_page.click_login_button()
        assert login_page.is_on_logged(), "It is not correct"
        time.sleep(6)

        product_page = ProductPage(self.driver)
        product_page.fill_search_box(self.search_product)
        product_page.click_search_button()
        assert product_page.is_on_product_page(), "It is not equal item that you searched."
        product_page.click_third_product()
        basket_page = BasketPage(self.driver)
        self.assertEqual(product_page.product_text(), basket_page.product_title_in_basket(), "It is not equal.")
        product_page.add_to_basket()

        basket_page.click_basket()
        assert basket_page.check_item_counts(), "The count is uncorrect."
        basket_page.click_delete_item()

        def tearDown(self):
            self.driver.quit()
