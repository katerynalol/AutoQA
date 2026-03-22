from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
        )

    def get_cart_item(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.shopping_cart_link"))
        )

    def add_item_to_cart(self, item_name):
        items = self.get_items()

        for item in items:
            name_element = item.find_element(By.CLASS_NAME, "inventory_item_name")
            if name_element.text == item_name:
                add_button = item.find_element(By.CLASS_NAME, "btn_inventory")
                add_button.click()
                break

    def go_to_cart(self):
        cart_element = self.get_cart_item()
        self.driver.execute_script("arguments[0].click();", cart_element)