import allure
import pytest
import pdb
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page, expect
from playwright.sync_api import Locator
from Data.testinfo import TestInfo
from Suites.Base.base_info import BaseInfo
from Suites.Locators import Locators
from Suites.Base.base_setup import BaseSetUp



class InfoCenter(BaseSetUp):
    def set_up(self):
        try:
            super().set_up()
            self.accept_cookie_button.click()
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the info center failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the info center")

            
            
    @allure.step("Banking page")
    def open_banking_page(self):
        try:
            self.banking_page.click()
            self.page.get_by_role("heading", name="Payments").is_visible()
            expect(self.payment_method_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Banking page is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the banking page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the banking page")  # Mark step as failed

            
            
    @allure.step("Casino FAQ")
    def open_casino_faq(self):
        try:
            self.casino_faq_page.click()
            self.faq_title.is_visible()
            expect(self.faq_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Casino FAQ is open", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the FAQ page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the FAQ page")  # Mark step as failed



    @allure.step("Casino dictionary")
    def open_casino_dictionary(self):
        try:
            self.casino_dictionary_page.click()
            self.dictionary_title.is_visible()
            expect(self.dictionary_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Casino dictionary is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the casino dictionary page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the casino dictionary page")  # Mark step as failed

        
    
    @allure.step("Crypto currencies FAQ")
    def open_crypto_page(self):
        try:
            self.crypto_page.click()
            self.crypto_page_title.is_visible()
            expect(self.crypto_faq_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Crypto currencies FAQ is open", attachment_type=allure.attachment_type.PNG)
                
        
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the crypto FAQ page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the crypto FAQ page")  # Mark step as failed

    
    @allure.step("Complaints")
    def open_complaints(self):
        try:
            self.complaints_page.click()
            self.complaints_title.is_visible()
            expect(self.complaints_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Complaints page is open", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the complaints page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the complaints page")  # Mark step as failed

    
    @allure.step("Terms and conditions")
    def open_terms_and_C(self):
        try:
            self.terms_page.click()
            self.terms_title.is_visible()
            expect(self.termsAndConditions_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Terms and conditions is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the T&C page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the T&C page")  # Mark step as failed

            
    
    @allure.step("Privacy policy")
    def open_privacy_policy(self):
        try:
            self.privacy_page.click()
            self.privacy_title.is_visible()
            expect(self.privacy_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Privacy policy is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the privacy policy page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the privacy policy page")  # Mark step as failed

    
    @allure.step("Responsible gaming page")
    def open_responsible_gaming(self):
        try:
            self.responsible_page.click()
            self.responsible_title.is_visible()
            expect(self.responsible_gambling_container).to_be_visible()
            allure.attach(self.page.screenshot(), name="Responsible gaming page", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the responsible gaming page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the responsible gaming page")  # Mark step as failed

            
    
    @allure.step("Casino support")
    def open_support(self):
        try:
            self.support_page.click()
            self.support_title.is_visible()
            expect(self.email_input_support_form).to_be_visible()
            expect(self.message_input_support_form).to_be_visible()
            allure.attach(self.page.screenshot(), name="Caasino support is open", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the support page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the support page")  # Mark step as failed

