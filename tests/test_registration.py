import pytest
import allure

@allure.feature('Practice Form')
@allure.story('Registration with correct data')
@pytest.mark.parametrize('credentials1, credentials2', [
    ('user@mail.ru', '8888888888')
])
def test_registration_valid_data(page, credentials1, credentials2, registration_page):
    with allure.step('Open registration form'):
        registration_page.navigate()
    with allure.step('Input fields'):
        registration_page.firstname_enter()
        registration_page.lastname_enter()
        registration_page.email_enter(credentials1)
        registration_page.female_click()
        registration_page.mobile_enter(credentials2)
        registration_page.data_of_birthday_enter()
        registration_page.subject_enter()
        registration_page.hobbies_check()
        registration_page.select_picture_enter()
        registration_page.address_enter()
        registration_page.select_state_click()
        registration_page.select_city_click()
        registration_page.submit_click()
        registration_page.alert_window()

@allure.feature('Practice Form')
@allure.story('Registration with incorrect data')
@pytest.mark.parametrize('credentials1, credentials2', [
    ('user@mail', '98888')
])
def test_registration_invalid_data(page, credentials1, credentials2, registration_page):
    with allure.step('Open registration form'):
        registration_page.navigate()
    with allure.step('Input fields'):
        registration_page.firstname_enter()
        registration_page.lastname_enter()
        registration_page.email_enter(credentials1)
        registration_page.female_click()
        registration_page.mobile_enter(credentials2)
        registration_page.data_of_birthday_enter()
        registration_page.subject_enter()
        registration_page.hobbies_check()
        registration_page.select_picture_enter()
        registration_page.address_enter()
        registration_page.select_state_click()
        registration_page.select_city_click()
        registration_page.submit_click()
        registration_page.alert_window_close()

@allure.feature('Practice Form')
@allure.story('Registration with empty required fields')
@pytest.mark.parametrize('credentials1', [
    ('user@mail.ru')
])
def test_registration_required_fields_empty(page, credentials1, registration_page):
    with allure.step('Open registration form'):
        registration_page.navigate()
    with allure.step('Input fields'):
        registration_page.email_enter(credentials1)
        registration_page.data_of_birthday_enter()
        registration_page.subject_enter()
        registration_page.hobbies_check()
        registration_page.select_picture_enter()
        registration_page.address_enter()
        registration_page.select_state_click()
        registration_page.select_city_click()
        registration_page.submit_click()
        registration_page.alert_window_close()












