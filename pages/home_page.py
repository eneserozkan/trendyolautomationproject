from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class HomePage(BasePage):
    GIRIS_BUTTON = (By.CSS_SELECTOR , "#account-navigation-container > div > div.account-nav-item.user-login-container")
    CLOSE_POPUP = (By.CLASS_NAME, "modal-close")
    ACCEPT_COOKIES = (By.ID, "onetrust-accept-btn-handler")
    home_page_check = (By.XPATH, "//*[@id='logo']")

    def close_pop_up(self):

        """
        It closes the pop-up you faced.
        """
        self.click_element(*self.CLOSE_POPUP)

    def accept_cookie(self):

        """This function accepts the cookies. """

        self.click_element(*self.ACCEPT_COOKIES)

    def click_login_button(self):

        """Clicks login button."""

        self.click_element(*self.GIRIS_BUTTON)

    def is_on_home_page(self):

        """Assert whether it is on homepage or not."""

        return self.presence_for_element(self.home_page_check).text == 'trendyol'