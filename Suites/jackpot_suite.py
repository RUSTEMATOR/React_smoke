import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Locator
from testdata import TestData


@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Main page Suite")
class JackpotBanners(TestData):
    def __init__(self, page: Page):
        self.page = page

        
    
    def open_page(self):
        try:
            self.page.goto("https://www.kingbillycasino6.com/")
            
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
            self.click_on_crown()
    
    time.sleep(3)
    
    @allure.step("Check Crown Jackpot")
    def click_on_crown(self):
        crown_button = self.page.get_by_role("link", name="Crown Jackpot")
        try:
            crown_button.click()
            time.sleep(3)
            allure.attach(self.page.screenshot(), name="Crown transfer", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Crown transfer (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.verify_final_link_crown()
        
    @allure.step("Verify final link after clicking on Crown Jackpot")
    def verify_final_link_crown(self):
        expected_final_link = "https://www.kingbillycasino6.com/jackpots"
        try:
            current_url = self.page.url()

            if current_url == expected_final_link:
                print(f"Test passed: Final link is correct - {current_url}")
            else:
                raise AssertionError(f"Test failed: Final link is incorrect - {current_url}")
            allure.attach(self.page.screenshot(), name="Link verification", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Link verification (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            self.page.goto("https://www.kingbillycasino6.com")
        finally:
            self.click_on_shield()
        
    #_______________________________________________________________________________________________________
    
    
    @allure.step("Check Shield Jackpot")
    def click_on_shield(self):
        shield_button = self.page.get_by_role("link", name="Shield Jackpot")
        try:
            shield_button.click()
            allure.attach(self.page.screenshot(), name="Shiel jackpot transfer", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Shield jackpot transfer (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.verify_final_link_shield()
    
    
    @allure.step("Verify final link after clicking on Crown Jackpot")
    def verify_final_link_shield(self):
        expected_final_link = "https://www.kingbillycasino6.com/jackpots"
        try:
            current_url = self.page.url()

            if current_url == expected_final_link:
                print(f"Test passed: Final link is correct - {current_url}")
            else:
                raise AssertionError(f"Test failed: Final link is incorrect - {current_url}")
            allure.attach(self.page.screenshot(), name="Link verification", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Link verification (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            self.page.goto("https://www.kingbillycasino6.com")
        finally:
            self.click_on_sword()
    
    #_______________________________________________________________________________________________________
    
            
    @allure.step("Check Shield Jackpot")
    def click_on_sword(self):
        shield_button = self.page.get_by_role("link", name="Sword Jackpot")
        try:
            shield_button.click()
            allure.attach(self.page.screenshot(), name="Sword jacktop transfer", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Sword jacktop transfer (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.verify_final_link_sword()

    @allure.step("Verify final link after clicking on Crown Jackpot")
    def verify_final_link_sword(self):
        expected_final_link = "https://www.kingbillycasino6.com/jackpots"
        try:
            current_url = self.page.url()

            if current_url == expected_final_link:
                print(f"Test passed: Final link is correct - {current_url}")
            else:
                raise AssertionError(f"Test failed: Final link is incorrect - {current_url}")
            allure.attach(self.page.screenshot(), name="Link verification", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Link verification (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            self.page.goto("https://www.kingbillycasino6.com")
