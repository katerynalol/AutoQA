from time import sleep
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# def test_login(driver):
#     driver.get("https://the-internet.herokuapp.com/login")
#     but_username = driver.find_element(By.ID, "username")
#     but_username.send_keys("tomsmith")
#     # sleep(2)
#
#     but_password = driver.find_element(By.ID, "password")
#     but_password.send_keys("SuperSecretPassword!")
#     # sleep(5)
#
#     but_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
#     but_submit.click()
#     sleep(2)
#
#     assert "https://the-internet.herokuapp.com/secure" in driver.current_url
#
#     text_info = driver.find_element(By.ID, "flash")
#     # assert text_info.text == "You logged into a secure area!\n×"
#     assert "You logged into a secure area!" in text_info.text


def test_wrong_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    but_username = driver.find_element(By.ID, "username")
    but_username.send_keys("tomsmith")
    sleep(2)

    but_password = driver.find_element(By.ID, "password")
    but_password.send_keys("qwerty")
    sleep(2)

    button_sub = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_sub.click()
    sleep(2)
    assert "https://the-internet.herokuapp.com/login" in driver.current_url








