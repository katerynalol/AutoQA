from selenium.webdriver.common.by import By
from summary.sum6.pages.base_page import BasePage

class AuthPage(BasePage):
    # Locators
    USER_NAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automationintesting.online/admin"

    def open(self):
        self.driver.get(self.url)


