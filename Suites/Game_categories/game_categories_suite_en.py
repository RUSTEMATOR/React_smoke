import pytest
import time
from playwright.sync_api import Playwright, sync_playwright, expect, Page
import allure
import re
from Suites.Base.base_setup import BaseSetUp

class TestDataCategoriesEn():
    categorie_name_en = ["New", "Top", "Popular", "Slots", "Live", "Table games"]
    dropdown_slot_item = ["Accumulating", "Bonus buy", "Megaways", "Exclusive", "Crash"]
    dropdown_live_item = ["Live blackjack", "Live roulette", "Live baccarat", "Live poker"]
    dropdown_table_item = ["Online roulette", "Online blackjack", "Online baccarat"]

class CategorieTestEn(BaseSetUp):

        
    @pytest.mark.parametrize("categorie_name_en", TestDataCategoriesEn.categorie_name_en)
    @allure.suite("Categories Checks")
    def test_game_categories_en(self, categorie_name_en: str) -> None:
        super().set_up()
        self.accept_cookie_button.click()
        try:
            if self.page.get_by_role("link", name=categorie_name_en, exact=True).first.is_visible():
                self.page.get_by_role("link", name=categorie_name_en, exact=True).first.click()
                self.page.locator(".game__action").first.click()
            else:
                self.page.get_by_role("link", name=categorie_name_en).first.click()
                self.page.locator(".game__action").first.click()
                
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        finally:
                self.page.mouse.move(32, 380)
                time.sleep(5)
                self.verify_the_page_loaded()
                allure.attach(self.page.screenshot(), name="Game screenshot", attachment_type=allure.attachment_type.PNG)
                
      #_______________________________________________________________________________________________          
                
    def verify_the_page_loaded(self):
        
        try:
            self.page.get_by_role("button", name=" New online games").click()
            self.page.get_by_role("button", name=" Recently played").click()
            self.page.get_by_role("button", name=" favorite games").click()
            self.page.get_by_role("button", name=" Top Winners").click()
            self.page.get_by_role("button", name=" Last Winners").click()
            self.page.get_by_role("button", name=" Jackpot Games").click()
            self.page.get_by_role("button", name=" Support").click()
            self.page.get_by_role("button", name=" Jackpot Games").click()
            self.page.get_by_role("button", name=" Notifications").click()
            self.page.get_by_role("button", name=" Notifications").click()
            self.page.locator('span.game-auth__btn-text').click()
        except Exception as e:
            allure.attach(self.page.screenshot(), name="Exception Details", attachment_type=allure.attachment_type.PNG)
        
        
        #____________________________________________________________________________________________________________
        
    def test_lobby_category(self):
        super().set_up()
        self.page.get_by_role("button", name="accept").click()
        self.page.locator("a").filter(has_text="Lobby").nth(2).click()
        time.sleep(3)
        try: 
            self.page.locator(".game__action").first.click()
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        finally:
                self.page.mouse.move(32, 380)
                time.sleep(5)
                self.verify_the_page_loaded()
                allure.attach(self.page.screenshot(), name="Game screenshot", attachment_type=allure.attachment_type.PNG)
            
    #_________________________________________________________________________________________________________________
            
    @pytest.mark.parametrize("dropdown_item", TestDataCategoriesEn.dropdown_slot_item)
    def test_game_dropdowns_slots_en(self, dropdown_item: str) -> None:
        super().set_up()
        self.accept_cookie_button.click()
        self.page.locator("a").filter(has_text="Slots").nth(1).click()
        self.page.locator("a").filter(has_text="Slots").nth(1).click()
        time.sleep(2)
        
        self.page.locator("div:nth-child(16) > div > .game-category-menu-v2__item > .game-category-helper > .game-category-helper__item > .game-category-helper__btn").click()
        self.page.get_by_text(dropdown_item, exact=True).click()
        time.sleep(3)
        try: 
            self.page.locator(".game__action").first.click()
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        finally:
                self.page.mouse.move(32, 380)
                time.sleep(5)
                self.verify_the_page_loaded()
                allure.attach(self.page.screenshot(), name="Game screenshot", attachment_type=allure.attachment_type.PNG)
                
                
        #_____________________________________________________________________________________________________________________________________________
        
    @pytest.mark.parametrize("dropdown_item", TestDataCategoriesEn.dropdown_live_item)
    def test_game_dropdowns_live_en(self, dropdown_live_item: str) -> None:
        super().set_up()
        self.accept_cookie_button.click()
        self.page.locator("a").filter(has_text=re.compile(r"^Live$")).nth(1).click()
        self.page.locator("a").filter(has_text=re.compile(r"^Live$")).nth(1).click()
        time.sleep(2)
        self.page.locator("div.slick-slide.slick-active.slick-current > div > div > div > div > button").click()
        self.page.get_by_role('link', name=dropdown_live_item).click()
        time.sleep(3)
        try:

            self.page.locator(".game__action").first.click()
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        finally:
                self.page.mouse.move(32, 380)
                time.sleep(5)
                self.verify_the_page_loaded()
                allure.attach(self.page.screenshot(), name="Game screenshot", attachment_type=allure.attachment_type.PNG)
                
#__________________________________________________________________________________________________________________________________________


    @pytest.mark.parametrize("dropdown_item", TestDataCategoriesEn.dropdown_table_item)
    def test_game_dropdowns_table_en(self, dropdown_table_item: str) -> None:
        super().set_up()
        self.accept_cookie_button.click()
        self.page.locator("a").filter(has_text="Table games").nth(1).click()
        self.page.locator("a").filter(has_text="Table games").nth(1).click()
        time.sleep(2)
        self.page.locator("div.slick-slide.slick-active.slick-current > div > div > div > div > button").click()
        self.page.get_by_role("link", name=dropdown_table_item).first.click()
        time.sleep(3)
        try: 
            self.page.locator(".game__action").first.click()
        except Exception as e:
            allure.attach(self.page.screenshot(e), name="Exception Details", attachment_type=allure.attachment_type.PNG)
            raise AssertionError
        finally:
                self.page.mouse.move(32, 380)
                time.sleep(5)
                self.verify_the_page_loaded()
                allure.attach(self.page.screenshot(), name="Game screenshot", attachment_type=allure.attachment_type.PNG)