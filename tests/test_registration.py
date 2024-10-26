import pytest
from playwright.sync_api import Page
from pages.registration_page import RegistrationPage

def test_add_todo(page:Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.firstname_click()
    registration_page.firstname_fill()
    registration_page.firstname_enter()
