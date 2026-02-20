from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://suninjuly.github.io/cats.html")
    yield driver
    driver.quit()

def test_title_cats(driver):
    headline = driver.find_element(By.TAG_NAME, "h1")
    assert headline.text == "Cat memes"


def test_title_of_card1(driver):
    time_card = driver.find_element(By.CSS_SELECTOR, "[class='col-sm-4']:nth-child(1) [class='text-muted']")
    assert time_card.text == "9 mins"

def test_of_text_search(driver):
    text_card = driver.find_element(By.CSS_SELECTOR, "[class='col-sm-4']:nth-child(6) p")
    assert text_card.text == "I love you so much"

def test_is_display(driver):
    card = driver.find_element(By.CSS_SELECTOR,  "[class='col-sm-4']:nth-child(2)")
    # assert card.is_displayed()
    print(card.is_displayed())

def test_count_cards(driver):
    cards = driver.find_elements(By.CLASS_NAME, 'card')
    assert len(cards) == 6

def test_count_img(driver):
    img = driver.find_elements(By.TAG_NAME, 'img') # (By.CLASS_NAME, 'card-img-top')
    assert len(img) == 6