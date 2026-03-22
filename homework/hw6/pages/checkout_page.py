from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def get_first_name_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))

    def get_last_name_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "last-name")))

    def get_postal_code_input(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, "postal-code")))

    def get_continue_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))

    def enter_first_name(self, first_name):
        first_name_field = self.get_first_name_input()
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.get_last_name_input()
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        postal_code_field = self.get_postal_code_input()
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def click_on_continue_button(self):
        self.get_continue_button().click()

    def get_total_price(self):
        return self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text