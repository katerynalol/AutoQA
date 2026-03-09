import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_hover_menu(driver):
    url = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"
    driver.get(url)

    all_text = driver.find_element(By.ID, "my-iframe")
    search_text = "semper posuere integer et senectus justo curabitur."

    driver.switch_to.frame(all_text)
    element = driver.find_element(By.TAG_NAME, "body")

    assert search_text in element.text