import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import expect
from Suites.Locators.Locators import Locators
from Suites.Base.base_setup import BaseSetUp
from Data.testinfo import TestInfo
@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")



class SuiteLogIn(BaseSetUp):

    @allure.step("Set up")
    def set_up(self):
        super().set_up_no_login()
        


    @allure.step("Open Sign in form")
    def open_signin_form(self):
        try:
            self.sign_in_form.click()
            expect(self.sign_in_button).to_be_visible()
            allure.attach(self.page.screenshot(), name="Sign in Form Opened", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Sign in Form Opened (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()


    @allure.step("Enter valid data")
    def enter_valid_data(self):
        try:
            self.login_email_field.click()
            self.login_email_field.fill(self.login_email)
            allure.attach(self.page.screenshot(), name="Email Filled", attachment_type=allure.attachment_type.PNG)

            self.login_password_field.click()
            self.login_password_field.fill(self.login_password)
            allure.attach(self.page.screenshot(), name="Password filled", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Valid data entered (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    @allure.step("Press Sign in")
    def press_login(self):
        try:
            self.sign_in_button.click()
            expect(self.deposit_button).to_be_visible()
            allure.attach(self.page.screenshot(), name="Logged in", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Valid data entered (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError() # Raising the exception to mark the step as failed in Allure
        