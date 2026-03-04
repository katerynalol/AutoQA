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


def test_drag_and_drop(browser):
    url = "https://crossbrowsertesting.github.io/drag-and-drop.html"
    browser.get(url)

    draggable_element = browser.find_element(By.ID, 'draggable')
    drop_location = browser.find_element(By.ID, 'droppable')

    actions = ActionChains(browser)
    actions.drag_and_drop(draggable_element, drop_location).perform()
    # sleep(3)
    dropped_text = browser.find_element(By.CSS_SELECTOR, "#droppable > p")
    assert dropped_text.text == "Dropped!"