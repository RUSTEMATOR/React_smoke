import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page
from testdata import TestData

@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")



class SuiteLogIn(TestData):
    def __init__(self, page: Page):
        self.page = page

        
    @allure.step("Open the page")
    def open_page(self):
        try:
            self.page.goto("https://www.kingbillycasino6.com/")
            allure.attach(self.page.screenshot(), name="Page opened", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Page opened (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally: 
            self.open_signin_form()

    @allure.step("Open Sign in form")
    def open_signin_form(self):
        sign_in_form = self.page.get_by_role("link", name="sign in")
        try:
            sign_in_form.click()
            allure.attach(self.page.screenshot(), name="Sign in Form Opened", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Sign in Form Opened (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.enter_valid_data()

    @allure.step("Enter valid data")
    def enter_valid_data(self):
        login_email_field = self.page.get_by_placeholder("your e-mail address")
        login_password_field = self.page.get_by_placeholder("your password")

        try:
            login_email_field.click()
            login_email_field.fill(self.login_email)
            allure.attach(self.page.screenshot(), name="Email Filled", attachment_type=allure.attachment_type.PNG)

            login_password_field.click()
            login_password_field.fill(self.login_password)
            allure.attach(self.page.screenshot(), name="Password filled", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Valid data entered (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)

        finally:
            self.press_enter()

    @allure.step("Press Sign in")
    def press_enter(self):
        try:
            self.page.get_by_role("button", name="sign in").click()
            time.sleep(3)
            get_bonus_link = self.page.get_by_role("link", name="GET BONUS")
            with allure_step("Check if 'GET BONUS' is visible", self.page):
                assert get_bonus_link.is_visible(), "GET BONUS link is not visible"
            allure.attach(self.page.screenshot(), name="Logged in", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Valid data entered (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise  # Raising the exception to mark the step as failed in Allure
        