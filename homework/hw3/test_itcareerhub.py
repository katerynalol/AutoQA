from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    sleep(5)
    yield driver
    driver.quit()


def test_logo_is_displayed(driver):
    logo = driver.find_element(By.CSS_SELECTOR, "img[alt='IT Career Hub']")

    assert logo.is_displayed()


def test_program_link_is_clickable(driver):
    programs_button = driver.find_element(By.LINK_TEXT, "Программы")
    programs_button.click()
    # sleep(2)
    course_item = driver.find_element(By.LINK_TEXT, "Python-разработчик")

    assert course_item.is_displayed()
    assert course_item.text == "Python-разработчик"


def test_payment_method_link_navigation(driver):
    payment_link = driver.find_element(By.CSS_SELECTOR, "a[href*='rec1921734713'].tn-atom")
    payment_link.click()
    sleep(2)
    target_section = driver.find_element(By.ID, "rec1921734713")

    assert target_section.is_displayed()


def test_about_us_link(driver):
    about_us = driver.find_element(By.CSS_SELECTOR, "a[href='/ru/o-nas'].tn-atom")
    about_us.click()
    # sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    assert "https://itcareerhub.de/ru/o-nas" in driver.current_url


def test_reviews_link_opens_in_new_window(driver):
    reviews = driver.find_element(By.CSS_SELECTOR, "a[href='/reviews'].tn-atom")
    reviews.click()
    # sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    assert "https://itcareerhub.de/reviews" in driver.current_url


def test_language_switch_for_de(driver):
    de_button = driver.find_element(By.LINK_TEXT, "de")
    de_button.click()
    sleep(2)
    assert driver.current_url == "https://itcareerhub.de/"

    headline = driver.find_element(By.TAG_NAME, "h1")
    assert headline.text == "Erwerben Sie einen gefragten IT-Beruf und starten Sie Ihre Karriere in Deutschland"

    ru_button = driver.find_element(By.LINK_TEXT, "ru")
    ru_button.click()
    sleep(2)
    assert driver.current_url == "https://itcareerhub.de/ru"

    headline = driver.find_element(By.TAG_NAME, "h1")
    assert headline.text == "Начните IT карьеру в Германии"
