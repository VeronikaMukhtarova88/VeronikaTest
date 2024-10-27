from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage

def test_add_todo(page:Page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()
    registration_page.firstname_enter()
    registration_page.lastname_enter()
    registration_page.email_enter()
    registration_page.female_click()
    registration_page.mobile_enter()
    registration_page.data_of_birthday_enter()
    registration_page.subject_enter()
    registration_page.hobbies_check()
    registration_page.select_picture_enter()
    registration_page.address_enter()
    registration_page.select_state_click()
    registration_page.select_city_click()
    registration_page.submit_click()









