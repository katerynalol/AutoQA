import pytest
from summary.sum6.pages.contact_page import ContactPage


@pytest.mark.usefixtures("setup")
class BaseTest:
    contact_page: ContactPage
    # inventory_page: InventoryPage (add more as you go)