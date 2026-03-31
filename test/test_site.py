
import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is('Samsung galaxy s6')



def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    browser.maximize_window()
    homepage.click_monitor()
    time.sleep(3)      # так делать не надо, см первый тест
    homepage.check_products_count(2)
    # monitors = browser.find_elements(By.CSS_SELECTOR, ".card")
    #
    #
    # assert len(monitors) == 2
