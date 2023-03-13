from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self, 10)

    def find_element(self, *locator):

        """Finds element"""

        return self.driver.find_element(*locator)

    def click_element(self, *locator):

        """Clicks element"""

        self.find_element(*locator).click()

    def send_text(self, text, *locator):

        """this function sends the text"""

        self.find_element(*locator).send_keys(text)

    def clear_text(self, *locator):

        """For the clear text"""

        self.find_element(*locator).clear()

        return self

    def wait_element(self, method, message=''):

        """Before the clicking item, this function waits."""

        return self.wait.until(ec.element_to_be_clickable(method), message)

    def presence_for_all_elements(self, selector):

        """
        Presence for all elements to present
        selector: locator of the elements to find
        """

        return self.wait.until(ec.presence_of_all_elements_located(selector))

    def presence_for_element(self, selector):

        """
               Presence for element to present
        """

        return self.wait.until(ec.presence_of_element_located(selector))
