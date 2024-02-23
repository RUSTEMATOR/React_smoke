import allure
import pytest
import time
import re
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


@allure.suite("Burger menu")
class PromoCards(TestData):
    
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
            self.press_getit()
    
    @allure.step("Press on Get it button")
    def press_getit(self):
        try:
            getit_button = self.page.get_by_role("link", name="GET BONUS")
            getit_button.click()
            time.sleep(2)
            allure.attach(self.page.screenshot(), name="Get it button pressed", attachment_type=allure.attachment_type.PNG)
            
            if self.page.locator("#promo-1").get_by_role("link", name="deposit").is_visible():
                pass
            else:
                raise AssertionError
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Press on Get it button (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.page.get_by_role("button", name="").click()
            self.open_burger_menu()
    
    @allure.step("Open burger menu")
    def open_burger_menu(self):
        try:
            self.page.get_by_role("banner").get_by_role("button").first.click()
            time.sleep(3)
            allure.attach(self.page.screenshot(), name="Burger menu opened", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            time.sleep(1)
            self.open_promotions()
    
    @allure.step("Check Promotions page")
    def open_promotions(self):
        try:
            promotions_page = self.page.locator("#bar").get_by_role("link", name="Promotions")
            promotions_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Promotions page is open", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening promotions page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.press_on_i()
            
    @allure.step("Press on 'i' button")
    def press_on_i(self):
        try:
            i_button = self.page.locator("div").filter(has_text=re.compile(r"^Crypto Welcome Bonus100% up to 1 BTC \+250 Free Spins$")).get_by_role("button")
            i_button.click()
            time.sleep(2)
            allure.attach(self.page.screenshot(), name="Button 'i' is pressed", attachment_type=allure.attachment_type.PNG)
            
            if self.page.locator("#promo-3").get_by_role("link", name="deposit").is_visible():
                pass
            else:
                raise AssertionError
        
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Pressing on 'i' (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.close_modal()
            
    @allure.step("Close modal")
    def close_modal(self):
        try:
            self.page.get_by_role("button", name="").click()
            allure.attach(self.page.screenshot(), name="Modal is closed", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Modal closing (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.click_on_GetIt()
            
    @allure.step ("Click on 'Get it' button")
    def click_on_GetIt(self):
        try:
            GetIt_button = self.page.locator("div").filter(has_text=re.compile(r"^Crypto Welcome Bonus100% up to 1 BTC \+250 Free SpinsGet it$")).get_by_role("button").nth(1)
            GetIt_button.click()
            time.sleep(2)
            allure.attach(self.page.screenshot(), name="'Get it' button clicked", attachment_type=allure.attachment_type.PNG)
            
            if self.page.locator("#promo-3").get_by_role("link", name="deposit").is_visible():
                pass
            else:
                raise AssertionError
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Click on 'Get it' button (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        