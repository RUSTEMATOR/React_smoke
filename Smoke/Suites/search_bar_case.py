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


@allure.suite("Heared Suite")
class SearchBar(TestData):
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
            self.click_on_search()
    
    @allure.step("Click on Search bar")
    def click_on_search(self):
        search_bar = self.page.locator("#games-search")
        
        
        try:
            search_bar.fill("Fire Lightning")
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Click on Search bar", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Click on Search bar (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        
        finally:
            self.enter_firelightning()
    
    
    @allure.step("Enter Fire Lightning game")
    def enter_firelightning(self):
        fire_lighnting_button = self.page.get_by_title("Fire Lightning")
        
        try:
            fire_lighnting_button.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Enter Fire Lightning game", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Enter fire lightning in the search field (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        
        finally:
            self.add_favorite()
    
    @allure.step("Make a bet")
    def add_favorite(self):
        try:
            time(7)
            self.page.get_by_role("button", name="").click()
            self.page.press("Space")
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Make a bet", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Enter fire lightning in the search field (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            
        finally:
            self.go_back()
    
    @allure.step("Go back to the main page")
    def go_back(self, distance = 100):
        main_page_button = self.page.frame_locator("#root iframe").frame_locator("iframe").locator("#button-back")
        
        self.page.mouse.move(0, 0)
        self.page.mouse.move(-distance, 0)
        main_page_button.click()
        time.sleep(1)
        allure.attach(self.page.screenshot(), name="Go back to the main page", attachment_type=allure.attachment_type.PNG)
        
        
        
    
    
