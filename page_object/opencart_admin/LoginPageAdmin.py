from page_object.opencart_admin.BasePageAdmin import BasePageAdmin
from page_object.opencart_admin.elements.AuthFormAdmin import AuthFormAdmin


class LoginPageAdmin(BasePageAdmin):

    def authorization_with(self, username, password):
        AuthFormAdmin(self.browser) \
            .open_login_page() \
            .fill_out_auth_form(username, password) \
            .send_auth_from()
