import random
from selenium.webdriver.common.by import By


class ProductPageAdmin:
    BTN_ADD_NEW_PRODUCT = (By.XPATH, "//i[@class='fa fa-plus']")
    BTN_DELETE_PRODUCT = (By.XPATH, "//button[@data-original-title='Delete']")
    BTN_SAVE_PRODUCT = (By.XPATH, "//i[@class='fa fa-save']")
    BTN_FILTER = (By.XPATH, "//button[@id='button-filter']")

    INPUT_PRODUCT_NAME = (By.XPATH, "//input[@id='input-name1']")
    INPUT_META_TAG_TITLE = (By.XPATH, "//input[@id='input-meta-title1']")
    INPUT_MODEL = (By.XPATH, "//input[@id='input-model']")
    INPUT_PRODUCT_NAME_FILTER = (By.XPATH, "//input[@name='filter_name']")

    TABLE_ELEMENTS = (By.XPATH, "//tbody/tr")
    CHECKBOXES = (By.XPATH, "//input[@type='checkbox']")

    DATA_SECTION = (By.XPATH, "//a[text()='Data']")

    ALERT_MESSAGE = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def __init__(self, browser):
        self.browser = browser

    def go_to_add_new_product_form(self):
        self.browser.find_element(*self.BTN_ADD_NEW_PRODUCT).click()

    def create_new_product(self):
        product_name = f"Smartphone {random.randint(1, 1000)}"
        self.browser.find_element(*self.INPUT_PRODUCT_NAME).clear()
        self.browser.find_element(*self.INPUT_PRODUCT_NAME).send_keys(product_name)
        self.browser.find_element(*self.INPUT_META_TAG_TITLE).clear()
        self.browser.find_element(*self.INPUT_META_TAG_TITLE).send_keys(product_name)
        self.browser.find_element(*self.DATA_SECTION).click()
        self.browser.find_element(*self.INPUT_MODEL).clear()
        self.browser.find_element(*self.INPUT_MODEL).send_keys(product_name)
        self.browser.find_element(*self.BTN_SAVE_PRODUCT).click()
        return product_name

    def check_product_in_product_list(self, product_name):
        self.browser.find_element(*self.INPUT_PRODUCT_NAME_FILTER).clear()
        self.browser.find_element(*self.INPUT_PRODUCT_NAME_FILTER).send_keys(product_name)
        self.browser.find_element(*self.BTN_FILTER).click()
        self.browser.find_element(By.XPATH, f"//td[text()='{product_name}']")

    def select_product_in_product_list_by_position(self, position):
        self.browser.find_elements(*self.CHECKBOXES)[position].click()
        return self

    def delete_product_in_product_list(self):
        self.browser.find_element(*self.BTN_DELETE_PRODUCT).click()
        alert = self.browser.switch_to.alert
        alert.accept()
        return self

    def check_alert_message(self):
        self.browser.find_element(*self.ALERT_MESSAGE)
