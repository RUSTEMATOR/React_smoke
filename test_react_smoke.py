import allure
import pytest
import time
from contextlib import contextmanager
from playwright.sync_api import sync_playwright, Page
from Suites.login_suite import SuiteLogIn
from Suites.deposit_case import SuiteHeader
from Suites.search_bar_case import SearchBar
from Suites.Negative_registration.test_negative_registration import TestData
from Suites.Negative_registration.test_negative_registration import NegativeReg
from Suites.negative_login_suite import NegativeLogin
from Suites.negative_login_suite import TestData_login
from Suites.jackpot_suite import JackpotBanners
from Suites.burger_menu_suite import BurgerMenu
from Suites.promo_suite import PromoCards


@allure.suite("Log in")
def test_login_duite(page):
    suite_login = SuiteLogIn(page)
    suite_login.open_page()

@allure.suite("Header suite")
def test_deposit(page):
    case_deposit = SuiteHeader(page)
    case_deposit.open_page()


@allure.suite("Header suite")
def test_searchbar(page):
    search_bar_case = SearchBar(page)
    search_bar_case.open_page()

@allure.suite("Negative registration")
@pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
def test_negativereg(page, email):
    negative_reg = NegativeReg(page)
    negative_reg.test_negative_registration(page, email)

@allure.suite("Negative login")
@pytest.mark.parametrize("email, password", zip(TestData_login.emails, TestData_login.passwords))
def test_negativelogin(page: Page, email: str, password: str) -> None:
    negative_log = NegativeLogin(page)
    negative_log.test_negativelogin(page, email, password)
    

@allure.suite("Jackpot banners suite")
def test_jackpot_banners(page):
    jackpot_banners = JackpotBanners(page)
    jackpot_banners.open_page()
    

@allure.suite("Burger menu suite")
def test_burger_menu(page):
    burger_menu = BurgerMenu(page)
    burger_menu.open_page()

@allure.suite("Promo cards")
def test_promo_cards(page):
    promo = PromoCards(page)
    promo.open_page()
    
    
