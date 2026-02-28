import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service





@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    yield driver
    driver.quit()


def test_VAlid_NA(driver):
    input_zip = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
    input_zip.send_keys('luboy text')
    input_first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
    button_sub = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    button_sub.click()
    input_zip_id = driver.find_element(By.ID,'zip-code')
    input_first_name_id = driver.find_element(By.ID, 'first-name')
    assert input_first_name_id.text=="N/A"
    assert input_zip_id.text=="luboy text"