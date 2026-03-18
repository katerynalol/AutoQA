from time import sleep
from summary.sum6.tests.base_test import BaseTest


class TestContactForm(BaseTest):

    def test_successful_open(self):
       self.contact_page.open()
       contact_text = self.contact_page.get_text(self.contact_page.LOCATION_INFO)

       assert contact_text == "Welcome to Shady Meadows, a delightful Bed & Breakfast nestled in the hills on Newingtonfordburyshire. A place so beautiful you will never want to leave. All our rooms have comfortable beds and we provide breakfast from the locally sourced supermarket. It is a delightful place."