import pytest
from selenium import webdriver
from pages.contact_page import ContactPage
from pages.auth_page import AuthPage

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.contact_page = ContactPage(driver)
    request.cls.auth_page = AuthPage(driver)
    yield
    driver.quit()