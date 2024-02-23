import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Locator
from testdata import TestData
from testdata import site_link



@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Heared Suite")
class SuiteHeader(TestData):
    def __init__(self, page: Page):
        self.page = page

        

    
    def open_page(self):
        try:
            self.page.goto(site_link)
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            
        finally: 
            self.open_signin_form()

    def open_signin_form(self):
        sign_in_form = self.page.get_by_role("link", name="sign in")
        try:
            sign_in_form.click()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            
        finally:
            self.enter_valid_data()


    def enter_valid_data(self):
        login_email_field = self.page.get_by_placeholder("your e-mail address")
        login_password_field = self.page.get_by_placeholder("your password")

        try:
            login_email_field.click()
            login_email_field.fill(self.login_email)
            

            login_password_field.click()
            login_password_field.fill(self.login_password)
            

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)

        finally:
            self.press_enter()

    
    def press_enter(self):
        try:
            self.page.get_by_role("button", name="sign in").click()
            time.sleep(3)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
        
        finally:
            self.press_deposit()
    
    @allure.step("Open Deposit window")
    def press_deposit(self):
        try:
            deposit_button = self.page.get_by_role("link", name="deposit")
            deposit_button.click()
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
        locator1 = self.page.locator("div").filter(has_text=(r"^Min €20$")).first
        try:
            if locator1.is_visible():
                locator1.click()
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
        closing_button = self.page.get_by_role("button", name="")
        
        try:
            closing_button.click()
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
            self.page.get_by_role("banner").get_by_role("button").first.click()
            self.page.locator("#downshift-2-input").click()
            self.page.get_by_role("link", name="Profile info").click()
            self.page.get_by_role("link", name=" Wallet").click()
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
            deposit_tab = self.page.get_by_role("link", name="deposit", exact=True)
            deposit_tab.click()
            
            if self.page.get_by_role("img", name="Banküberweisung").is_visible():
                pass
            else:
                raise AssertionError
            allure.attach(self.page.screenshot(), name="Deposit methods", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Deposit method missing", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
