from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class ProductPage(BasePage):
    SEARCH_BOX = (By.CLASS_NAME, "V8wbcUhU")
    SEARCH_BUTTON = (By.CLASS_NAME, "cyrzo7gC")
    THIRD_PRODUCT = (By.XPATH, "//*[@id='search-app']/div/div[1]/div[2]/div[3]/div[1]/div/div[4]/div[1]/a/div[1]")
    PRODUCT_TITLE = (
    By.XPATH, "//*[@id='search-app']/div/div[1]/div[2]/div[3]/div[1]/div/div[4]/div[1]/a/div[2]/div[1]/div/div/span[2]")
    ADD_TO_BASKET = (By.CLASS_NAME, "add-to-basket")
    product_page_check = (By.XPATH, "//*[@class='dscrptn']")
    title = (By.XPATH, "//*[@class='srch-rslt-title']")

    def fill_search_box(self, name):

        """Search for keyword via the search box"""

        self.send_text(name, *self.SEARCH_BOX)

    def click_search_button(self):

        """Click search button."""

        self.click_element(*self.SEARCH_BUTTON)

    def click_third_product(self):

        """ Select third product on product page. """

        self.click_element(*self.THIRD_PRODUCT)

    def add_to_basket(self):

        """ The item is added in the basket"""

        self.click_element(*self.ADD_TO_BASKET)

    def product_text(self):

        """It takes the text of product for the assertion"""

        return self.find_element(self.PRODUCT_TITLE).text

    def is_on_product_page(self):

        """Check the user is on product page"""

        return self.presence_for_element(self.product_page_check).text == self.presence_for_element(self.title).text
