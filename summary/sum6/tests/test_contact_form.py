from time import sleep
from .base_test import BaseTest
from .test_data import Constants

class TestContactForm(BaseTest):

    def test_successful_open_main_page(self):
       self.contact_page.open()
       text = self.contact_page.get_text(self.contact_page.LOCATION_INFO)
       print(text)
       sleep(1)

    def test_successful_open_auth_page(self):
        self.auth_page.open()
        self.auth_page.type_text(self.auth_page.USER_NAME_FIELD, Constants.USERNAME)
        self.auth_page.type_text(self.auth_page.PASSWORD_FIELD, Constants.PASSWORD)
        sleep(1)
