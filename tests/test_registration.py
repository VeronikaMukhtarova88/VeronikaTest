from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage

def test_add_todo(page:Page):
    registration_page = RegistrationPage(page)
    registration_page.open()
    registration_page.firstname_click()
    registration_page.firstname_fill()
    registration_page.lastname_click()
    registration_page.lastname_fill()
    registration_page.email_click()
    registration_page.email_fill()
    registration_page.female_click()
    registration_page.mobile_click()
    registration_page.mobile_fill()
    registration_page.data_of_birthday_click()
    registration_page.submit_click()
    registration_page.subject_fill()
    registration_page.hobbies_click()
    registration_page.select_picture_click()
    registration_page.address_click()
    registration_page.address_fill()
    registration_page.select_state_click()
    registration_page.select_city_click()
    registration_page.submit_click()









