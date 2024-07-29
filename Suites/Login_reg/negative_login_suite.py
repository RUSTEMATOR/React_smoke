from playwright.sync_api import Page, expect, Playwright
from Suites.Base.base_setup import BaseSetUp
import pytest
import allure
from contextlib import contextmanager

@contextmanager
def allure_step(name):
    try:
        yield
    except AssertionError as e:
        raise AssertionError(f"{name} failed: {str(e)}")

class TestData_login():
    from playwright.sync_api import Page

    # Define the list of test data
    emails = [
        "samoilenkofluttershy@gmail.com",
        "",
        "lololololo",
        "example@kbc.pp..ua",
        "samoilenkofluttershy@gmail.com",
    ]

    passwords = [
        "",
        "193786Az.",
        "fa",
        "",
        "8is887dus7",
    ]

class NegativeLogin(TestData_login, BaseSetUp):
        
    @allure.title("Negative emails_check")
    # Define the test function
    @pytest.mark.parametrize("email, password", zip(TestData_login.emails, TestData_login.passwords))
    def test_negativelogin(self, email: str, password: str) -> None:
        super().set_up_no_login()
        self.page.get_by_role("link", name="sign in").click()
        self.page.get_by_placeholder("your e-mail address").fill(email)
        self.page.get_by_placeholder("your password").click()
        self.page.get_by_placeholder("your password").fill(password)
        self.page.get_by_role("button", name="sign in").click()

        expect(self.page.get_by_role("link", name="GET BONUS")).not_to_be_visible()
        self.browser.close()
