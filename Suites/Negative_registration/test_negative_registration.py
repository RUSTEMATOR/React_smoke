from playwright.sync_api import Page, Playwright
import pytest
import allure
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

class NegativeReg(TestData):
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False,
                                                  # proxy={
                                                  #     'server': 'http://138.197.150.103:8090',
                                                  #     'username': 'kbc',
                                                  #     'password': '347SP&Uwqt!2xZ7w', }
                                                  )

        self.context = self.browser.new_context(viewport={"width": 1920, "height": 1080})
        self.page = self.context.new_page()
    @allure.title("Negative emails_check")
    # Define the test function
    @pytest.mark.parametrize("email", [(e) for e in TestData.test_data])
    def test_negative_registration(self, email: str) -> None:
        self.page.goto("https://www.kingbillycasino.com/")
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
        