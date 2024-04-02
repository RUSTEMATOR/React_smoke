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


@allure.suite("Burger menu")
class BurgerMenu(TestData):
    
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
            self.open_burger_menu()
    
    @allure.step("Open burger menu")
    def open_burger_menu(self):
        try:
            burger_menu = self.page.locator('.burger__slide')
            burger_menu.first.click()
            time.sleep(1)
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
        expected_promotions_url = "https://www.kingbillycasino.com/promotions"
        try:
            promotions_page = self.page.locator("#bar").get_by_role("link", name="Promotions")
            promotions_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Promotions page is open", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url() == expected_promotions_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening promotions page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        
        finally:
            self.open_tournaments()
            
    
    @allure.step("Open Tournament page")
    def open_tournaments(self):
        expected_tournaments_url = "https://www.kingbillycasino.com/tournaments"
        self.page.get_by_role("banner").get_by_role("button").first.click()
        try:
            tournament_page = self.page.locator("#bar").get_by_role("link", name="Tournaments")
            tournament_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Tournament page is opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url() == expected_tournaments_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.open_vip()
            
    @allure.step("Open VIP page")
    def open_vip(self):
        expected_vip_url = "https://www.kingbillycasino.com/vip-club"
        self.page.get_by_role("banner").get_by_role("button").first.click()
        try:
            vip_page = self.page.locator("#bar").get_by_role("link", name="VIP")
            vip_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="VIP page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url() == expected_vip_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.open_banking()
    
    @allure.step("Open banking")
    def open_banking(self):
        expected_banking_url = "https://www.kingbillycasino.com/online-casino-payments"
        self.page.get_by_role("banner").get_by_role("button").first.click()
        try:
            banking_page = self.page.locator("#bar").get_by_role("link", name="Banking")
            banking_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Banking page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url() == expected_banking_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening burger menu (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.open_jackpots()
    
    
    @allure.step("Open Jackpots")
    def open_jackpots(self):
        expected_jackpots_url = "https://www.kingbillycasino.com/jackpots"
        self.page.get_by_role("banner").get_by_role("button").first.click()
        try:
            jackpot_page = self.page.get_by_role("link", name="Jackpots", exact=True)
            jackpot_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Jackpot page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url() == expected_jackpots_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening jackpot (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        finally:
            self.open_legend()
    
    
    @allure.step("Open Legend")
    def open_legend(self):
        expected_legend_url = "https://www.kingbillycasino.com/jackpots"
        self.page.get_by_role("button", name="accept").click()
        self.page.get_by_role("banner").get_by_role("button").first.click()    
        try:
            legend_page = self.page.locator("#bar").get_by_role("link", name="Legend")
            legend_page.click()
            time.sleep(1)
            allure.attach(self.page.screenshot(), name="Legend page opened", attachment_type=allure.attachment_type.PNG)
            
            if self.page.url() == expected_legend_url:
               pass
            else:
                raise AssertionError()
            
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Opening legend page (Failed)", attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)
        