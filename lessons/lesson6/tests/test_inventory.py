import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from lessons.lesson6.pages.inventory_page import InventoryPage
from lessons.lesson6.pages.login_page import LoginPage
from time import sleep



class TestInventory:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        yield driver
        driver.quit()

    @pytest.fixture(scope="class")
    def inventory_page(self, driver):
        return InventoryPage(driver)

    @pytest.fixture(scope="class")
    def login_page(self, driver):
        return LoginPage(driver)

    def test_items_amount(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.get_items_amount() == 6, "Количество товаров не совпадает."

    def test_all_items_are_displayed(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_items_are_displayed(), "Не все товары отображаются."

    def test_all_items_names_are_displayed(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_items_names_are_displayed(), "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_item_names_are_not_empty(), "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self, inventory_page, login_page):
        login_page.success_login("standard_user", "secret_sauce")
        assert inventory_page.all_item_names_contains_sauce_labs(), "Не все товары начинаются с 'Sauce Labs'."
    
    def test_prices_compare(self, inventory_page,login_page):
        login_page.success_login("standard_user", "secret_sauce")
        
        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bike Light",
            "Sauce Labs Bolt T-Shirt"
        ]
        
        price_backpack = inventory_page.get_one_price(items[0])
        price_bike_light = inventory_page.get_one_price(items[1])
        price_t_shirt = inventory_page.get_one_price(items[2])
        
        inventory_page.get_item_price_button(1).click()
        inventory_page.get_item_price_button(2).click()
        inventory_page.get_item_price_button(3).click()
        
        
        inventory_page.get_cart_item().click()
        
        cart_price_backpack = inventory_page.get_cart_item_price(3)
        cart_price_bike_light = inventory_page.get_cart_item_price(4)
        cart_price_t_shirt = inventory_page.get_cart_item_price(5)
        
        assert price_backpack == cart_price_backpack, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
        assert price_bike_light == cart_price_bike_light, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
        assert price_t_shirt == cart_price_t_shirt, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
        
        
        
        
        
        
        
#         Открыть сайт SauceDemo.
# Авторизоваться как пользователь standard_user.
# Проверить, что после входа URL страницы равен https://www.saucedemo.com/inventory.html.
# Запомнить цены следующих товаров на странице Inventory:
# Sauce Labs Backpack
# Sauce Labs Bike Light
# Sauce Labs Bolt T-Shirt
# Вывести цены товаров в консоль.
# Добавить эти товары в корзину.
# Перейти в корзину.
# Запомнить цены товаров в корзине.
# Сравнить цены товаров в корзине с ценами на странице Inventory.
# Закрыть браузер.