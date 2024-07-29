import re
import time
import allure
import pdb
from contextlib import contextmanager
from playwright.sync_api import Locator, expect
from Suites.Locators import Locators
from Data.testinfo import TestInfo
from Suites.Base.base_setup import BaseSetUp
from Suites.Base.base_info import BaseInfo

@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")


@allure.suite("Burger menu")
class BurgerMenu(BaseSetUp, BaseInfo):
    
    def set_up(self):
        try:
            super().set_up()
            self.accept_cookie_button.click()
        except Exception as e:
            raise AssertionError from e

    
    # @allure.step("Open burger menu")
    # def open_burger_menu(self):
    #     try:
    #         self.burger_menu.click()
    #         time.sleep(1)
    #         allure.attach(self.page.screenshot(), name="Burger menu opened", attachment_type=allure.attachment_type.PNG)
    #     except Exception as e:
    #         allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
    #         allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
    #         allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
    
    @allure.step("Check Promotions page")
    def open_promotions(self):
        try:
            self.promotions_page_sidebar.click()
            expect(self.cashback_card).to_be_visible()
            allure.attach(self.page.screenshot(), name="Promotions page is open", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening promotions page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

            
    
    @allure.step("Open Tournament page")
    def open_tournaments(self):
        try:
            self.tournament_page.click()
            expect(self.tournament_banner).to_be_visible()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Tournament page is opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url == self.tournaments_url:
               pass
            else:
                raise AssertionError()

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()


            
    @allure.step("Open VIP page")
    def open_vip(self):
        try:
            self.vip_page.click()
            allure.attach(self.page.screenshot(), name="VIP page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url == self.vip_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    
    @allure.step("Open banking")
    def open_banking(self):
        try:
            self.banking_page.click()
            expect(self.banking_item).to_be_visible()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Banking page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url == self.banking_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    
    
    @allure.step("Open Jackpots")
    def open_jackpots(self):
        try:
            self.jackpot_page.click()
            expect(self.shield_jackpot).to_be_visible()
            allure.attach(self.page.screenshot(), name="Jackpot page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url == self.jackpots_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening jackpot (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()

    
    
    @allure.step("Open Legend")
    def open_legend(self):
        try:
            self.legend_page.click()
            expect(self.legend_title).to_be_visible()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Legend page opened", attachment_type=allure.attachment_type.PNG)

            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening legend page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
            raise AssertionError()
        