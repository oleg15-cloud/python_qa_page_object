from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.common.by import By


class MainPageAdmin:
    NAVIGATION_CATALOG = (By.XPATH, "//li[@id='menu-catalog']")
    NAVIGATION_CATALOG_PRODUCTS = "//a[text()='Products']"

    def __init__(self, browser):
        self.browser = browser

    def go_to_product_page(self):
        self.browser.find_element(*self.NAVIGATION_CATALOG).click()
        WebDriverWait(self.browser, 3).until(
            ec.visibility_of_element_located((By.XPATH, self.NAVIGATION_CATALOG_PRODUCTS))).click()
