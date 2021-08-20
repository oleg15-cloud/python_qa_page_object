from page_object.opencart_admin.LoginPageAdmin import LoginPageAdmin
from page_object.opencart_admin.MainPageAdmin import MainPageAdmin
from page_object.opencart_admin.ProductPageAdmin import ProductPageAdmin


def test_auth(browser, user):
    LoginPageAdmin(browser).authorization_with(*user)
    MainPageAdmin(browser).go_to_product_page()
    ProductPageAdmin(browser).go_to_add_new_product_form()
    product_name = ProductPageAdmin(browser).create_new_product()
    ProductPageAdmin(browser).check_new_product_in_product_list(product_name)
