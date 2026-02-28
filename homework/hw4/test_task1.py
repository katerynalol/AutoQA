import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()


def test_button_text_change(driver):
    text_box = driver.find_element(By.CLASS_NAME, "form-control")
    text_box.send_keys("ITCH")

    submit_button = driver.find_element(By.CLASS_NAME, "btn-primary")
    submit_button.click()

    assert submit_button.text == "ITCH"