from os import path
from playwright.sync_api import Page, expect

class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.email = page.get_by_placeholder("name@example.com")
        self.female = page.get_by_text("Female")
        self.mobile = page.get_by_placeholder("Mobile Number")
        self.data_of_birthday1 = page.locator("#dateOfBirthInput")
        self.data_of_birthday2 = page.get_by_role("option", name="Choose Wednesday, November 13th, 2024")
        self.subject_find = page.locator(".subjects-auto-complete__value-container")
        self.subject_input = page.locator("#subjectsInput")
        self.hobbies1 = page.get_by_text("Reading")
        self.hobbies2 = page.get_by_text("Music")
        self.select_picture_find = page.get_by_label("Select picture")
        self.address_input = page.get_by_placeholder("Current Address")
        self.select_state_find = page.locator("#state svg")
        self.select_state_input = page.get_by_text("Uttar Pradesh", exact=True)
        self.select_city_find = page.locator("#city svg")
        self.select_city_input = page.get_by_text("Agra", exact=True)
        self.submit_button = page.get_by_role("button", name="Submit")
        self.alert_accept = page.get_by_text("Thanks for submitting the form")


    def navigate(self):
        self.page.goto("https://demoqa.com/automation-practice-form", timeout=60000)


    def firstname_enter(self):
        self.first_name.click()
        self.first_name.fill("Veronika")

    def lastname_enter(self):
        self.last_name.click()
        self.last_name.fill("Test")

    def email_enter(self, credentials1):
        self.email.click()
        self.email.fill(credentials1)

    def female_click(self):
        self.female.click()

    def mobile_enter(self, credentials2):
        self.mobile.click()
        self.mobile.fill(credentials2)

    def data_of_birthday_enter(self):
        self.data_of_birthday1.click()
        self.data_of_birthday2.click()

    def subject_enter(self):
        self.subject_find.click()
        self.subject_input.fill("Test")

    def hobbies_check(self):
        self.hobbies1.check()
        self.hobbies2.check()

    def select_picture_enter(self):
        self.select_picture_find.click()
        self.page.set_input_files("#uploadPicture", './tests/file.txt')

    def address_enter(self):
        self.address_input.click()
        self.address_input.fill("Volzhsky, Olomoutskaya 5")

    def select_state_click(self):
        self.select_state_find.click()
        self.select_state_input.click()

    def select_city_click(self):
        self.select_city_find.click()
        self.select_city_input.click()

    def submit_click(self):
        self.submit_button.click()

    def alert_window(self):
        self.alert_accept.click()

    def alert_window_close(self):
        expect(self.alert_accept).to_be_hidden()
