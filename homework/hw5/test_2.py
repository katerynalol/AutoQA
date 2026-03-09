import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.globalsqa.com/demo-site/draganddrop/"

@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()

    d.get(URL)

    consent_cookie = {
        "name": "FCCDCF",
        "value": "%5Bnull%2Cnull%2Cnull%2C%5B%22CQgl8sAQgl8sAEsACBENCUFoAP_gAEPgABBoK1IB_C7EbCFCiDJ3IKMEMAhHABBAYsAwAAYBAwAADBIQIAQCgkEYBASAFCACCAAAKASBAAAgCAAAAUAAIAAFAABAAAwAIBAIIAAAgAAAAEAIAAAACIAAEQCAAAAEAEAAkAgAAAIASAAAAAAAAACBAAAAAAAAAAAAAAAABAEAAQAAQAAAAAAAiAAAAAAAABAIAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQWEQD-F2I2EKFEGCuQUYIYBCuACAAxYBgAAwCBgAAGCQgQAgFJIIkCAEAIEAAEAAAQAgCAABQEBAAAIAAAAAqAACAABgAQCAQAIABAAAAgIAAAAAAEQAAIgEAAAAIAIABABAAAAQAkAAAAAAAAAECAAAAAAAAAAAAAAAAAAIAAEABgAAAAAABEAAAAAAAACAQIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAA.ILCIB_C7EbCFCiDJ3IKMEMAhXABBAYsAwAAYBAwAADBIQIAQCkkEaBASAFCACCAAAKASBAAAoCAgAAUAAIAAVAABAAAwAIBAIIEAAgAAAQEAIAAAACIAAEQCAAAAEAEAAkAgAAAIASAAAAAAAAACBAAAAAAAAAAAAAAAABAEAASAAwAAAAAAAiAAAAAAAABAIEAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAABAAAAAAAQAAAE%22%2C%222~61.89.122.161.184.196.230.314.442.445.494.550.576.827.1029.1033.1046.1047.1051.1097.1126.1166.1301.1342.1415.1725.1765.1942.1958.1987.2068.2072.2074.2107.2213.2219.2223.2224.2328.2331.2387.2416.2501.2567.2568.2575.2657.2686.2778.2869.2878.2908.2920.2963.3005.3023.3126.3234.3235.3253.3309.3731.6931.8931.13731.15731.33931~dv.%22%2C%2212B1A492-A3E1-4AB1-8265-0AC9C6F70FA1%22%5D%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22b7049a38-ceb4-4b15-9a2b-b4be27488197%5C%22%2C%5B1772729210%2C963000000%5D%5D%22%5D%5D%5D",
        "domain": ".globalsqa.com",
        "path": "/",
        "secure": False,
    }

    d.add_cookie(consent_cookie)
    d.refresh()

    yield d
    d.quit()


def test_drag_and_drop(driver):
    wait = WebDriverWait(driver, 10)
    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame")))
    driver.switch_to.frame(frame)

    picture_1 = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery li")))[0]
    trash = wait.until(EC.visibility_of_element_located((By.ID, "trash")))

    actions = ActionChains(driver)
    actions.drag_and_drop(picture_1, trash).perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash li")))

    assert len(driver.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    assert len(driver.find_elements(By.CSS_SELECTOR, "#gallery li")) == 3
