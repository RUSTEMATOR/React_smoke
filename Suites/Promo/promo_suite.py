import allure
import pytest
import time
import re
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


@allure.suite("Burger menu")
class PromoCards(BaseSetUp):
    
    def set_up(self):
        try:
            super().set_up()
            self.accept_cookie_button.click()

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)



    @allure.step("Press on Get it button")
    def press_getit(self):
        try:
            while not self.getit_button.is_visible():
                self.arrow.click()
            else:
                self.getit_button.click()
                expect(self.bonus_modal).to_be_visible()
                expect(self.page.locator(".promo-modal__button.deposit-button")).to_be_visible()
                expect(self.page.locator(".promo-modal__button.deposit-button")).to_contain_text("deposit")


                time.sleep(2)
                allure.attach(self.page.screenshot(), name="Get it button pressed", attachment_type=allure.attachment_type.PNG)
                self.page.go_back()

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Press on Get it button (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Bonus modal is not visible")




    @allure.step("Check Promotions page")
    def open_promotions(self):
        try:
            self.promotions_page_sidebar.click()
            time.sleep(1)
            expect(self.promo_list).to_be_visible()
            allure.attach(self.page.screenshot(), name="Promotions page is open", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening promotions page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Promotions page is not visible")

            
    @allure.step("Press on 'i' button")
    def press_on_i(self):
        try:
            self.i_button.click()
            expect(self.bonus_modal).to_be_visible()
            expect(self.page.locator(".promo-modal__button.deposit-button")).to_be_visible()
            expect(self.page.locator(".promo-modal__button.deposit-button")).to_contain_text("deposit")

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
            raise AssertionError("Bonus modal is not visible")

            
    @allure.step("Close modal")
    def close_modal(self):
        try:
            self.page.get_by_role("button", name="").click()
            allure.attach(self.page.screenshot(), name="Modal is closed", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Modal closing (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)

            
    @allure.step ("Click on 'Get it' button")
    def click_on_GetIt(self):
        try:
            GetIt_button = self.page.locator("div").filter(has_text=re.compile(r"^Crypto Welcome Bonus100% up to 1 BTC \+250 Free SpinsGet it$")).get_by_role("button").nth(1)
            GetIt_button.click()

            expect(self.bonus_modal).to_be_visible()
            expect(self.page.locator(".promo-modal__button.deposit-button")).to_be_visible()
            expect(self.page.locator(".promo-modal__button.deposit-button")).to_contain_text("deposit")

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
        