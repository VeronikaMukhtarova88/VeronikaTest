import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 800, 'width': 1000})
    yield page