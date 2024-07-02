import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page, expect
from playwright.sync_api import Locator
from Data.testinfo import TestInfo
from Suites.Locators.Locators import Locators



@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Heared Suite")
class SuiteHeader(Locators):
    def __init__(self, page: Page):
        self.page = page

        

    
    def open_page(self, kingbillysite):
        try:
            self.page.goto(kingbillysite)
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            
        finally: 
            self.open_signin_form()

    def open_signin_form(self):
        try:
            self.sign_in_form.click()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            
        finally:
            self.enter_valid_data()


    def enter_valid_data(self):
        try:
            self.login_email_field.click()
            self.login_email_field.fill(self.login_email)
            

            self.login_password_field.click()
            self.login_password_field.fill(self.login_password)
            

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)

        finally:
            self.press_enter()

    
    def press_enter(self):
        try:
            self.sign_in_button.click()
            time.sleep(3)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        
        finally:
            self.press_deposit()
    
    @allure.step("Open Deposit window")
    def press_deposit(self):
        try:
            self.deposit_button.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Deposit button clicked", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Deposit button clicked (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally: 
            self.options_check()
            
    @allure.step("Check for deposit options")
    def options_check(self):
        try:
            if self.payment_method.is_visible():
                self.payment_method.click()
                pass
            else:
                raise AssertionError
                
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Check for deposit options (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            
        finally:
            self.close_deposit()
            

    @allure.step("Close the deposit window")
    def close_deposit(self):
        try:
            self.closing_button.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Close the deposit window", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Close the deposit window (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        
        finally:
            self.open_players_profile()
    
    @allure.step("Open wallet in player's profile")
    def open_players_profile(self):
        try:
            self.sidebar_menu.click()
            self.profile_unwrapper.click()
            self.profile_info_button.click()
            self.wallet_tab.click()
            allure.attach(self.page.screenshot(), name="Go back to the main page", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening profile (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.check_deposit_tab()
    
    @allure.step("Check deposit tab")
    def check_deposit_tab(self):
        try:

            self.deposit_tab.click()
            
            expect(self.bank_transfer).to_be_visible(timeout=10000)

            allure.attach(self.page.screenshot(), name="Deposit methods", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Deposit method missing", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
