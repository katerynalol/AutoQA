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


def test_file_upload(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    upload = browser.find_element(By.ID, "file-upload")
    upload.send_keys("E:\\Work\\autoqa\\lesson5\key.jpg")

    button_upload = browser.find_element(By.ID, "file-submit")
    button_upload.click()

    sleep(5)