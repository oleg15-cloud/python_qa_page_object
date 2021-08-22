import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MainPage:
    BTN_MY_ACCOUNT = (By.XPATH, "//i[@class='fa fa-user']")
    BTN_MY_ACCOUNT_REGISTER = (By.XPATH, "//a[text()='Register']")
    BTN_CURRENCY = "//button[@class='btn btn-link dropdown-toggle']"

    CURRENCIES = (By.XPATH, "//li/button")
    CURRENCY_STRONG = (By.XPATH, "//strong")
    PRODUCT_CARDS = (By.XPATH, "//div[@class='product-thumb transition']")
    PRODUCT_CARDS_PRICE = (By.XPATH, "//p[@class='price']")

    def __init__(self, browser):
        self.browser = browser

    def go_to_registration_page(self):
        self.browser.find_element(*self.BTN_MY_ACCOUNT).click()
        self.browser.find_element(*self.BTN_MY_ACCOUNT_REGISTER).click()

    def switch_to_another_currency(self):
        WebDriverWait(self.browser, 2).until(ec.visibility_of_element_located((By.XPATH, self.BTN_CURRENCY))).click()
        currencies = self.browser.find_elements(*self.CURRENCIES)
        random_currency = random.randint(0, len(currencies) - 1)
        currencies[random_currency].click()
        return self.browser.find_element(*self.CURRENCY_STRONG)

    def check_currency_in_product_card(self, web_element):
        assert web_element == self.browser.find_element(*self.CURRENCY_STRONG)
