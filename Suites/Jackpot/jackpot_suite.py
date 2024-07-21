
import allure
from contextlib import contextmanager
from playwright.sync_api import expect

from Suites.Base.base_setup import BaseSetUp


@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Main page Suite")
class JackpotBanners(BaseSetUp):
    @allure.step("set up")
    def set_up(self):
        super().set_up()
        allure.attach(self.page.screenshot(), name="Setup", attachment_type=allure.attachment_type.PNG)
        self.accept_cookie_button.click()
    
    @allure.step("Check Crown Jackpot")
    def click_on_crown(self):
        try:
            self.crown_button.click()
            expect(self.crown_banner).to_be_visible(timeout=9000)
            allure.attach(self.page.screenshot(), name="Crown transfer", attachment_type=allure.attachment_type.PNG)
            self.page.go_back()
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Crown transfer (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Crown Jackpot transfer failed")

        
    #_______________________________________________________________________________________________________
    
    
    @allure.step("Check Shield Jackpot")
    def click_on_shield(self):
        try:
            self.shield_button.click()
            expect(self.shield_banner).to_be_visible(timeout=9000)
            allure.attach(self.page.screenshot(), name="Shiel jackpot transfer", attachment_type=allure.attachment_type.PNG)
            self.page.go_back()
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Shield jackpot transfer (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Shield Jackpot transfer failed")

    #_______________________________________________________________________________________________________
    
            
    @allure.step("Check Shield Jackpot")
    def click_on_sword(self):
        try:
            self.shield_button.click()
            expect(self.sword_banner).to_be_visible(timeout=9000)
            allure.attach(self.page.screenshot(), name="Sword jacktop transfer", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Sword jacktop transfer (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError("Sword Jackpot transfer failed")



