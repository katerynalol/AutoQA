import pytest
from selenium import webdriver
from summary.sum6.pages.contact_page import ContactPage


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.contact_page = ContactPage(driver)

    yield
    driver.quit()