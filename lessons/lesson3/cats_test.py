import pytest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.devtools.v135.debugger import pause


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_check_button(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    element = driver.find_element(By.ID, "newButtonName")
    element.click()
    element.send_keys("ITCH")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH"))

# def test_slow_calculator(driver):
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#     wait = WebDriverWait(driver, 10)
#     delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
#     delay_input.clear()
#     delay_input.send_keys("15")
#     driver.find_element(By.XPATH, "//span[text()='7']").click()
#     driver.find_element(By.XPATH, "//span[text()='+']").click()
#     driver.find_element(By.XPATH, "//span[text()='8']").click()
#     driver.find_element(By.XPATH, "//span[text()='=']").click()
#     try:
#         result_element = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))
#     except TimeoutException:
#         raise AssertionError("Ожидаемый результат '15' не отобразился (таймаут ожидания)!")

# def test_slow_calculator2(driver):
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
#     wait = WebDriverWait(driver, 10)
#     land_element = wait.until(EC.presence_of_element_located((By.ID, "landscape")))
#     # assert 'https://bonigarcia.dev/selenium-webdriver-java/img/landscape.png' in land_element.get_attribute("src")
#     assert land_element.get_attribute("src") == 'https://bonigarcia.dev/selenium-webdriver-java/img/landscape.png'

# def test_header_text(driver):
#     driver.implicitly_wait(10)
#     element = driver.find_element(By.CSS_SELECTOR, "img[imgfield='tn_img_1710153310161']")
#     element.click()
#     sleep(1)
#     wait = WebDriverWait(driver, 3)
#     element = wait.until(EC.presence_of_element_located((By.ID, "some_id")))
#
#     # header = driver.find_element(By.CSS_SELECTOR, "img[imgfield='tn_img_1710153310161']")
#     # header.click()
#     # sleep(5)
#     # assert header.text == "Cat memes"
#     # print('test text header is successful!')

# def test_time_of_first_cat_card(driver):
#     time_first_cat = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(1) small")
#     assert time_first_cat.text == "9 mins"
#     print('test time of first cat card is successful!')
#
# def test_last_cat_card_name(driver):
#     last_card_name = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(6) p")
#     assert last_card_name.text == "I love you so much"
#
# def test_cats_album_text(driver):
#     cats_album = driver.find_element(By.TAG_NAME, "strong")
#     assert cats_album.text == "Cats album"
#
def test_first_cat_card_is_displayed(driver):
    driver.get('https://suninjuly.github.io/cats.html')
    first_cat_card = driver.find_element(By.CSS_SELECTOR, ".col-sm-4:nth-child(1)")
    assert first_cat_card.is_displayed()
#
# def test_photo_icon_is_displayed(driver):
#     photo_icon = driver.find_element(By.TAG_NAME, "svg")
#     assert photo_icon.is_displayed()
#
# # def test_check_image_quantity(driver):
# #     images = driver.find_elements(By.TAG_NAME, "img")
# #     print(len(images))
#
#
# def test_check_all_cards_are_displayed(driver):
#     cards = driver.find_elements(By.CSS_SELECTOR, ".col-sm-4")
#     for card in cards:
#         assert card.is_displayed()

#
# import pytest
# from selenium import webdriver
# from selenium.common import TimeoutException
# from selenium.webdriver.common.by import By
# from time import sleep
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()
#
# def test_dragging(driver):
#     driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
#
#     wait = WebDriverWait(driver, 10)
#
#     # Принятие cookies
#     consent_btn = wait.until(EC.visibility_of_element_located((
#         By.CSS_SELECTOR,
#         "button.fc-button.fc-cta-consent.fc-primary-button"
#     )))
#     consent_btn.click()
#
#     # Переключение на iframe
#     iframe = wait.until(EC.visibility_of_element_located((
#         By.CSS_SELECTOR,
#         'div[rel-title="Photo Manager"] > p > iframe'
#     )))
#     driver.switch_to.frame(iframe)
#
#     # Выполнение drag-and-drop
#     source = driver.find_element(By.CSS_SELECTOR, "#gallery > li:nth-child(1)")
#     target = driver.find_element(By.ID, "trash")
#     actions = ActionChains(driver)
#     actions.drag_and_drop(source, target).perform()
#
#     # Ожидание, пока количество элементов <li> станет 3
#     try:
#         wait.until(lambda d: len(d.find_element(By.ID, "gallery").find_elements(By.TAG_NAME, "li")) == 3)
#     except TimeoutException:
#         actual_li = driver.find_element(By.ID, "gallery").find_elements(By.TAG_NAME, "li")
#         assert False, f"Ожидалось 3 элемента <li>, но найдено {len(actual_li)} после 10 секунд ожидания"
#
#
# def test_drag_and_drop_image_to_trash(driver):
#     driver.get('https://www.globalsqa.com/demo-site/draganddrop/')
#
#     #сначала кликаем на куки-капчу, иначе дальше тест упадет
#     consent_button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Соглашаюсь']")))
#     consent_button.click()
#
#     photo_manager_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'Photo Manager')))
#     photo_manager_tab.click()
#
#     WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@data-src, 'photo-manager.html')]")))
#
#
#     source_image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]/img")))
#     source_image_alt = source_image.get_attribute('alt')
#
#     trash_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'trash')))
#
#     actions = ActionChains(driver)
#     actions.click_and_hold(source_image).move_to_element(trash_element).release().perform()
#     print('Изображение перетащено в корзину')
#
#     WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//div[@id='trash']/ul/li/img[@alt='{source_image_alt}']")))
#     print(f"Изображение '{source_image_alt}' в корзине")
#
#     items_in_trash = driver.find_elements(By.XPATH, "//div[@id='trash']/ul/li")
#     assert len(items_in_trash) == 1, f'Ожидался 1 элемент в корзине, но найдено {len(items_in_trash)}'
#     print(f'В корзине {len(items_in_trash)} фотография(ии) (ожидался 1)')
#
#
#     WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.XPATH, f"//ul[@id='gallery']/li/img[@alt='{source_image_alt}']")))
#     items_in_gallery = driver.find_elements(By.XPATH, "//ul[@id='gallery']/li")
#     assert len(items_in_gallery) == 3, f'Ожидалось 3 фотографии в галерее, но найдено {len(items_in_gallery)}'
#     print(f'В галерее осталось {len(items_in_gallery)} фотографии (ожидалось 3)')
#
#
#     driver.switch_to.default_content()