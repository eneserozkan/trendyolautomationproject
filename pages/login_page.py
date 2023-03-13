from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_BOX = (By.ID, "login-email")
    PASSWORD_BOX = (By.ID, "login-password-input")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-register > div.lr-container > div.q-layout.login > form > button")
    valid_login = (By.CLASS_NAME, "user-name")

    def fill_email_textbook(self, email):

        """Fill email box with the mail that the user used"""

        self.clear_text(*self.EMAIL_BOX).send_text(email, *self.EMAIL_BOX)

    def fill_password_box(self, password):

        """ Fill the password"""

        self.send_text(password, *self.PASSWORD_BOX)

    def click_login_button(self):

        """ Click sign in button"""

        self.click_element(*self.LOGIN_BUTTON)

    def is_on_logged(self):

        """Assert whether the user logs in or not."""

        return self.presence_for_element(self.valid_login).text == "Enes Erözkan"
