import pytest
from selenium import webdriver
from homework.hw6.pages.login_page import LoginPage
from homework.hw6.pages.inventory_page import InventoryPage
from homework.hw6.pages.cart_page import CartPage
from homework.hw6.pages.checkout_page import CheckoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class TestSaucedemoPurchase:
    @pytest.fixture(scope="class", autouse=True)
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def login_page(self, driver):
        return LoginPage(driver)

    @pytest.fixture(scope="class", autouse=True)
    def inventory_page(self, driver):
        return InventoryPage(driver)

    @pytest.fixture(scope="class", autouse=True)
    def cart_page(self, driver):
        return CartPage(driver)

    @pytest.fixture(scope="class", autouse=True)
    def checkout_page(self, driver):
        return CheckoutPage(driver)

    def test_checkout_total_price(self, login_page, inventory_page, cart_page, checkout_page):
        login_page.open()
        login_page.success_login("standard_user", "secret_sauce")

        wait = WebDriverWait(inventory_page.driver, 10)

        inventory_page.add_item_to_cart("Sauce Labs Backpack")
        wait.until(
            lambda driver: inventory_page.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text != "0")

        inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        wait.until(
            lambda driver: inventory_page.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text != "1")

        inventory_page.add_item_to_cart("Sauce Labs Onesie")
        wait.until(
            lambda driver: inventory_page.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge").text == "3")

        inventory_page.go_to_cart()

        wait.until(lambda driver: "cart.html" in driver.current_url)

        cart_page.proceed_to_checkout()

        wait.until(lambda driver: "checkout-step-one.html" in driver.current_url)

        checkout_page.enter_first_name("John")
        checkout_page.enter_last_name("Doe")
        checkout_page.enter_postal_code("12345")
        checkout_page.click_on_continue_button()

        total_price = checkout_page.get_total_price()
        assert total_price == "Total: $58.29", f"Итоговая сумма неверна: {total_price}"