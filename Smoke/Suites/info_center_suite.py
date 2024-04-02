import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page
from playwright.sync_api import Locator
from testdata import TestData



class InfoCenter():
    
    def __init__(self, page: Page):
        self.page = page
    
    @allure.step("Open site")
    def open_page(self):
        try:
            self.page.goto("https://www.kingbillycasino.com/")
            allure.attach(self.page.screenshot(), name="Opening the main page successful", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the site failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the site")  # Mark step as failed
            
        finally: 
            self.open_banking_page()
            
            
    @allure.step("Banking page")
    def open_banking_page(self):
        try:
            banking_page = self.page.get_by_role("link", name="Banking")
            banking_page.click()
            self.page.get_by_role("heading", name="Payments").is_visible()
            allure.attach(self.page.screenshot(), name="Banking page is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the banking page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the banking page")  # Mark step as failed
        
        finally:
            self.open_casino_faq()
            
            
    @allure.step("Casino FAQ")
    def open_casino_faq(self):
        casino_faq_page = self.page.get_by_role("link", name="Casino FAQ")
        faq_title = self.page.get_by_role("heading", name="CASINO FAQ")
        try:
            casino_faq_page.click()
            faq_title.is_visible()
            allure.attach(self.page.screenshot(), name="Casino FAQ is open", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the FAQ page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the FAQ page")  # Mark step as failed
    
        finally:
            self.open_casino_dictionary()


    @allure.step("Casino dictionary")
    def open_casino_dictionary(self):
        casino_dictionary_page = self.page.get_by_role("main").get_by_role("link", name="Casino Dictionary")
        dictionary_title = self.page.get_by_role("heading", name="KING’S DICTIONARY")
        
        try:
            casino_dictionary_page.click()
            dictionary_title.is_visible()
            allure.attach(self.page.screenshot(), name="Casino dictionary is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the casino dictionary page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the casino dictionary page")  # Mark step as failed
        
        finally:
            self.open_crypto_page()
        
    
    @allure.step("Crypto currencies FAQ")
    def open_crypto_page(self):
        crypto_page = self.page.get_by_role("main").get_by_role("link", name="Crypto Currencies FAQ")
        crypto_page_title = self.page.get_by_role("heading", name="CRYPTO CURRENCIES FAQ")
        
        try:
            crypto_page.click()
            crypto_page_title.is_visible()
            allure.attach(self.page.screenshot(), name="Crypto currencies FAQ is open", attachment_type=allure.attachment_type.PNG)
                
        
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the crypto FAQ page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the crypto FAQ page")  # Mark step as failed
            
        finally:
            self.open_complaints()
    
    @allure.step("Complaints")
    def open_complaints(self):
        complaints_page = self.page.get_by_role("main").get_by_role("link", name="Complaints")
        complaints_title = self.page.get_by_role("heading", name="Complaints")
        
        try:
            complaints_page.click()
            complaints_title.is_visible()
            allure.attach(self.page.screenshot(), name="Complaints page is open", attachment_type=allure.attachment_type.PNG)
        
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the complaints page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the complaints page")  # Mark step as failed
        
        finally:
            self.open_terms_and_C()
    
    @allure.step("Terms and conditions")
    def open_terms_and_C(self):
        terms_page = self.page.get_by_role("main").get_by_role("link", name="Terms and Conditions", exact=True)
        terms_title = self.page.get_by_role("heading", name="TERMS AND CONDITIONS")
        
        try:
            terms_page.click()
            terms_title.is_visible()
            allure.attach(self.page.screenshot(), name="Terms and conditions is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the T&C page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the T&C page")  # Mark step as failed
        
        finally:
            self.open_privacy_policy()
            
    
    @allure.step("Privacy policy")
    def open_privacy_policy(self):
        privacy_page = self.page.get_by_role("main").get_by_role("link", name="Privacy Policy")
        privacy_title = self.page.get_by_role("heading", name="PRIVACY POLICY")
        
        try:
            privacy_page.click()
            privacy_title.is_visible()
            allure.attach(self.page.screenshot(), name="Privacy policy is open", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the privacy policy page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the privacy policy page")  # Mark step as failed
        
        finally:
            self.open_responsible_gaming()
            
    
    @allure.step("Responsible gaming page")
    def open_responsible_gaming(self):
        responsible_page = self.page.get_by_role("main").get_by_role("link", name="Responsible Gaming")
        responsible_title = self.page.get_by_role("heading", name="Responsible Gaming")
        
        try:
            responsible_page.click()
            responsible_title.is_visible()
            allure.attach(self.page.screenshot(), name="Responsible gaming page", attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the responsible gaming page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the responsible gaming page")  # Mark step as failed
        
        finally:
            self.open_support()
            
    
    @allure.step("Casino support")
    def open_support(self):
        support_page = self.page.get_by_role("link", name="Support")
        support_title = self.page.get_by_role("heading", name="Casino Support")
        
        try:
            support_page.click()
            support_title.is_visible()
            allure.attach(self.page.screenshot(), name="Caasino support is open", attachment_type=allure.attachment_type.PNG)
                
            
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Opening the support page failed", attachment_type=allure.attachment_type.PNG)
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Failed to open the support page")  # Mark step as failed

