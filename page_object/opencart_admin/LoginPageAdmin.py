from selenium.webdriver.common.by import By


class LoginPageAdmin:
    path = "/admin/"

    INPUT_USERNAME = (By.XPATH, "//input[@name='username']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name='password']")
    BTN_LOGIN = (By.XPATH, "//button[@class='btn btn-primary']")

    def __init__(self, browser):
        self.browser = browser

    def authorization_with(self, username, password):
        self.browser.open(self.path)
        self.browser.find_element(*self.INPUT_USERNAME).clear()
        self.browser.find_element(*self.INPUT_USERNAME).send_keys(username)
        self.browser.find_element(*self.INPUT_PASSWORD).clear()
        self.browser.find_element(*self.INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*self.BTN_LOGIN).click()
