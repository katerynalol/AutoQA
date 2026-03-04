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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    yield driver
    driver.quit()


def test_image_upload(driver):
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.ID, "landscape")))

    image_container = driver.find_element(By.ID, "image-container")
    images = image_container.find_elements(By.TAG_NAME, "img")
    image_3 = images[2]

    alt_value = image_3.get_attribute("alt")

    # images = driver.find_elements(By.TAG_NAME, "img")
    # image_3 = images[3]
    #
    # alt_value = image_3.get_attribute("alt")

    assert alt_value == "award"