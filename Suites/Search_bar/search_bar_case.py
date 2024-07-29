import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page, expect
from playwright.sync_api import Locator
from Suites.Base.base_setup import BaseSetUp


@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Heared Suite")
class SearchBar(BaseSetUp):
    def set_up(self):
        super().set_up()
        self.accept_cookie_button.click()

    
    @allure.step("Click on Search bar")
    def click_on_search(self):
        try:
            self.search_bar.fill("Fire Lightning")
            self.search_bar.blur()
            expect(self.search_bar).to_have_value("Fire Lightning")
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Click on Search bar", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Click on Search bar (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    @allure.step("Enter Fire Lightning game")
    def enter_firelightning(self):
        try:
            self.fire_lighnting_button.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Enter Fire Lightning game", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Enter fire lightning in the search field (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()


    @allure.step("Go back to the main page")
    def go_back(self, distance = 100):
        try:
            self.page.mouse.move(0, 0)
            self.page.mouse.move(-distance, 0)
            self.main_page_button.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Go back to the main page", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Go back to the main page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()
        
        
        
    
    
