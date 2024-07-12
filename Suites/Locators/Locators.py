from playwright.sync_api import Page, expect

class Locators:
    page = Page
    @property
    def sign_in_form(self):
        return self.page.get_by_role("link", name="sign in")

    @property
    def login_email_field(self):
        return self.page.get_by_placeholder("your e-mail address")

    @property
    def login_password_field(self):
        return self.page.get_by_placeholder("your password")

    @property
    def sign_in_button(self):
        return self.page.get_by_role("button", name="sign in")

    @property
    def burger_menu(self):
        return self.page.locator('.burger__slide').first

    @property
    def promotions_page(self):
        return self.page.locator('xpath=//*[@id="bar"]/div[2]/div/div/header/div[2]/ul/li[1]/a/span')
    @property
    def tournament_page(self):
        return self.page.locator("#bar").get_by_role("link", name="Tournaments")

    @property
    def vip_page(self):
        return self.page.locator("#bar").get_by_role("link", name="VIP")

    @property
    def banking_page(self):
        return self.page.locator('xpath=//*[@id="bar"]/div[2]/div/div/header/div[2]/ul/li[4]/a/span')

    @property
    def jackpot_page(self):
        return self.page.get_by_role("link", name="Jackpots", exact=True)

    @property
    def legend_page(self):
        return self.page.locator("#bar").get_by_role("link", name="Legend")

    @property
    def deposit_button(self):
        return self.page.get_by_role("link", name="deposit")

    @property
    def payment_method(self):
        return self.page.locator("div").filter(has_text=(r"^Min €20$")).first

    @property
    def closing_button(self):
        return self.page.get_by_role("button", name="")

    @property
    def sidebar_menu(self):
        return self.page.get_by_role("banner").get_by_role("button").first

    @property
    def profile_unwrapper(self):
        return self.page.locator("#downshift-2-input")

    @property
    def profile_info_button(self):
        return self.page.get_by_role("link", name="Profile info")

    @property
    def wallet_tab(self):
        return self.page.get_by_role("link", name=" Wallet")

    @property
    def deposit_tab(self):
        return self.page.get_by_role("link", name="deposit", exact=True)

    @property
    def bank_transfer(self):
        return self.page.get_by_role("img", name="Banküberweisung")

    @property
    def casino_faq_page(self):
        return self.page.get_by_role("link", name="Casino FAQ")

    @property
    def faq_title(self):
        return self.page.get_by_role("heading", name="CASINO FAQ")

    @property
    def casino_dictionary_page(self):
        return self.page.get_by_role("main").get_by_role("link", name="Casino Dictionary")

    @property
    def dictionary_title(self):
        return self.page.get_by_role("heading", name="KING’S DICTIONARY")

    @property
    def crypto_page(self):
        return self.page.get_by_role("main").get_by_role("link", name="Crypto Currencies FAQ")

    @property
    def crypto_page_title(self):
        return self.page.get_by_role("heading", name="CRYPTO CURRENCIES FAQ")

    @property
    def complaints_page(self):
        return self.page.get_by_role("main").get_by_role("link", name="Complaints")

    @property
    def complaints_title(self):
        return self.page.get_by_role("heading", name="Complaints")

    @property
    def terms_page(self):
        return self.page.get_by_role("main").get_by_role("link", name="Terms and Conditions", exact=True)

    @property
    def terms_title(self):
        return self.page.get_by_role("heading", name="TERMS AND CONDITIONS")

    @property
    def privacy_page(self):
        return self.page.get_by_role("main").get_by_role("link", name="Privacy Policy")

    @property
    def privacy_title(self):
        return self.page.get_by_role("heading", name="PRIVACY POLICY")

    @property
    def responsible_page(self):
        return self.page.get_by_role("main").get_by_role("link", name="Responsible Gaming")

    @property
    def responsible_title(self):
        return self.page.get_by_role("heading", name="Responsible Gaming")

    @property
    def support_page(self):
        return self.page.get_by_role("link", name="Support")

    @property
    def support_title(self):
        return self.page.get_by_role("heading", name="Casino Support")

    @property
    def crown_button(self):
        return self.page.get_by_role("link", name="Crown Jackpot")

    @property
    def shield_button(self):
        return self.page.get_by_role("link", name="Shield Jackpot")

    @property
    def sword_button(self):
        return self.page.get_by_role("link", name="Sword Jackpot")

    @property
    def get_bonus_link(self):
        return self.page.get_by_role("link", name="GET BONUS")

    @property
    def registration_form(self):
        return self.page.get_by_role("link", name="Create account")

    @property
    def login_input(self):
        return self.page.locator("#registration-dynamic-form__email")

    @property
    def password_input(self):
        return self.page.locator("#registration-dynamic-form__password_single")

    @property
    def adult_checkbox(self):
        return self.page.locator("#sign-up label").filter(
            has_text="I am 18 years old and I accept the Privacy Policy and Terms and Conditions *").locator(
            "span").first

    @property
    def promo_checkbox(self):
        return self.page.locator("#sign-up label").filter(has_text="I want to receive promos").locator(
            "span").first

    @property
    def create_account_button(self):
        return self.page.locator("#sign-up").get_by_role("button", name="Create account")

    @property
    def notification(self):
        return self.page.get_by_role("heading",
                                     name="You will receive an email with instructions on how to confirm your email address in a few minutes.")

    @property
    def search_bar(self):
        return self.page.locator("#games-search")

    @property
    def fire_lighnting_button(self):
        return self.page.get_by_title("Fire Lightning")

    @property
    def main_page_button(self):
        return self.page.frame_locator("#root iframe").frame_locator("iframe").locator("#button-back")


    @property
    def burger_slider(self):
        return self.page.locator(".burger__slide")

    @property
    def cashback_card(self):
        return self.page.locator('xpath=//*[@id="root"]/div[2]/main/div/div[2]/div/div[1]/div/div[1]')


    @property
    def accept_cookie_button(self):
        return self.page.locator("#accept_initial_notification_button")

    @property
    def tournament_banner(self):
        return self.page.locator('.tourn-item')

    @property
    def banking_item(self):
        return self.page.locator('.payment-list__block > .payment-list__block-wrapper>:first-child').first


    @property
    def shield_jackpot(self):
        return self.page.locator('xpath=//*[@id="root"]/div[2]/main/div/div[1]/div/div/div[1]/div')

    @property
    def legend_title(self):
        return self.page.locator('xpath=//*[@id="root"]/div[2]/main/div/div/div/div/div[2]/div/h2')
