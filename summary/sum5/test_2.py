from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from lessons.lesson1.without_fixture.test_calculator import calc


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_troll_panel(driver):
    driver.get("http://suninjuly.github.io/redirect_accept.html")
    panel = driver.find_element(By.CLASS_NAME, "trollface")
    panel.click()
    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)
    x_value = driver.find_element(By.ID, "input_value").text
    result = calc(x_value)
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()
    sleep(5)