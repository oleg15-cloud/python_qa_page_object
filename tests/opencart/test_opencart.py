from page_object.opencart.BasePage import BasePage
from page_object.opencart.RegistrationPage import RegistrationPage


def test_registration_new_user(browser):
    BasePage(browser).go_to_registration_page()
    RegistrationPage(browser) \
        .create_new_user() \
        .check_success_registration_message()


def test_switch_currency(browser):
    currency = BasePage(browser).switch_to_another_currency()
    BasePage(browser).check_new_currency(currency)
