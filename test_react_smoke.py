from index import (allure, pytest, Registration, SuiteHeader, SearchBar, SuiteLogIn, NegativeReg, NegativeLogin,
                   JackpotBanners, TestData, TestDataCategoriesEn, TestData_login, CategorieTestEn,
                   PromoCards, InfoCenter, BurgerMenu)

from qase.pytest import qase

@qase.suite('Registration')
@qase.title('Registration test positive')
@allure.suite("Registration")
def test_registration(playwright):
    registration = Registration(playwright)
    try:
        registration.set_up_no_login()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.open_registration()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.fillin_login()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.fillin_password()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.adult_checkbox_check()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.create_account()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.notification_check()
        qase.attach((registration.page.screenshot(), "image/png", "result.png"))
        registration.browser.close()
    except Exception as e:
        registration.browser.close()
        raise AssertionError("Test failed")

@qase.suite('Log in')
@qase.title('Login positive tet')
@allure.suite("Log in")
def test_login_duite(playwright):
    suite_login = SuiteLogIn(playwright)
    try:
        suite_login.set_up_no_login()
        qase.attach((suite_login.page.screenshot(), "image/png", "result.png"))
        suite_login.open_signin_form()
        qase.attach((suite_login.page.screenshot(), "image/png", "result.png"))
        suite_login.enter_valid_data()
        qase.attach((suite_login.page.screenshot(), "image/png", "result.png"))
        suite_login.press_login()
        qase.attach((suite_login.page.screenshot(), "image/png", "result.png"))
        suite_login.browser.close()
    except Exception as e:
        suite_login.browser.close()
        raise AssertionError("Test failed")


@qase.suite('Header')
@qase.title('Deposit')
@allure.suite("Header suite")
def test_deposit(playwright):
    case_deposit = SuiteHeader(playwright)
    try:
        case_deposit.set_up()
        qase.attach((case_deposit.page.screenshot(), "image/png", "result.png"))
        case_deposit.press_deposit()
        qase.attach((case_deposit.page.screenshot(), "image/png", "result.png"))
        case_deposit.options_check()
        qase.attach((case_deposit.page.screenshot(), "image/png", "result.png"))
        case_deposit.close_deposit()
        qase.attach((case_deposit.page.screenshot(), "image/png", "result.png"))
        case_deposit.open_players_profile()
        qase.attach((case_deposit.page.screenshot(), "image/png", "result.png"))
        case_deposit.check_deposit_tab()
        qase.attach((case_deposit.page.screenshot(), "image/png", "result.png"))
        case_deposit.browser.close()
    except Exception as e:
        case_deposit.browser.close()
        raise AssertionError("Test failed")



@qase.suite('Header')
@qase.title('Searchbar')
@allure.suite("Header suite")
def test_searchbar(playwright):
    search_bar_case = SearchBar(playwright)
    try:
        search_bar_case.set_up()
        qase.attach((search_bar_case.page.screenshot(), "image/png", "result.png"))
        search_bar_case.click_on_search()
        qase.attach((search_bar_case.page.screenshot(), "image/png", "result.png"))
        search_bar_case.enter_firelightning()
        qase.attach((search_bar_case.page.screenshot(), "image/png", "result.png"))
        search_bar_case.go_back()
        qase.attach((search_bar_case.page.screenshot(), "image/png", "result.png"))
        search_bar_case.browser.close()
    except:
        search_bar_case.browser.close()
        raise AssertionError("Test failed")

@qase.suite('Negative registration')
@qase.title('Registration test negative')
@allure.suite("Negative registration")
@pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
def test_negativereg(playwright, email):
    negative_reg = NegativeReg(playwright)
    try:
        negative_reg.test_negative_registration(email)
        qase.attach((negative_reg.page.screenshot(), "image/png", "result.png"))
        negative_reg.browser.close()
    except AssertionError as e:
        negative_reg.browser.close()
        raise AssertionError("Test failed")
@qase.suite('Negative login')
@qase.title('Login test negative')
@allure.suite("Negative login")
@pytest.mark.parametrize("email, password", zip(TestData_login.emails, TestData_login.passwords))
def test_negativelogin(playwright, email: str, password: str) -> None:
    negative_log = NegativeLogin(playwright)
    try:
        negative_log.test_negativelogin(email, password)
        qase.attach((negative_log.page.screenshot(), "image/png", "result.png"))
        negative_log.browser.close()
    except AssertionError as e:
        negative_log.browser.close()
        raise AssertionError("Test failed")

@qase.suite('Jackpot banners suite')
@qase.title('JackpotBanners')
@allure.suite("Jackpot banners suite")
def test_jackpot_banners(playwright):
    jackpot_banners = JackpotBanners(playwright)
    try:
        jackpot_banners.set_up()
        qase.attach((jackpot_banners.page.screenshot(), "image/png", "result.png"))
        jackpot_banners.click_on_crown()
        qase.attach((jackpot_banners.page.screenshot(), "image/png", "result.png"))
        jackpot_banners.click_on_shield()
        qase.attach((jackpot_banners.page.screenshot(), "image/png", "result.png"))
        jackpot_banners.click_on_sword()
        qase.attach((jackpot_banners.page.screenshot(), "image/png", "result.png"))
        jackpot_banners.browser.close()
    except:
        jackpot_banners.browser.close()
        raise AssertionError("Test failed")



