import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page, expect
from playwright.sync_api import Locator
from Data.testinfo import TestInfo
from Suites.Base.base_setup import BaseSetUp
from Suites.Locators.Locators import Locators


class Generator():
    @staticmethod
    # Function to generate a random email
    def generate_random_email():
        import random
        import string
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        return f'{random_word}{random_numbers}@kingbilly.xyz'


class Registration(TestInfo, BaseSetUp):
    def set_up(self):
        try:
            super().set_up_no_login()
            self.accept_cookie_button.click()

        except Exception as e:
            raise AssertionError from e

    @allure.step("Open registration form")
    def open_registration(self):
        try:
            self.registration_form.click()
            expect(self.login_input).to_be_visible()
            allure.attach(self.page.screenshot(), name="Registration form opened",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError


    @allure.step("Fill in login input")
    def fillin_login(self):
        random_email = Generator.generate_random_email()

        try:
            self.login_input.fill(random_email)
            self.password_input.click()
            time.sleep(1)
            expect(self.login_input).to_have_value(random_email)
            # Write email to the log file
            with open('test_accs_automation.txt', 'a') as file:
                file.write(random_email + '\n')
            # allure.attach(self.page.screenshot(), name="Login filled", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError


    @allure.step("Fill in password")
    def fillin_password(self):
        try:
            self.password_input.fill("193786Az()")
            expect(self.password_input).to_have_value("193786Az()")
            allure.attach(self.page.screenshot(), name="Password filled", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError


    @allure.step("Click on 18 years old checkbox")
    def adult_checkbox(self):
        try:
            self.adult_checkbox.click()
            expect(self.adult_checkbox).to_be_checked(True)
            allure.attach(self.page.screenshot(), name="18 years old checkbox clicked",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError


    @allure.step("Click on Promo checkbox")
    def promo_checkbox(self):
        try:
            self.promo_checkbox.click()
            expect(self.promo_checkbox).to_be_checked(True)
            allure.attach(self.page.screenshot(), name="Promo checkbox clicked",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError


    @allure.step("Create account")
    def create_account(self):
        try:
            self.create_account_button.click()
            allure.attach(self.page.screenshot(), name="Create account button clicked",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError


    @allure.step("Check for notification")
    def notification_check(self):
        try:
            expect(self.notification).to_be_visible()
            allure.attach(self.page.screenshot(), name="Notification is present",attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
