from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class BasketPage(BasePage):
    BASKET = (By.CLASS_NAME, "link-text")
    PRODUCT_COUNT = (By.CLASS_NAME, "counter-content")
    DELETE_ITEM = (By.CLASS_NAME, "i-trash")
    ITEM_TITLE = (By.CLASS_NAME, "pr-new-br")
    check_item_count = (By.CLASS_NAME, "counter-content")

    def click_basket(self):
        self.presence_for_all_elements(self.BASKET)[2].click()

    def product_title_in_basket(self):
        return self.click_element(*self.ITEM_TITLE).text

    def click_delete_item(self):
        self.click_element(*self.DELETE_ITEM)

    def check_item_counts(self):
        return self.presence_for_element(self.check_item_count).text == "1"








