from page_object.opencart_admin.BasePageAdmin import BasePageAdmin


class Alerts(BasePageAdmin):

    def alert_accept(self):
        alert = self.browser.switch_to.alert
        alert.accept()
