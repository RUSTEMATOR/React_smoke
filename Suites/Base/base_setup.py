import allure
import allure
import time
from playwright.sync_api import Page, Playwright, expect
from Suites.Locators.Locators import Locators

class BaseSetUp(Locators):

    kingbillysite = "https://www.kingbillycasino.com/"
    promo_link = "https://www.kingbillycasino.com/promotions"
    tournaments_url = "https://www.kingbillycasino.com/tournaments"
    vip_url = "https://www.kingbillycasino.com/vip-club"
    banking_url = "https://www.kingbillycasino.com/online-casino-payments"
    jackpots_url = "https://www.kingbillycasino.com/jackpots"
    legend_url = "https://www.kingbillycasino.com/jackpots"
    login_email = 'samoilenkofluttershy@gmail.com'
    login_password = '193786Az()'


    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
            # proxy={
            #                                           'server': 'http://138.197.150.103:8090',
            #                                           'username': 'kbc',
            #                                           'password': '347SP&Uwqt!2xZ7w',})



        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    @allure.step("Open the page")
    def open_page(self):
        try:
            self.page.goto(self.kingbillysite)
            allure.attach(self.page.screenshot(), name="Page opened", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Page opened (Failed)",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)


    @allure.step("Open Sign in form")
    def open_signin_form(self):
        try:
            self.sign_in_form.click()
            allure.attach(self.page.screenshot(), name="Sign in Form Opened",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Sign in Form Opened (Failed)",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)


    @allure.step("Enter valid data")
    def enter_valid_data(self):
        try:
            self.login_email_field.click()
            self.login_email_field.fill(self.login_email)
            allure.attach(self.page.screenshot(), name="Email Filled", attachment_type=allure.attachment_type.PNG)

            self.login_password_field.click()
            self.login_password_field.fill(self.login_password)
            allure.attach(self.page.screenshot(), name="Password filled", attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Valid data entered (Failed)",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)



    @allure.step("Press Sign in")
    def press_enter(self):
        try:
            self.page.get_by_role("button", name="sign in").click()
            time.sleep(3)

        except Exception as e:
            allure.attach(str(e), name="Exception Details", attachment_type=allure.attachment_type.TEXT)
            allure.attach(self.page.screenshot(), name="Valid data entered (Failed)",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(self.page.content(), name="Page HTML", attachment_type=allure.attachment_type.HTML)

    def set_up(self):
        self.open_page()
        self.open_signin_form()
        self.enter_valid_data()
        self.press_enter()


    def set_up_no_login(self):
        self.open_page()