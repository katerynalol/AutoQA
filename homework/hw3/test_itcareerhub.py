from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    # sleep(5)
    yield driver
    driver.quit()


def test_logo(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")

    assert logo.is_displayed()


def test_programs_link(driver):
    programs_button = driver.find_element(By.XPATH, "//span[text()='Программы']")
    programs_button.click()
    # sleep(2)
    course_item = driver.find_element(By.XPATH, "//div[contains(text(), 'Python-разработчик')]")

    assert course_item.is_displayed()
    assert course_item.text == "Python-разработчик"


def test_payment_method(driver):
    payment_link = driver.find_element(By.XPATH, "//span[text()='Способы оплаты']")
    payment_link.click()
    # sleep(2)
    target_header = driver.find_element(By.XPATH,"//*[contains(text(), 'Помогаем подобрать подходящий способ оплаты')]")

    assert target_header.is_displayed(), "Страница не прокрутилась к способам оплаты"


def test_about_us(driver):
    about_us = driver.find_element(By.XPATH, "//span[text()='О нас']")
    about_us.click()
    # sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    assert "https://itcareerhub.de/ru/o-nas" in driver.current_url


def test_reviews(driver):
    about_us = driver.find_element(By.XPATH, "//span[text()='Отзывы']")
    about_us.click()
    # sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    assert "https://itcareerhub.de/reviews" in driver.current_url


def test_language_switch(driver):
    de_button = driver.find_element(By.LINK_TEXT, "de")
    de_button.click()
    sleep(2)
    assert driver.current_url == "https://itcareerhub.de/"

    ru_button = driver.find_element(By.LINK_TEXT, "ru")
    ru_button.click()
    sleep(2)
    assert driver.current_url == "https://itcareerhub.de/ru"
