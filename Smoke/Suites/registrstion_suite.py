import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Locator
from testdata import TestData
from testdata import site_link

class Generator():
    @staticmethod
    # Function to generate a random email
    def generate_random_email():
        import random
        import string
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        random_word = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
        return f'{random_word}{random_numbers}@kingbilly.xyz'


class Registration(TestData):
    def __init__(self, page: Page):
        self.page = page


    @allure.step("Open Site")
    def open_site(self):
        try:
            self.page.goto("https://www.kingbillycasino.com/")
            allure.attach(self.page.screenshot(), name="Page opened", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally:
            self.open_registration()
            
    
    @allure.step("Open registration form")
    def open_registration(self):
        registration_form = self.page.get_by_role("link", name="Create account")
        try:
            registration_form.click()
            allure.attach(self.page.screenshot(), name="Registration form opened", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally:
            self.fillin_login()
    
    @allure.step("Fill in login input")
    def fillin_login(self):
        login_input = self.page.locator("#registration-dynamic-form__email")
        random_email = Generator.generate_random_email()
        try:
            login_input.fill(random_email)
            # Write email to the log file
            with open('test_accs_automation.txt', 'a') as file:
                file.write(random_email + '\n')
            allure.attach(self.page.screenshot(), name="Login filled", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally: 
            self.fillin_password()
    
    
    @allure.step("Fill in password")
    def fillin_password(self):
        password_input = self.page.locator("#registration-dynamic-form__password_single")
        try: 
            password_input.fill("193786Az()")
            allure.attach(self.page.screenshot(), name="Password filled", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally:
            self.adult_checkbox()
    
            
    @allure.step("Click on 18 years old checkbox")
    def adult_checkbox(self):
        adult_checkbox = self.page.locator("#sign-up label").filter(has_text="I am 18 years old and I accept the Privacy Policy and Terms and Conditions *").locator("span").first
        try:
            adult_checkbox.click()
            allure.attach(self.page.screenshot(), name="18 years old checkbox clicked", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally:
            self.promo_checkbox()
            
    
    @allure.step("Click on Promo checkbox")
    def promo_checkbox(self):
        promo_checkbox = self.page.locator("#sign-up label").filter(has_text="I want to receive promos").locator("span").first
        
        try:
            promo_checkbox.click()
            allure.attach(self.page.screenshot(), name="Promo checkbox clicked", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally:
            self.create_account()
            
    
    @allure.step("Create account")
    def create_account(self):
        create_account_button = self.page.locator("#sign-up").get_by_role("button", name="Create account")
        try:
            create_account_button.click()
            allure.attach(self.page.screenshot(), name="Create account button clicked", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
        finally:
            self.notification_check()
            
            
    @allure.step("Check for notification")
    def notification_check(self):
        notification = self.page.get_by_role("heading", name="You will receive an email with instructions on how to confirm your email address in a few minutes.")
        try:
            notification.is_visible()
            allure.attach(self.page.screenshot(), name="Notification is present", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        
            
    
    