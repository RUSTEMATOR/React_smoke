from index import (allure, pytest, Page, Registration, SuiteHeader, SearchBar, SuiteLogIn, NegativeReg, NegativeLogin,
                   JackpotBanners, TestData, TestDataCategoriesEn, TestDataProviders, TestData_login, CategorieTestEn,
                   PromoCards, InfoCenter, ProvidersTest, BurgerMenu)


@allure.suite("Registration")
def test_registration(playwright):
    registration = Registration(playwright)
    try:
        registration.set_up_no_login()
        registration.open_registration()
        registration.fillin_login()
        registration.fillin_password()
        registration.adult_checkbox_check()
        registration.create_account()
        registration.notification_check()
        registration.browser.close()
    except Exception as e:
        registration.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Log in")
def test_login_duite(playwright):
    suite_login = SuiteLogIn(playwright)
    try:
        suite_login.set_up_no_login()
        suite_login.open_signin_form()
        suite_login.enter_valid_data()
        suite_login.press_login()
        suite_login.browser.close()
    except Exception as e:
        suite_login.browser.close()
        raise AssertionError("Test failed")



@allure.suite("Header suite")
def test_deposit(playwright):
    case_deposit = SuiteHeader(playwright)
    try:
        case_deposit.set_up()
        case_deposit.press_deposit()
        case_deposit.options_check()
        case_deposit.close_deposit()
        case_deposit.open_players_profile()
        case_deposit.check_deposit_tab()
        case_deposit.browser.close()
    except Exception as e:
        case_deposit.browser.close()
        raise AssertionError("Test failed")





@allure.suite("Header suite")
def test_searchbar(playwright):
    search_bar_case = SearchBar(playwright)
    try:
        search_bar_case.set_up()
        search_bar_case.click_on_search()
        search_bar_case.enter_firelightning()
        search_bar_case.go_back()
        search_bar_case.browser.close()
    except:
        search_bar_case.browser.close()
        raise AssertionError("Test failed")

#
@allure.suite("Negative registration")
@pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
def test_negativereg(playwright, email):
    negative_reg = NegativeReg(playwright)
    try:
        negative_reg.test_negative_registration(email)
        negative_reg.browser.close()
    except AssertionError as e:
        negative_reg.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Negative login")
@pytest.mark.parametrize("email, password", zip(TestData_login.emails, TestData_login.passwords))
def test_negativelogin(playwright, email: str, password: str) -> None:
    negative_log = NegativeLogin(playwright)
    try:
        negative_log.test_negativelogin(email, password)
        negative_log.browser.close()
    except AssertionError as e:
        negative_log.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Jackpot banners suite")
def test_jackpot_banners(playwright):
    jackpot_banners = JackpotBanners(playwright)
    try:
        jackpot_banners.set_up()
        jackpot_banners.click_on_crown()
        jackpot_banners.click_on_shield()
        jackpot_banners.click_on_sword()
        jackpot_banners.browser.close()
    except:
        jackpot_banners.browser.close()
        raise AssertionError("Test failed")




@allure.suite("Burger menu suite")
def test_burger_menu(playwright):
    burger_menu = BurgerMenu(playwright)
    try:
        burger_menu.set_up()
        # burger_menu.open_burger_menu()
        burger_menu.open_promotions()
        burger_menu.open_tournaments()
        burger_menu.open_vip()
        burger_menu.open_banking()
        burger_menu.open_jackpots()
        burger_menu.open_legend()
        burger_menu.browser.close()
    except:
        burger_menu.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Promo cards")
def test_promo_cards(playwright):
    promo = PromoCards(playwright)
    try:
        promo.set_up()
        promo.press_getit()
        promo.open_promotions()
        promo.press_on_i()
        promo.close_modal()
        promo.click_on_GetIt()
        promo.browser.close()

    except:
        promo.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Info_center")
def test_info_center(playwright):
    info_center = InfoCenter(playwright)
    try:
        info_center.set_up()
        info_center.open_banking_page()
        info_center.open_casino_faq()
        info_center.open_casino_dictionary()
        info_center.open_crypto_page()
        info_center.open_complaints()
        info_center.open_terms_and_C()
        info_center.open_privacy_policy()
        info_center.open_responsible_gaming()
        info_center.open_support()
        info_center.browser.close()
    except:
        info_center.browser.close()
        raise AssertionError("Test failed")




@pytest.mark.parametrize("categorie_name_en", TestDataCategoriesEn.categorie_name_en)
@allure.suite("Category check")
def test_game_category(playwright, categorie_name_en):
    category = CategorieTestEn(playwright)
    try:
        category.test_game_categories_en(categorie_name_en)
        category.browser.close()
    except:
        category.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Category check")
def test_lobby_category(playwright):
    category = CategorieTestEn(playwright)
    try:
        category.test_lobby_category()
        category.browser.close()
    except:
        category.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Category check")
@pytest.mark.parametrize("dropdown_slot_item", TestDataCategoriesEn.dropdown_slot_item)
def test_dropdowns_categorie(playwright, dropdown_slot_item):
    dropdowns = CategorieTestEn(playwright)
    try:
        dropdowns.test_game_dropdowns_slots_en(dropdown_slot_item)
        dropdowns.browser.close()
    except:
        dropdowns.browser.close()
        raise AssertionError("Test failed")


@allure.suite("Category check")
@pytest.mark.parametrize("dropdown_live_item", TestDataCategoriesEn.dropdown_live_item)
def test_dropdowns_live_categorie(playwright, dropdown_live_item):
    dropdowns = CategorieTestEn(playwright)
    try:
        dropdowns.test_game_dropdowns_live_en(dropdown_live_item)
        dropdowns.browser.close()
    except:
        dropdowns.browser.close()
        raise AssertionError("Test failed")

@allure.suite("Category check")
@pytest.mark.parametrize("dropdown_table_item", TestDataCategoriesEn.dropdown_table_item)
def test_table_categorie(playwright, dropdown_table_item):
    dropdowns = CategorieTestEn(playwright)
    try:
        dropdowns.test_game_dropdowns_table_en(dropdown_table_item)
        dropdowns.browser.close()
    except:
        dropdowns.browser.close()
        raise AssertionError("Test failed")
#
#
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
#
#
#
