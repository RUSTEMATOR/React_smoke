import allure
# import pytest
# from playwright.sync_api import Page
# from Suites.Login_reg.login_suite import SuiteLogIn
# from Suites.Deposit.deposit_case import SuiteHeader
# from Suites.Search_bar.search_bar_case import SearchBar
# from Suites.Negative_registration.test_negative_registration import TestData
# from Suites.Negative_registration.test_negative_registration import NegativeReg
# from Suites.Login_reg.negative_login_suite import NegativeLogin
# from Suites.Login_reg.negative_login_suite import TestData_login
# from Suites.Jackpot.jackpot_suite import JackpotBanners
from Suites.Burger_menu.burger_menu_suite import BurgerMenu
# from Suites.Promo.promo_suite import PromoCards
# from Suites.API.api_requests import test_url_response
# from Suites.Providers.providers_suite import ProvidersTest
# from Suites.Providers.providers_suite import TestDataProviders
# from Suites.Game_categories.game_categories_suite_en import CategorieTestEn, TestDataCategoriesEn
# from Suites.Info_center.info_center_suite import InfoCenter
# from Suites.Login_reg.registrstion_suite import Registration


# @allure.suite("Registration")
# def test_registration(page):
#     registration = Registration(page)
#     registration.open_site()
#
# @allure.suite("Log in")
# def test_login_duite(page):
#     suite_login = SuiteLogIn(page)
#     suite_login.open_page()
#
# @allure.suite("Header suite")
# def test_deposit(page):
#     case_deposit = SuiteHeader(page)
#     case_deposit.open_page()
#
#
# @allure.suite("Header suite")
# def test_searchbar(page):
#     search_bar_case = SearchBar(page)
#     search_bar_case.open_page()
#
# @allure.suite("Negative registration")
# @pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
# def test_negativereg(page, email):
#     negative_reg = NegativeReg(page)
#     negative_reg.test_negative_registration(page, email)
#
# @allure.suite("Negative login")
# @pytest.mark.parametrize("email, password", zip(TestData_login.emails, TestData_login.passwords))
# def test_negativelogin(page: Page, email: str, password: str) -> None:
#     negative_log = NegativeLogin(page)
#     negative_log.test_negativelogin(page, email, password)
#
#
# @allure.suite("Jackpot banners suite")
# def test_jackpot_banners(page):
#     jackpot_banners = JackpotBanners(page)
#     jackpot_banners.open_page()
    

@allure.suite("Burger menu suite")
def test_burger_menu(playwright):
    burger_menu = BurgerMenu(playwright)
    burger_menu.set_up()
    burger_menu.open_burger_menu()


# @allure.suite("Promo cards")
# def test_promo_cards(page):
#     promo = PromoCards(page)
#     promo.open_page()
#
# @allure.suite("Info_center")
# def test_info_center(page):
#     info_center = InfoCenter(page)
#     info_center.open_page()
#
#
# @pytest.mark.parametrize("categorie_name_en", TestDataCategoriesEn.categorie_name_en)
# @allure.suite("Category check")
# def test_game_category(page, categorie_name_en):
#     category = CategorieTestEn(page)
#     category.test_game_categories_en(categorie_name_en)
#
# @allure.suite("Category check")
# def test_lobby_category(page):
#     category = CategorieTestEn(page)
#     category.test_lobby_category()
#
# @allure.suite("Category check")
# @pytest.mark.parametrize("dropdown_slot_item", TestDataCategoriesEn.dropdown_slot_item)
# def test_dropdowns_categorie(page, dropdown_slot_item):
#     dropdowns = CategorieTestEn(page)
#     dropdowns.test_game_dropdowns_slots_en(dropdown_slot_item)
#
#
# @allure.suite("Category check")
# @pytest.mark.parametrize("dropdown_live_item", TestDataCategoriesEn.dropdown_live_item)
# def test_dropdowns_live_categorie(page, dropdown_live_item):
#     dropdowns = CategorieTestEn(page)
#     dropdowns.test_game_dropdowns_live_en(dropdown_live_item)
#
# @allure.suite("Category check")
# @pytest.mark.parametrize("dropdown_table_item", TestDataCategoriesEn.dropdown_table_item)
# def test_table_categorie(page, dropdown_table_item):
#     dropdowns = CategorieTestEn(page)
#     dropdowns.test_game_dropdowns_table_en(dropdown_table_item)
#
# @allure.suite("API Checks")
# @pytest.fixture(scope="function")
# def check_urls():
#     # Add your code here to perform URL testing
#     urls = [
#         "https://www.kingbillycasino6.com/de",
#     ]
#     for url in urls:
#         test_url_response(url)
#
# @allure.suite("Providers Check")
# @pytest.mark.parametrize("provider_name", TestDataProviders.provider_names)
# def test_check_providers(page: Page, provider_name):
#     providers = ProvidersTest(page)
#     providers.test_provider_play(provider_name)


        
