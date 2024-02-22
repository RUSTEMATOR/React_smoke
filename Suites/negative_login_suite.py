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

    links = [
        "kingbillycasino.com"
    ]

class NegativeLogin(TestData_login):
    
    def __init__(self, page: Page):
        self.page = page
        
    @allure.title("Negative emails_check")
    # Define the test function
    @pytest.mark.parametrize("email, password", zip(TestData_login.emails, TestData_login.passwords))
    def test_negativelogin(self, page: Page, email: str, password: str) -> None:
        self.page.goto("https://www.kingbillycasino.com/")
        self.page.get_by_role("link", name="sign in").click()
        self.page.get_by_placeholder("your e-mail address").fill(email)
        self.page.get_by_placeholder("your password").click()
        self.page.get_by_placeholder("your password").fill(password)
        self.page.get_by_role("button", name="sign in").click()
        time.sleep(3)
        
        if self.page.get_by_role("link", name="GET BONUS").is_visible():
            raise AssertionError("Test failed: Sign in is successful.")
        else:
            print("Test passed: Login is not possible.")
