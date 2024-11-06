import pytest
from playwright.async_api import Page
from pages.registration_page import RegistrationPage

@pytest.fixture()
def registration_page(page:Page):
    return RegistrationPage(page)

@pytest.fixture()
def page(context):
    page: Page = context.new_page()
    page.set_viewport_size({'height': 600, 'width': 800})
    yield page

