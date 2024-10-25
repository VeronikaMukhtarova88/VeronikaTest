from playwright.sync_api import expect
from playwright.sync_api import Page, expect

class RegistrationPage:

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto("https://demoqa.com/automation-practice-form")

    def firstname_click(self):
        self.page.get_by_placeholder("First Name").click()

    def firstname_fill(self):
        self.page.get_by_placeholder("First Name").fill("Veronika")

    def firstname_enter(self):
        self.page.get_by_placeholder("First Name").press("Enter")