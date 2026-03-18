from selenium.webdriver.common.by import By
from summary.sum6.pages.base_page import BasePage


class ContactPage(BasePage):
    # Locators
    NAME_FIELD = (By.ID, "name")
    LOCATION_INFO = (By.CSS_SELECTOR, ".card-body h4 + p")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationintesting.online/#contact"

    def open(self):
        self.driver.get(self.url)