import allure
import pytest
import time
import pdb
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, expect
from playwright.sync_api import Locator
from Data.testinfo import TestInfo
from Suites.Locators.Locators import Locators
from Suites.Base.base_setup import BaseSetUp



@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Heared Suite")
class SuiteHeader(BaseSetUp):
    def set_up(self):
        try:
            super().set_up()
            self.accept_cookie_button.click()
        except Exception as e:
            raise AssertionError from e
    
    @allure.step("Open Deposit window")
    def press_deposit(self):
        try:
            self.deposit_button.click()
            expect(self.payment_method).to_be_visible()
            allure.attach(self.page.screenshot(), name="Deposit button clicked", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Deposit button clicked (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

            
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
            raise AssertionError()

            

    @allure.step("Close the deposit window")
    def close_deposit(self):
        try:
            self.closing_button.click()
            expect(self.payment_method).to_be_hidden()
            allure.attach(self.page.screenshot(), name="Close the deposit window", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Close the deposit window (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    
    @allure.step("Open wallet in player's profile")
    def open_players_profile(self):
        try:
            self.profile_unwrapper.click()
            self.profile_info_button.click()
            self.wallet_tab.click()

            allure.attach(self.page.screenshot(), name="Go back to the main page", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening profile (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    
    @allure.step("Check deposit tab")
    def check_deposit_tab(self):
        try:
            self.deposit_tab.click()
            expect(self.payment_method).to_be_visible(timeout=10000)

            allure.attach(self.page.screenshot(), name="Deposit methods", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Deposit method missing", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()
