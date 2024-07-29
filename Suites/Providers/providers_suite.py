import pytest
import time
from playwright.sync_api import Playwright, sync_playwright, expect, Page
from Suites.Base.base_setup import BaseSetUp

class TestDataProviders():
    provider_names = [
        "1spin4win",
        "3 Oaks ",
        "4theplayer",
        "7mojos",
        "Acerun",
        "Amatic",
        "Apparat Gaming",
        "Authentic Gaming",
        "AvatarUX",
        "Baddingo",
        "Bangbanggames",
        "Belatra",
        "Beterlive",
        "BGaming",
        "BigTimeGaming",
        "Blueprint",
        "Boomerangstudios",
        "Booming Games",
        "Betsoft Gaming",
        "Bulletproof",
        "Eagaming",
        "AMUSNET",
        "Elcasino",
        "Endorphina",
        "Evolution",
        "Evoplay Entertainment",
        "Eyecon",
        "Ezugi",
        "Fazi",
        "Felix Gaming",
        "Fugaso",
        "GameArt",
        "Gamebeat",
        "Gamevy",
        "Gamzix",
        "Goldenhero",
        "Habanero",
        "High 5",
        "Hotrisegames",
        "iSoftBet",
        "Jelly",
        "KA Gaming",
        "Lucky",
        "Mancala Gaming",
        "Mascot",
        "Mplay",
        "Netent",
        "Nolimit",
        "Nucleus Gaming",
        "Onlyplay",
        "Peter and Sons",
        "Platipus",
        "Play'n GO",
        "Playson",
        "Playtech",
        "Popiplay",
        "Pragmatic Play",
        "Push Gaming",
        "Games Global",
        "Quickspin",
        "Red Tiger Gaming",
        "Reelplay",
        "Reevo",
        "Reflexgaming",
        "Relax Gaming",
        "Retrogaming",
        "Slotopia",
        "SmartSoft",
        "Spinomenal",
        "Spribe",
        "Swintt",
        "Thunderkick",
        "Tom Horn",
        "Turbogames",
        "Tvbet",
        "Vivo Gaming",
        "Wazdan",
        "Winfast",
        "Winfinity",
        "Yggdrasil"
    ]

class ProvidersTest(BaseSetUp):

        
    @pytest.mark.parametrize("provider_name", TestDataProviders.provider_names)
    def test_provider_play(self, provider_name: str) -> None:
        super().set_up()
        self.accept_cookie_button.click()
        self.page.locator("#games-page-providers-filter i").nth(1).click()
        self.page.get_by_role("link", name=provider_name).click()
        time.sleep(3)
        if self.page.locator("div:nth-child(1) > .game > .game__wrapper > .game__action").is_visible():
            self.page.locator(".game__play").first.click()
            time.sleep(2)
            pass
        else:
            raise AssertionError(f"No games are found for provider: {provider_name}")

