from page_object.opencart.MainPage import MainPage
from page_object.opencart.RegistrationPage import RegistrationPage


def test_registration_new_user(browser):
    MainPage(browser).go_to_registration_page()
    RegistrationPage(browser) \
        .create_new_user() \
        .check_success_registration_message()


def test_switch_currency(browser):
    currency = MainPage(browser).switch_to_another_currency()
    MainPage(browser).check_currency_in_product_card(currency)
