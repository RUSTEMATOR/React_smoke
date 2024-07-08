from playwright.sync_api import Playwright, sync_playwright, Page
import pytest
import allure
import time
from contextlib import contextmanager
@contextmanager
def allure_step(name, page):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")

class TestData():
    from playwright.sync_api import Page
# Define the list of test data
    test_data = [
        "example#kbc.pp.ua",
        "example@kbc.pp-ua",
        "example@kbc.pp_ua",
        "example@kbc.pp..ua",
        "",  # Empty value
        "exämple@kbc.pp.ua",
        "example@softs_wis..com",
        "example.softswis.com",
        "example@@softswis.com",
        "example@soft swis.com",
        "example@softswis..com",
        "example@"
    ]

    links = [
    "kingbillycasino.com"
]

class NegativeReg(TestData):
    
    def __init__(self, page: Page):
        self.page = page
        
    @allure.title("Negative emails_check")
    # Define the test function
    @pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
    def test_negative_registration(self, page: Page, email: str, kingbillysite) -> None:
        self.page.goto(kingbillysite)
        self.page.get_by_role("button", name="accept").click()
        self.page.get_by_role("link", name="Create account").click()
        self.page.locator("#registration-dynamic-form__email").click()
        self.page.locator("#registration-dynamic-form__email").fill(email)
        self.page.locator("#registration-dynamic-form__password_single").fill("193786Az()")
        self.page.locator("#sign-up label").filter(has_text="I am 18 years old and I accept the Privacy Policy and Terms and Conditions *").click()
        create_account_button = self.page.locator("#sign-up").get_by_role("button", name="Create account")

        if create_account_button.is_enabled():
            raise AssertionError("Test failed: Create account button is clickable.")
        else:
            print("Test passed: Create account button is not clickable.")
        