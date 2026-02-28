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
    driver.get("http://www.uitestingplayground.com/")
    yield driver
    driver.quit()


def test_load_delay(driver):
    load_delay_link = driver.find_element(By.LINK_TEXT, "Load Delay")
    wait = WebDriverWait(driver, 10)
    load_delay_link.click()

    btn = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))

    assert btn.is_displayed()