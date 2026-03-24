import pytest
from summary.sum6.pages.contact_page import ContactPage
from summary.sum6.pages.auth_page import AuthPage

@pytest.mark.usefixtures("setup")
class BaseTest:
    contact_page: ContactPage
    auth_page: AuthPage