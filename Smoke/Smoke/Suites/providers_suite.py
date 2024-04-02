import pytest
import time
from playwright.sync_api import Playwright, sync_playwright, expect, Page

class TestDataProviders():
    provider_names = [
        "1spin4win 1spin4win106",
        "3 Oaks 3 Oaks83",
        "4theplayer 4theplayer27",
        "7mojos 7mojos28",
        "Acerun Acerun4",
        "Amatic Amatic189",
        "Apparat Gaming Apparat Gaming31",
        "Authentic Gaming Authentic Gaming26",
        "AvatarUX AvatarUX28",
        "Baddingo Baddingo1",
        "Bangbanggames Bangbanggames13",
        "Belatra Belatra100",
        "Beterlive Beterlive14",
        "BGaming BGaming142",
        "BigTimeGaming BigTimeGaming42",
        "Blueprint Blueprint65",
        "Boomerangstudios Boomerangstudios2",
        "Booming Games Booming Games164",
        "Betsoft Gaming Betsoft Gaming167",
        "Bulletproof Bulletproof11",
        "Eagaming Eagaming83",
        "AMUSNET AMUSNET202",
        "Elcasino Elcasino1",
        "Endorphina Endorphina153",
        "Evolution Evolution398",
        "Evoplay Entertainment Evoplay Entertainment235",
        "Eyecon Eyecon59",
        "Ezugi Ezugi70",
        "Fazi Fazi206",
        "Felix Gaming Felix Gaming1",
        "Fugaso Fugaso46",
        "GameArt GameArt156",
        "Gamebeat Gamebeat28",
        "Gamevy Gamevy3",
        "Gamzix Gamzix48",
        "Goldenhero Goldenhero17",
        "Habanero Habanero204",
        "High 5 High 5250",
        "Hotrisegames Hotrisegames2",
        "iSoftBet iSoftBet201",
        "Jelly Jelly6",
        "KA Gaming KA Gaming650",
        "Lucky Lucky70",
        "Mancala Gaming Mancala Gaming54",
        "Mascot Mascot83",
        "Mplay Mplay18",
        "Netent Netent181",
        "Nolimit Nolimit83",
        "Nucleus Gaming Nucleus Gaming124",
        "Onlyplay Onlyplay66",
        "Peter and Sons Peter and Sons21",
        "Platipus Platipus110",
        "Play'n GO Play'n GO332",
        "Playson Playson77",
        "Playtech Playtech362",
        "Popiplay Popiplay35",
        "Pragmatic Play Pragmatic Play380",
        "Push Gaming Push Gaming41",
        "Games Global Games Global1k+",
        "Quickspin Quickspin107",
        "Red Tiger Gaming Red Tiger Gaming264",
        "Reelplay Reelplay36",
        "Reevo Reevo34",
        "Reflexgaming Reflexgaming18",
        "Relax Gaming Relax Gaming299",
        "Retrogaming Retrogaming68",
        "Slotopia Slotopia25",
        "SmartSoft SmartSoft53",
        "Spinomenal Spinomenal385",
        "Spribe Spribe8",
        "Swintt Swintt134",
        "Thunderkick Thunderkick77",
        "Tom Horn Tom Horn70",
        "Turbogames Turbogames29",
        "Tvbet Tvbet8",
        "Vivo Gaming Vivo Gaming2",
        "Wazdan Wazdan233",
        "Winfast Winfast16",
        "Winfinity Winfinity15",
        "Yggdrasil Yggdrasil126"
    ]

class ProvidersTest():
    def __init__(self, page: Page):
        self.page = page
        
    @pytest.mark.parametrize("provider_name", TestDataProviders.provider_names)
    def test_provider_play(self, provider_name: str) -> None:
        self.page.goto("https://www.kingbillycasino.com/")
        self.page.get_by_role("button", name="accept").click()
        self.page.locator("#games-page-providers-filter i").nth(1).click()
        self.page.get_by_role("link", name=provider_name).click()
        time.sleep(3)
        if self.page.locator("div:nth-child(1) > .game > .game__wrapper > .game__action").is_visible():
            self.page.locator(".game__play").first.click()
            time.sleep(2)
            pass
        else:
            raise AssertionError(f"No games are found for provider: {provider_name}")

