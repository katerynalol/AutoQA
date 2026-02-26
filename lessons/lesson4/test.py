import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculation(driver):
    input_7 = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(1)")
    input_7.click()

    input_plus = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(4))")
    input_plus.click()

    input_8 = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span:nth-child(2)")
    input_8.click()

    input_equal = driver.find_element(By.CSS_SELECTOR, "#calculator > div.keys > span.btn.btn-outline-warning")
    input_equal.click()

    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#calculator > div.top > div"), 15))

    assert element