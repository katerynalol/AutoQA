from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hover_menu(browser):
    url = "https://crossbrowsertesting.github.io/hover-menu.html"
    browser.get(url)

    actions = ActionChains(browser)

    dropdown_link = browser.find_element(By.CSS_SELECTOR, '[class="dropdown"] > [class="dropdown-toggle"]')
    actions.move_to_element(dropdown_link).perform()

    # sleep(3)

    secondary_menu = browser.find_element(By.LINK_TEXT, "Secondary Menu")
    actions.move_to_element(secondary_menu).perform()

    secondary_action = browser.find_element(By.LINK_TEXT, "Secondary Action")
    secondary_action.click()


    title = browser.find_element(By.CSS_SELECTOR, '[class="jumbotron secondary-clicked"] h1')
    assert title.text == "Secondary Page"