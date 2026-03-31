import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.fixture()
def browser():
    browser = webdriver.Firefox()
    browser.maximize_window()
    yield browser



def test_open_s6(browser):
    browser.get('https://www.demoblaze.com/index.html')
    galaxy_s6 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Samsung galaxy s6"))
    )
    galaxy_s6.click()
    title = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h2"))
    )
    assert title.text == 'Samsung galaxy s6'


def test_two_monitors(browser):
    browser.get('https://www.demoblaze.com/index.html')
    browser.maximize_window()
    monitor_link = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[onclick="byCat(\'monitor\')"]')
        )
    )
    monitor_link.click()
    time.sleep(3)      #плохое ожидание, на первой странице правильное
    monitors = browser.find_elements(By.CSS_SELECTOR, ".card")


    assert len(monitors) == 2