@qase.suite('Burger menu')
@qase.title('Burger Menu')
@allure.suite("Burger menu suite")
def test_burger_menu(playwright):
    burger_menu = BurgerMenu(playwright)
    try:
        burger_menu.set_up()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        #burger_menu.open_burger_menu()
        burger_menu.open_promotions()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        burger_menu.open_tournaments()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        burger_menu.open_vip()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        burger_menu.open_banking()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        burger_menu.open_jackpots()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        burger_menu.open_legend()
        qase.attach((burger_menu.page.screenshot(), "image/png", "result.png"))
        burger_menu.browser.close()
    except:
        burger_menu.browser.close()
        raise AssertionError("Test failed")

@qase.suite('Promo cards')
@qase.title('Promo cards')
@allure.suite("Promo cards")
def test_promo_cards(playwright):
    promo = PromoCards(playwright)
    try:
        promo.set_up()
        promo.press_getit()
        qase.attach((promo.page.screenshot(), "image/png", "result.png"))
        promo.open_promotions()
        qase.attach((promo.page.screenshot(), "image/png", "result.png"))
        promo.press_on_i()
        qase.attach((promo.page.screenshot(), "image/png", "result.png"))
        promo.close_modal()
        qase.attach((promo.page.screenshot(), "image/png", "result.png"))
        promo.click_on_GetIt()
        qase.attach((promo.page.screenshot(), "image/png", "result.png"))
        promo.browser.close()

    except:
        promo.browser.close()
        raise AssertionError("Test failed")

@qase.suite('Info center')
@qase.title('Info center')

@allure.suite("Info_center")
def test_info_center(playwright):
    info_center = InfoCenter(playwright)
    try:
        info_center.set_up()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_banking_page()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_casino_faq()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_casino_dictionary()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_crypto_page()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_complaints()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_terms_and_C()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_privacy_policy()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_responsible_gaming()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.open_support()
        qase.attach((info_center.page.screenshot(), "image/png", "result.png"))
        info_center.browser.close()
    except:
        info_center.browser.close()
        raise AssertionError("Test failed")



@qase.suite("Category check")
@qase.title(f'{TestDataCategoriesEn.categorie_name_en}')
@pytest.mark.parametrize("categorie_name_en", TestDataCategoriesEn.categorie_name_en)
@allure.suite("Category check")
def test_game_category(playwright, categorie_name_en):
    category = CategorieTestEn(playwright)
    try:
        category.test_game_categories_en(categorie_name_en)
        qase.attach((category.page.screenshot(), "image/png", "result.png"))
        category.browser.close()
    except:
        category.browser.close()
        raise AssertionError("Test failed")
@qase.suite("Category check")
@qase.title('Lobby category')
@allure.suite("Category check")
def test_lobby_category(playwright):
    category = CategorieTestEn(playwright)
    qase.attach((category.page.screenshot(), "image/png", "result.png"))
    try:
        category.test_lobby_category()
        category.browser.close()
    except:
        category.browser.close()
        raise AssertionError("Test failed")

@qase.suite("Category check")
@qase.title('Dropdown slots category')
@allure.suite("Category check")
@pytest.mark.parametrize("dropdown_slot_item", TestDataCategoriesEn.dropdown_slot_item)
def test_dropdowns_categorie(playwright, dropdown_slot_item):
    dropdowns = CategorieTestEn(playwright)
    try:
        dropdowns.test_game_dropdowns_slots_en(dropdown_slot_item)
        qase.attach((dropdowns.page.screenshot(), "image/png", "result.png"))
        dropdowns.browser.close()
    except:
        dropdowns.browser.close()
        raise AssertionError("Test failed")

@qase.suite('Category check')
@qase.title('Dropdown live')
@allure.suite("Category check")
@pytest.mark.parametrize("dropdown_live_item", TestDataCategoriesEn.dropdown_live_item)
def test_dropdowns_live_categorie(playwright, dropdown_live_item):
    dropdowns = CategorieTestEn(playwright)
    try:

        dropdowns.test_game_dropdowns_live_en(dropdown_live_item)
        qase.attach((dropdowns.page.screenshot(), "image/png", "result.png"))
        dropdowns.browser.close()
    except:
        dropdowns.browser.close()
        dropdowns.page.screenshot()
        raise AssertionError("Test failed")

@qase.suite('Category check')
@qase.title('Dropdown table')
@allure.suite("Category check")
@pytest.mark.parametrize("dropdown_table_item", TestDataCategoriesEn.dropdown_table_item)
def test_table_categorie(playwright, dropdown_table_item):
    dropdowns = CategorieTestEn(playwright)
    try:
        dropdowns.test_game_dropdowns_table_en(dropdown_table_item)
        qase.attach((dropdowns.page.screenshot(), "image/png", "result.png"))
        dropdowns.browser.close()
    except:
        dropdowns.browser.close()
        raise AssertionError("Test failed")


# @allure.suite("Providers Check")
# @pytest.mark.parametrize("provider_name", TestDataProviders.provider_names)
# def test_check_providers(playwright, provider_name):
#     providers = ProvidersTest(playwright)
#     try:
#         providers.test_provider_play(provider_name)
#         providers.browser.close()
#     except:
#         providers.browser.close()
#         raise AssertionError("Test failed")



