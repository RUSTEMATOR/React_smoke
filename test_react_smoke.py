import allure
import pytest
# from playwright.sync_api import Page
from Suites.Login_reg.login_suite import SuiteLogIn
from Suites.Deposit.deposit_case import SuiteHeader
# from Suites.Search_bar.search_bar_case import SearchBar
# from Suites.Negative_registration.test_negative_registration import TestData
# from Suites.Negative_registration.test_negative_registration import NegativeReg
from Suites.Login_reg.negative_login_suite import NegativeLogin
from Suites.Login_reg.negative_login_suite import TestData_login
from Suites.Jackpot.jackpot_suite import JackpotBanners
# from Suites.Burger_menu.burger_menu_suite import BurgerMenu
# from Suites.Promo.promo_suite import PromoCards
# from Suites.API.api_requests import test_url_response
# from Suites.Providers.providers_suite import ProvidersTest
# from Suites.Providers.providers_suite import TestDataProviders
# from Suites.Game_categories.game_categories_suite_en import CategorieTestEn, TestDataCategoriesEn
from Suites.Info_center.info_center_suite import InfoCenter
from Suites.Login_reg.registrstion_suite import Registration


@allure.suite("Registration")
def test_registration(playwright):
    registration = Registration(playwright)
    registration.set_up_no_login()
    registration.open_registration()
    registration.fillin_login()
    registration.fillin_password()
    registration.adult_checkbox()
    registration.create_account()
    registration.notification_check()

# @allure.suite("Log in")
# def test_login_duite(playwright):
#     suite_login = SuiteLogIn(playwright)
#     suite_login.set_up_no_login()
#     suite_login.open_signin_form()
#     suite_login.enter_valid_data()
#     suite_login.press_login()

# @allure.suite("Header suite")
# def test_deposit(playwright):
#     case_deposit = SuiteHeader(playwright)
#     case_deposit.set_up()
#     case_deposit.press_deposit()
#     case_deposit.options_check()
#     case_deposit.close_deposit()
#     case_deposit.open_players_profile()
#     case_deposit.check_deposit_tab()

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
# def test_negativelogin(playwright, email: str, password: str) -> None:
#     negative_log = NegativeLogin(playwright)
#     negative_log.test_negativelogin(playwright, email, password)
#
#
# @allure.suite("Jackpot banners suite")
# def test_jackpot_banners(playwright):
#     jackpot_banners = JackpotBanners(playwright)
#     jackpot_banners.set_up()
#     jackpot_banners.click_on_crown()
#     jackpot_banners.click_on_shield()
#     jackpot_banners.click_on_sword()

    

# @allure.suite("Burger menu suite")
# def test_burger_menu(playwright):
#     burger_menu = BurgerMenu(playwright)
#     burger_menu.set_up()
#     burger_menu.open_burger_menu()
#     burger_menu.open_promotions()
#     burger_menu.open_tournaments()
#     burger_menu.open_vip()
#     burger_menu.open_banking()
#     burger_menu.open_jackpots()
#     burger_menu.open_legend()


# @allure.suite("Promo cards")
# def test_promo_cards(page):
#     promo = PromoCards(page)
#     promo.open_page()
#
# @allure.suite("Info_center")
# def test_info_center(playwright):
#     info_center = InfoCenter(playwright)
#     info_center.set_up()
#     info_center.open_banking_page()
#     info_center.open_casino_faq()
#     info_center.open_casino_dictionary()
#     info_center.open_crypto_page()
#     info_center.open_complaints()
#     info_center.open_terms_and_C()
#     info_center.open_privacy_policy()
#     info_center.open_responsible_gaming()
#     info_center.open_support()
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


        
