from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/automation-practice-form", timeout=60000)

    def firstname_click(self):
        self.page.get_by_placeholder("First Name").click()

    def firstname_fill(self):
        self.page.get_by_placeholder("First Name").fill("Veronika")

    def lastname_click(self):
        self.page.get_by_placeholder("Last Name").click()

    def lastname_fill(self):
        self.page.get_by_placeholder("Last Name").fill("Test")

    def email_click(self):
        self.page.get_by_placeholder("name@example.com").click()

    def email_fill(self):
        self.page.get_by_placeholder("name@example.com").fill("test@mail.ru")

    def female_click(self):
        self.page.get_by_text("Female").click()

    def mobile_click(self):
        self.page.get_by_placeholder("Mobile Number").click()

    def mobile_fill(self):
        self.page.get_by_placeholder("Mobile Number").fill("9888888888")

    def data_of_birthday_click(self):
        self.page.locator("#dateOfBirthInput").click()
        self.page.get_by_text("13141516171819").click()

    def subject_click(self):
        self.page.locator(".subjects-auto-complete__value-container").click()

    def subject_fill(self):
        self.page.locator("#subjectsInput").fill("Test")

    def hobbies_click(self):
        self.page.locator("#hobbies-checkbox-2").check()
        self.page.get_by_text("Music").click()

    def select_picture_click(self):
        self.page.get_by_label("Select picture").click()

    def uploadfile_set_input_files(self):
        self.page.get_by_label("Select picture").set_input_files("IMG-f18e355a5b3a53e62b6b027263ac4fbc-V.jpg")

    def address_click(self):
        self.page.get_by_placeholder("Current Address").click()

    def address_fill(self):
        self.page.get_by_placeholder("Current Address").fill("Volzhsky, Olomoutskaya 5")

    def select_state_click(self):
        self.page.locator("#state svg").click()
        self.page.get_by_text("Uttar Pradesh", exact=True).click()

    def select_city_click(self):
        self.page.locator("#city svg").click()
        self.page.get_by_text("Agra", exact=True).click()

    def submit_click(self):
        self.page.get_by_role("button", name="Submit").click()


